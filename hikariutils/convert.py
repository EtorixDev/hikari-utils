import math
import typing

import whenever

from hikariutils.constants import DISCORD_EPOCH, TWITTER_EPOCH, UNIX_EPOCH
from hikariutils.regex import URLS


def snowflake_to_datetime(id: int, source: typing.Literal["DISCORD", "TWITTER", "UNIX"]) -> whenever.ZonedDateTime:
    """Convert a snowflake into a whenever datetime."""
    epoch = DISCORD_EPOCH if source == "DISCORD" else TWITTER_EPOCH if source == "TWITTER" else UNIX_EPOCH
    timestamp = ((id >> 22) + (epoch.timestamp() * 1000)) / 1000
    return whenever.ZonedDateTime.from_timestamp(timestamp, tz="UTC")


def jump_url(guild_id: int, channel_id: int | None = None, message_id: int | None = None) -> str:
    """Build a jump url for a Discord channel or message."""
    return f"https://discord.com/channels/{guild_id}" + (f"/{channel_id}" if channel_id else "") + (f"/{message_id}" if message_id else "")


def jump_hyperlink(guild_id: int, channel_id: int | None = None, message_id: int | None = None, text: str | None = None) -> str:
    """Build a jump hyperlink for a Discord channel or message."""
    return f"[{code_or_sanitize(text) if text else '`Jump`'}](<{jump_url(guild_id, channel_id, message_id)}>)"


def seconds(seconds: float, style: typing.Literal["Long", "Short", "Single"] = "Short") -> str:
    """
    Convert the provided seconds to one of the following styles:
    - Long: 1 week, 2 days, 3 hours, 4 minutes, and 5 seconds
    - Short: 1w 2d 3h 4m 5s
    - Single: 1.5 Days or 1 Hour, etc.
    """

    if style == "Single":
        if seconds >= 86400:
            days = seconds / 86400
            return f"{str(round(days, 2)).removesuffix('.0')} day{'s' if seconds > 86400 else ''}"

        if seconds >= 3600:
            hours = seconds / 3600
            return f"{str(round(hours, 2)).removesuffix('.0')} hour{'s' if seconds > 3600 else ''}"

        if seconds >= 60:
            minutes = seconds / 60
            return f"{str(round(minutes, 2)).removesuffix('.0')} minute{'s' if seconds > 60 else ''}"

        return f"{str(round(seconds, 2)).removesuffix('.0')} second{'s' if seconds != 1 else ''}"

    output: list[float | str] = []

    if seconds == 0:
        output.append(seconds)
        output.append("second" if style == "Long" else "s")
    if seconds >= 604800:
        weeks = math.floor(seconds / 604800)
        seconds = seconds % 604800
        output.append(weeks)
        output.append("week" if style == "Long" else "w")
    if seconds >= 86400:
        days = math.floor(seconds / 86400)
        seconds = seconds % 86400
        output.append(days)
        output.append("day" if style == "Long" else "d")
    if seconds >= 3600:
        hours = math.floor(seconds / 3600)
        seconds = seconds % 3600
        output.append(hours)
        output.append("hour" if style == "Long" else "h")
    if seconds >= 60:
        minutes = math.floor(seconds / 60)
        seconds = int(seconds % 60)
        output.append(minutes)
        output.append("minute" if style == "Long" else "m")
    if seconds > 0:
        minutes = math.floor(seconds)
        output.append(seconds)
        output.append("second" if style == "Long" else "s")

    x = 0
    output_str = ""

    if style == "Long":
        while len(output) > x:
            output_str += f"{'and ' if len(output) == x + 2 and len(output) != 2 else ''}{str(output[x]).removesuffix('.0')} {output[x + 1]}{'s' if output[x] != 1 else ''}{', ' if len(output) > x + 2 and len(output) > 4 else ' ' if len(output) == 4 else ''}"
            x += 2
    else:
        while len(output) > x:
            output_str += f"{str(output[x])}"
            x += 1

    return output_str.strip()


def sanitize_markdown(text: str, ignore_urls: bool = True) -> str:
    """Sanitize all markdown by adding backslashes before the characters."""
    urls: list[str] = []

    if ignore_urls:
        urls = URLS.findall(text)

        for index, url in enumerate(urls):
            text = text.replace(url, f"URLPLACEHOLDER{index}")

    sanitized_text = text.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|").replace("*", "\\*").replace("~", "\\~").replace(">", "\\>").replace("#", "\\#").replace("@", "\\@").replace("_", "\\_")

    if ignore_urls:
        for index, url in enumerate(urls):
            sanitized_text = sanitized_text.replace(f"URLPLACEHOLDER{index}", url)

    return sanitized_text


def sanitize_quote_code(text: str) -> str:
    """Sanitize quotation markdown and code block markdown."""
    return text.replace("`", "\\`").replace(">", "\\>")


def code_or_sanitize(text: str) -> str:
    """Return the text in a single code block if the text contains no graves, otherwise return the text with markdown sanitized."""
    return f"`{text}`" if text and "`" not in text else f"{sanitize_markdown(text)}" if text else ""

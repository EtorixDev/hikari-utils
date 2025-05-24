import datetime
import typing
from datetime import timedelta, timezone

import dateparser
import whenever

from hikariutils.constants import UNIX_EPOCH
from hikariutils.convert import snowflake_to_datetime


def is_float(term: str) -> bool:
    """Check if the input is a number."""
    try:
        float(term)
        return True
    except ValueError:
        return False


def human_time(date_and_time: str) -> tuple[int, int, float, str, str] | tuple[None, None, None, None, None]:
    """Find the timestamp and timezone information for a human time representation.

    Returns a tuple containing:
    - The UNIX timestamp in seconds.
    - The UNIX timestamp in milliseconds.
    - The difference in seconds from the current time.
    - The timezone name.
    - The UTC offset.
    """
    try:
        tz_name: str | None = None
        target_date: whenever.ZonedDateTime | datetime.datetime | None = None
        target_date_timestamp: float | None = None

        if is_float(date_and_time):
            date_and_time_float: float = float(date_and_time)

            if len(date_and_time) >= 17:
                target_date = snowflake_to_datetime(int(date_and_time), "DISCORD")
            elif date_and_time_float > 32536850399:
                target_date = whenever.ZonedDateTime.from_timestamp(date_and_time_float / 1000, tz="UTC")
            else:
                target_date = whenever.ZonedDateTime.from_timestamp(date_and_time_float, tz="UTC")

            target_date_timestamp = target_date.timestamp_millis()
        else:
            if any([term in date_and_time.lower() for term in ["x.com", "twitter.com"]]):
                target_date = snowflake_to_datetime(int(date_and_time), "TWITTER")
                target_date_timestamp = target_date.timestamp_millis()
            else:
                target_date = dateparser.parse(date_and_time)

                if target_date and not target_date.tzname():
                    date_and_time += " UTC"
                    target_date = dateparser.parse(date_and_time)

                if not target_date or not target_date.tzname() or not target_date.utcoffset():
                    return (None, None, None, None, None)

                tz_name = target_date.tzname()
                target_date_timestamp = target_date.timestamp() * 1000

        if tz_name and isinstance(target_date, datetime.datetime):
            # Extract Timezone + Abbreviation + Offset
            target_timezone_name = typing.cast(str, tz_name).replace("\\", "")
            target_timezone_offset_seconds = int(typing.cast(timedelta, target_date.utcoffset()).total_seconds())
            target_timezone_offset_hours = target_timezone_offset_seconds // 3600
            target_timezone_offset_minutes = (target_timezone_offset_seconds % 3600) // 60
            target_timezone = timezone(timedelta(seconds=target_timezone_offset_seconds))
            target_timezone_offset = f"{'-' if target_timezone_offset_seconds < 0 else '+'}{abs(target_timezone_offset_hours):02d}:{abs(target_timezone_offset_minutes):02d}"
            # Reparse With Timezone As Base
            target_date = dateparser.parse(date_and_time, settings={"RELATIVE_TIMEZONE": target_timezone})  # type: ignore
        else:
            target_timezone_name = "UTC"
            target_timezone_offset = "+00:00"

        if not target_date:
            return (None, None, None, None, None)

        # Content Output Display
        target_date_unix_millis = int(target_date_timestamp - UNIX_EPOCH.timestamp_millis())
        target_date_unix_seconds = int(target_date_unix_millis / 1000)
        difference_in_seconds = max(round(target_date_timestamp - whenever.Instant.now().timestamp(), 3), 0)

        return (target_date_unix_seconds, target_date_unix_millis, difference_in_seconds, target_timezone_name, target_timezone_offset)
    except Exception:
        return (None, None, None, None, None)

import typing

import emoji
import hikari

from hikariutils.errors import MandatoryBanNotFound, MandatoryChannelNotFound, MandatoryEmojiNotFound, MandatoryGuildNotFound, MandatoryMemberNotFound, MandatoryRoleNotFound, MandatoryUserNotFound


class Optional:
    """Retrieve an object from the cache or fetch it from Discord if not found. Return None if still not found."""

    @staticmethod
    async def guild(bot: hikari.GatewayBot, guild: int | hikari.Guild | None, cache: bool = True) -> hikari.Guild | None:
        """Retrieve a guild from the cache. If not found, fetch it from Discord. Return None if still not found."""
        guild = await _guild(bot, guild, mandatory=False, cache=cache)
        return guild

    @staticmethod
    async def ban(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.User) -> hikari.GuildBan | None:
        """Fetch a ban for a guild member. Return None if not found."""
        return await _ban(bot, guild, member)

    @staticmethod
    async def user(bot: hikari.GatewayBot, user: int | hikari.User, cache: bool = True) -> hikari.User | None:
        """Retrieve a user from the cache. If not found, fetch it from Discord. Return None if still not found."""
        return await _user(bot, user, mandatory=False, cache=cache)

    @staticmethod
    async def member(bot: hikari.GatewayBot, guild: int | hikari.Guild, user: int | hikari.User, cache: bool = True) -> hikari.Member | None:
        """Retrieve a member from the cache. If not found, fetch it from Discord. Return None if still not found."""
        return await _member(bot, guild, user, mandatory=False, cache=cache)

    @staticmethod
    async def members(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> typing.Iterable[hikari.Member] | None:
        """Retrieve members from the cache. If not found, fetch them from Discord. Return None if still not found."""
        return await _members(bot, guild, mandatory=False, cache=cache)

    @staticmethod
    async def boosters(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> list[hikari.Member] | None:
        """Retrieve boosters for a guild from the cache. If not found, fetch them from Discord. Return None if still not found."""
        return await _boosters(bot, guild, mandatory=False, cache=cache)

    @staticmethod
    async def channel(bot: hikari.GatewayBot, channel: int | hikari.GuildChannel, cache: bool = True) -> hikari.GuildChannel | hikari.DMChannel | None:
        """Retrieve a guild channel from the cache. If not found, fetch it from Discord. Return None if still not found."""
        return await _channel(bot, channel, mandatory=False, cache=cache)

    @staticmethod
    async def channels(bot: hikari.GatewayBot, guild: int | hikari.Guild, channel_type: hikari.ChannelType | None = None, cache: bool = True) -> typing.Iterable[hikari.GuildChannel] | None:
        """Retrieve guild channels from the cache. If not found, fetch them from Discord. Optionally filters by channel type. Return None if still not found."""
        return await _channels(bot, guild, channel_type, mandatory=False, cache=cache)

    @staticmethod
    async def role(bot: hikari.GatewayBot, guild: int | hikari.Guild, role: int | hikari.Role, cache: bool = True) -> hikari.Role | None:
        """Retrieve a role from the cache. If not found, fetch it from Discord. Return None if still not found."""
        return await _role(bot, guild, role, mandatory=False, cache=cache)

    @staticmethod
    async def roles(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> typing.Iterable[hikari.Role] | None:
        """Retrieve roles from the cache. If not found, fetch them from Discord. Return None if still not found."""
        return await _roles(bot, guild, mandatory=False, cache=cache)

    @staticmethod
    async def top_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.Member, cache: bool = True) -> hikari.Role | None:
        """Retrieve the top role for a member in a guild. If not found, fetch it from Discord. Return None if still not found."""
        return await _top_role(bot, guild, member, mandatory=False, cache=cache)

    @staticmethod
    async def booster_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> hikari.Role | None:
        """Retrieve the booster role for a guild. If not found, fetch it from Discord. Return None if still not found."""
        return await _booster_role(bot, guild, mandatory=False, cache=cache)

    @staticmethod
    async def emoji(bot: hikari.GatewayBot | None, emoji_id: int | str | hikari.Emoji, guild: int | hikari.Guild | None = None, cache: bool = True) -> hikari.Emoji | None:
        """Retrieve an emoji from the cache. If not found, fetch it from Discord. Return None if still not found."""
        return await _emoji(bot, emoji_id, guild, mandatory=False, cache=cache)


class Mandatory:
    """Retrieve an object from the cache or fetch it from Discord if not found. Raise an exception if still not found."""

    @staticmethod
    async def guild(bot: hikari.GatewayBot, guild: int | hikari.Guild | None, cache: bool = True) -> hikari.Guild:
        """Retrieve a guild from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        guild = await _guild(bot, guild, mandatory=True, cache=cache)

        if not guild:
            raise MandatoryGuildNotFound

        return guild

    @staticmethod
    async def ban(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.User) -> hikari.GuildBan:
        """Fetch a ban for a guild member. Raise an exception if not found."""
        resolved_ban = await _ban(bot, guild, member)

        if not resolved_ban:
            raise MandatoryBanNotFound

        return resolved_ban

    @staticmethod
    async def user(bot: hikari.GatewayBot, user: int | hikari.User, cache: bool = True) -> hikari.User:
        """Retrieve a user from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_user = await _user(bot, user, mandatory=True, cache=cache)

        if not resolved_user:
            raise MandatoryUserNotFound

        return resolved_user

    @staticmethod
    async def member(bot: hikari.GatewayBot, guild: int | hikari.Guild, user: int | hikari.User, cache: bool = True) -> hikari.Member:
        """Retrieve a member from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_member = await _member(bot, guild, user, mandatory=True, cache=cache)

        if not resolved_member:
            raise MandatoryMemberNotFound

        return resolved_member

    @staticmethod
    async def members(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> typing.Iterable[hikari.Member]:
        """Retrieve members from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
        resolved_members = await _members(bot, guild, mandatory=True, cache=cache)

        if not resolved_members:
            raise MandatoryMemberNotFound

        return resolved_members

    @staticmethod
    async def boosters(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> list[hikari.Member]:
        """Retrieve boosters for a guild from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
        resolved_boosters = await _boosters(bot, guild, mandatory=True, cache=cache)

        if not resolved_boosters:
            raise MandatoryMemberNotFound

        return resolved_boosters

    @staticmethod
    async def channel(bot: hikari.GatewayBot, channel: int | hikari.GuildChannel, cache: bool = True) -> hikari.GuildChannel | hikari.DMChannel | None:
        """Retrieve a guild channel from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_channel = await _channel(bot, channel, mandatory=True, cache=cache)

        if not resolved_channel:
            raise MandatoryChannelNotFound

        return resolved_channel

    @staticmethod
    async def channels(bot: hikari.GatewayBot, guild: int | hikari.Guild, channel_type: hikari.ChannelType | None, cache: bool = True) -> typing.Iterable[hikari.GuildChannel]:
        """Retrieve guild channels from the cache. If not found, fetch them from Discord. Optionally filters by channel type. Raise an exception if still not found."""
        resolved_channels = await _channels(bot, guild, channel_type, mandatory=True, cache=cache)

        if not resolved_channels:
            raise MandatoryChannelNotFound

        return resolved_channels

    @staticmethod
    async def role(bot: hikari.GatewayBot, guild: int | hikari.Guild, role: int | hikari.Role, cache: bool = True) -> hikari.Role:
        """Retrieve a role from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_role = await _role(bot, guild, role, mandatory=True, cache=cache)

        if not resolved_role:
            raise MandatoryRoleNotFound

        return resolved_role

    @staticmethod
    async def roles(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> typing.Iterable[hikari.Role]:
        """Retrieve roles from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
        resolved_roles = await _roles(bot, guild, mandatory=True, cache=cache)

        if not resolved_roles:
            raise MandatoryRoleNotFound

        return resolved_roles

    @staticmethod
    async def top_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.Member, cache: bool = True) -> hikari.Role:
        """Retrieve the top role for a member in a guild. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_top_role = await _top_role(bot, guild, member, mandatory=True, cache=cache)

        if not resolved_top_role:
            raise MandatoryRoleNotFound

        return resolved_top_role

    @staticmethod
    async def booster_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, cache: bool = True) -> hikari.Role:
        """Retrieve the booster role for a guild. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_role = await _booster_role(bot, guild, mandatory=True, cache=cache)

        if not resolved_role:
            raise MandatoryRoleNotFound

        return resolved_role

    @staticmethod
    async def emoji(bot: hikari.GatewayBot | None, emoji_id: int | str | hikari.Emoji, guild: int | hikari.Guild | None, cache: bool = True) -> hikari.Emoji:
        """Retrieve an emoji from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
        resolved_emoji = await _emoji(bot, emoji_id, guild, mandatory=True, cache=cache)

        if not resolved_emoji:
            raise MandatoryEmojiNotFound

        return resolved_emoji


async def _guild(bot: hikari.GatewayBot, guild: int | hikari.Guild | None, mandatory: bool = False, cache: bool = True) -> hikari.Guild | None:
    try:
        if not guild:
            raise MandatoryGuildNotFound
        resolved_guild = (bot.cache.get_guild(guild) if cache else None) or (await bot.rest.fetch_guild(guild))
    except hikari.NotFoundError:
        resolved_guild = None

    if not resolved_guild and mandatory:
        raise MandatoryGuildNotFound

    return resolved_guild


async def _ban(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.User) -> hikari.GuildBan | None:
    try:
        return await bot.rest.fetch_ban(guild, member)
    except hikari.NotFoundError:
        return None


async def _user(bot: hikari.GatewayBot, user: int | hikari.User, mandatory: bool = False, cache: bool = True) -> hikari.User | None:
    try:
        resolved_user = (bot.cache.get_user(user) if cache else None) or (await bot.rest.fetch_user(user))
    except hikari.NotFoundError:
        resolved_user = None

    if not resolved_user and mandatory:
        raise MandatoryUserNotFound

    return resolved_user


async def _member(bot: hikari.GatewayBot, guild: int | hikari.Guild, user: int | hikari.User, mandatory: bool = False, cache: bool = True) -> hikari.Member | None:
    try:
        resolved_member = (bot.cache.get_member(guild, user) if cache else None) or (await bot.rest.fetch_member(guild, user))
    except hikari.NotFoundError:
        resolved_member = None

    if not resolved_member and mandatory:
        raise MandatoryMemberNotFound

    return resolved_member


async def _members(bot: hikari.GatewayBot, guild: int | hikari.Guild, mandatory: bool = False, cache: bool = True) -> typing.Iterable[hikari.Member] | None:
    try:
        resolved_members = (bot.cache.get_members_view_for_guild(guild if isinstance(guild, int) else guild.id).values() if cache else None) or (await bot.rest.fetch_members(guild))
    except hikari.NotFoundError:
        resolved_members = None

    if not resolved_members and mandatory:
        raise MandatoryMemberNotFound

    return resolved_members


async def _boosters(bot: hikari.GatewayBot, guild: int | hikari.Guild, mandatory: bool = False, cache: bool = True) -> list[hikari.Member] | None:
    try:
        resolved_members = (await _members(bot, guild, mandatory, cache)) or []
        resolved_boosters = [member for member in resolved_members if member.premium_since] or None
    except hikari.NotFoundError:
        resolved_boosters = None

    if not resolved_boosters and mandatory:
        raise MandatoryMemberNotFound

    return resolved_boosters


async def _channel(bot: hikari.GatewayBot, channel: int | hikari.GuildChannel, mandatory: bool = False, cache: bool = True) -> hikari.GuildChannel | hikari.DMChannel | None:
    try:
        resolved_channel = ((bot.cache.get_guild_channel(channel) or bot.cache.get_thread(channel)) if cache else None) or (await bot.rest.fetch_channel(channel))
    except hikari.NotFoundError:
        resolved_channel = None

    if (not resolved_channel and mandatory) or (resolved_channel and not isinstance(resolved_channel, (hikari.GuildChannel | hikari.DMChannel))):
        raise MandatoryChannelNotFound

    return resolved_channel


async def _channels(bot: hikari.GatewayBot, guild: int | hikari.Guild, channel_type: hikari.ChannelType | None = None, mandatory: bool = False, cache: bool = True) -> typing.Iterable[hikari.GuildChannel] | None:
    try:
        resolved_channels = (bot.cache.get_guild_channels_view_for_guild(guild).values() if cache else None) or (await bot.rest.fetch_guild_channels(guild))
        resolved_filtered = [channel for channel in resolved_channels if not channel_type or channel.type is channel_type] or None
    except hikari.NotFoundError:
        resolved_filtered = None

    if not resolved_filtered and mandatory:
        raise MandatoryChannelNotFound

    return resolved_filtered


async def _role(bot: hikari.GatewayBot, guild: int | hikari.Guild, role: int | hikari.Role, mandatory: bool = False, cache: bool = True) -> hikari.Role | None:
    try:
        role_id = role if isinstance(role, int) else role.id
        resolved_role = bot.cache.get_role(role_id)

        if not resolved_role:
            roles = (await _roles(bot, guild, mandatory, cache)) or []

            for role in roles:
                if role.id == role_id:
                    resolved_role = role
                    break
    except hikari.NotFoundError:
        resolved_role = None

    if not resolved_role and mandatory:
        raise MandatoryRoleNotFound

    return resolved_role


async def _roles(bot: hikari.GatewayBot, guild: int | hikari.Guild, mandatory: bool = False, cache: bool = True) -> typing.Iterable[hikari.Role] | None:
    try:
        resolved_roles = (bot.cache.get_roles_view_for_guild(guild).values() if cache else None) or (await bot.rest.fetch_roles(guild))
    except hikari.NotFoundError:
        resolved_roles = None

    if not resolved_roles and mandatory:
        raise MandatoryRoleNotFound

    return resolved_roles


async def _top_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, member: int | hikari.Member, mandatory: bool = False, cache: bool = True) -> hikari.Role | None:
    try:
        if isinstance(member, int):
            resolved_member = typing.cast(hikari.Member, await _member(bot, guild, member, mandatory=True, cache=cache))
        else:
            resolved_member = member

        top_role = resolved_member.get_top_role() if cache else None

        if not top_role:
            roles = await resolved_member.fetch_roles()
            top_role = max(roles, key=lambda role: role.position, default=None)
    except hikari.NotFoundError:
        top_role = None

    if not top_role and mandatory:
        raise MandatoryRoleNotFound

    return top_role


async def _booster_role(bot: hikari.GatewayBot, guild: int | hikari.Guild, mandatory: bool = False, cache: bool = True) -> hikari.Role | None:
    try:
        resolved_role = None
        roles = (await _roles(bot, guild, mandatory, cache)) or []

        for role in roles:
            if role.is_premium_subscriber_role:
                resolved_role = role
                break
    except hikari.NotFoundError:
        resolved_role = None

    if not resolved_role and mandatory:
        raise MandatoryRoleNotFound

    return resolved_role


async def _emoji(bot: hikari.GatewayBot | None, emoji_id: int | str | hikari.Emoji, guild: int | hikari.Guild | None = None, mandatory: bool = False, cache: bool = True) -> hikari.Emoji | None:
    try:
        resolved_emoji = None

        if isinstance(emoji_id, hikari.Emoji):
            resolved_emoji = emoji_id
        elif isinstance(emoji_id, str):
            if emoji_id in emoji.EMOJI_DATA:
                resolved_emoji = hikari.UnicodeEmoji.parse(emoji_id)
            else:
                try:
                    resolved_emoji = hikari.CustomEmoji.parse(emoji_id)
                except ValueError:
                    pass
        else:
            try:
                if (unicode_char := chr(emoji_id)) in emoji.EMOJI_DATA:
                    resolved_emoji = hikari.UnicodeEmoji.parse(unicode_char)
            except ValueError:
                if bot:
                    resolved_emoji = bot.cache.get_emoji(emoji_id) if cache else None

                    if not resolved_emoji and guild:
                        resolved_emoji = await bot.rest.fetch_emoji(guild, emoji_id)
    except hikari.NotFoundError:
        resolved_emoji = None

    if not resolved_emoji and mandatory:
        raise MandatoryRoleNotFound

    return resolved_emoji

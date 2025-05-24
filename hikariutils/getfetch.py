import typing

import emoji as emojis
import hikari

from hikariutils.errors import InvalidBot, MandatoryBanNotFound, MandatoryChannelNotFound, MandatoryEmojiNotFound, MandatoryGuildNotFound, MandatoryMemberNotFound, MandatoryRoleNotFound, MandatoryUserNotFound


class Optional:
    class Either:
        """Retrieve an object from the cache or fetch it from Discord if not found. Return None if still not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.GatewayGuild | hikari.RESTGuild | None:
            """Retrieve a guild from the cache. If not found, fetch it from Discord. Return None if still not found."""
            return await _either_guild(bot, guild)

        @staticmethod
        async def banned(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.GuildBan | None:
            """Retrieve a ban by fetching it from Discord. Return None if not found."""
            return await _rest_banned(bot, guild, user)

        @staticmethod
        async def user(
            bot: hikari.GatewayBot | hikari.RESTBot,
            user: int | hikari.User | None,
        ) -> hikari.User | None:
            """Retrieve a user from the cache. If not found, fetch it from Discord. Return None if still not found."""
            return await _either_user(bot, user)

        @staticmethod
        async def member(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member | None:
            """Retrieve a member from the cache. If not found, fetch it from Discord. Return None if still not found."""
            return await _either_member(bot, guild, user)

        @staticmethod
        async def members(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve members from the cache. If not found, fetch them from Discord. Return None if still not found."""
            return await _either_members(bot, guild)

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve members from the cache. If not found, fetch them from Discord. Return None if still not found."""
            return await _either_boosters(bot, guild)

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel | None:
            """Retrieve a channel from the cache. If not found, fetch it from Discord. Return None if still not found."""
            return await _either_channel(bot, channel)

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
            """Retrieve channels from the cache. If not found, fetch them from Discord. Return None if still not found."""
            return await _either_channels(bot, guild)

        @staticmethod
        async def dms(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.PrivateChannel | None,
        ) -> hikari.PrivateChannel | None:
            """Retrieve a private channel by fetching from Discord. Return None if not found."""
            return await _rest_dms(bot, channel)

        @staticmethod
        async def dm(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.DMChannel | None,
        ) -> hikari.DMChannel | None:
            """Retrieve a DM channel by fetching from Discord. Return None if not found."""
            return await _rest_dm(bot, channel)

        @staticmethod
        async def group(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GroupDMChannel | None,
        ) -> hikari.GroupDMChannel | None:
            """Retrieve a group DM channel by fetching from Discord. Return None if not found."""
            return await _rest_group(bot, channel)

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel | None:
            """Retrieve a textable channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_textable(bot, channel)

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
            """Retrieve textable channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_textables(bot, guild)

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel | None:
            """Retrieve a permissible channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_permissible(bot, channel)

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
            """Retrieve permissible channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_permissibles(bot, guild)

        @staticmethod
        async def category(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory | None:
            """Retrieve a category channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_category(bot, channel)

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
            """Retrieve category channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_categories(bot, guild)

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel | None:
            """Retrieve a voice channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_voice(bot, channel)

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
            """Retrieve voice channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_voices(bot, guild)

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel | None:
            """Retrieve a stage channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_stage(bot, channel)

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
            """Retrieve stage channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_stages(bot, guild)

        @staticmethod
        async def text(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel | None:
            """Retrieve a text channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_text(bot, channel)

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
            """Retrieve text channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_texts(bot, guild)

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel | None:
            """Retrieve a thread channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_thread(bot, channel)

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
            """Retrieve thread channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_threads(bot, guild)

        @staticmethod
        async def public(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
            """Retrieve a public thread or news thread from the cache or fetch from Discord. Return None if not found."""
            return await _either_public(bot, channel)

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
            """Retrieve public/news threads from the cache or fetch from Discord. Return None if not found."""
            return await _either_publics(bot, guild)

        @staticmethod
        async def private(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread | None:
            """Retrieve a private thread from the cache or fetch from Discord. Return None if not found."""
            return await _either_private(bot, channel)

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
            """Retrieve private threads from the cache or fetch from Discord. Return None if not found."""
            return await _either_privates(bot, guild)

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel | None:
            """Retrieve a forum channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_forum(bot, channel)

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
            """Retrieve forum channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_forums(bot, guild)

        @staticmethod
        async def news(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel | None:
            """Retrieve a news channel from the cache or fetch from Discord. Return None if not found."""
            return await _either_news(bot, channel)

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
            """Retrieve news channels from the cache or fetch from Discord. Return None if not found."""
            return await _either_newses(bot, guild)

        @staticmethod
        async def role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role | None:
            """Retrieve a role from the cache or fetch from Discord. Return None if not found."""
            return await _either_role(bot, guild, role)

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
            """Retrieve roles belonging to a member or a guild from the cache or fetch from Discord. Return None if not found."""
            return await _either_roles(bot, guild, member)

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role | None:
            """Retrieve the top role of a member or guild from the cache or fetch from Discord. Return None if not found."""
            return await _either_top_role(bot, guild, member)

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role | None:
            """Retrieve the booster role of a guild from the cache or fetch from Discord. Return None if not found."""
            return await _either_booster_role(bot, guild)

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot | hikari.RESTBot,
            emoji: int | str | hikari.Emoji | None,
            guild: int | hikari.Guild | None = None,
        ) -> hikari.Emoji | None:
            """Retrieve an emoji from the cache or fetch from Discord. Return None if not found."""
            return await _either_emoji(bot, emoji, guild)

    class Cache:
        """Retrieve an object from the cache. Return None if not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.GatewayGuild | None:
            """Retrieve a guild from the cache. Return None if not found."""
            return await _cache_guild(bot, guild)

        @staticmethod
        async def user(
            bot: hikari.GatewayBot,
            user: int | hikari.User | None,
        ) -> hikari.User | None:
            """Retrieve a user from the cache. Return None if not found."""
            return await _cache_user(bot, user)

        @staticmethod
        async def member(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member | None:
            """Retrieve a member from the cache. Return None if not found."""
            return await _cache_member(bot, guild, user)

        @staticmethod
        async def members(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve members from the cache. Return None if not found."""
            return await _cache_members(bot, guild)

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve boosters from the cache. Return None if not found."""
            return await _cache_boosters(bot, guild)

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel | None:
            """Retrieve a channel from the cache. Return None if not found."""
            return await _cache_channel(bot, channel)

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
            """Retrieve channels from the cache. Return None if not found."""
            return await _cache_channels(bot, guild)

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel | None:
            """Retrieve a textable channel from the cache. Return None if not found."""
            return await _cache_textable(bot, channel)

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
            """Retrieve textable channels from the cache. Return None if not found."""
            return await _cache_textables(bot, guild)

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel | None:
            """Retrieve a permissible channel from the cache. Return None if not found."""
            return await _cache_permissible(bot, channel)

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
            """Retrieve permissible channels from the cache. Return None if not found."""
            return await _cache_permissibles(bot, guild)

        @staticmethod
        async def category(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory | None:
            """Retrieve a category channel from the cache. Return None if not found."""
            return await _cache_category(bot, channel)

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
            """Retrieve category channels from the cache. Return None if not found."""
            return await _cache_categories(bot, guild)

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel | None:
            """Retrieve a voice channel from the cache. Return None if not found."""
            return await _cache_voice(bot, channel)

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
            """Retrieve voice channels from the cache. Return None if not found."""
            return await _cache_voices(bot, guild)

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel | None:
            """Retrieve a stage channel from the cache. Return None if not found."""
            return await _cache_stage(bot, channel)

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
            """Retrieve stage channels from the cache. Return None if not found."""
            return await _cache_stages(bot, guild)

        @staticmethod
        async def text(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel | None:
            """Retrieve a text channel from the cache. Return None if not found."""
            return await _cache_text(bot, channel)

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
            """Retrieve text channels from the cache. Return None if not found."""
            return await _cache_texts(bot, guild)

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel | None:
            """Retrieve a thread channel from the cache. Return None if not found."""
            return await _cache_thread(bot, channel)

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
            """Retrieve thread channels from the cache. Return None if not found."""
            return await _cache_threads(bot, guild)

        @staticmethod
        async def public(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
            """Retrieve a public thread or news thread from the cache. Return None if not found."""
            return await _cache_public(bot, channel)

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
            """Retrieve public/news threads from the cache. Return None if not found."""
            return await _cache_publics(bot, guild)

        @staticmethod
        async def private(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread | None:
            """Retrieve a private thread from the cache. Return None if not found."""
            return await _cache_private(bot, channel)

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
            """Retrieve private threads from the cache. Return None if not found."""
            return await _cache_privates(bot, guild)

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel | None:
            """Retrieve a forum channel from the cache. Return None if not found."""
            return await _cache_forum(bot, channel)

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
            """Retrieve forum channels from the cache. Return None if not found."""
            return await _cache_forums(bot, guild)

        @staticmethod
        async def news(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel | None:
            """Retrieve a news channel from the cache. Return None if not found."""
            return await _cache_news(bot, channel)

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
            """Retrieve news channels from the cache. Return None if not found."""
            return await _cache_newses(bot, guild)

        @staticmethod
        async def role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role | None:
            """Retrieve a role from the cache. Return None if not found."""
            return await _cache_role(bot, guild, role)

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
            """Retrieve roles belonging to a member or a guild from the cache. Return None if not found."""
            return await _cache_roles(bot, guild, member)

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role | None:
            """Retrieve the top role of a member or guild from the cache. Return None if not found."""
            return await _cache_top_role(bot, guild, member)

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role | None:
            """Retrieve the booster role of a guild from the cache. Return None if not found."""
            return await _cache_booster_role(bot, guild)

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot,
            emoji: int | str | hikari.Emoji | None,
        ) -> hikari.Emoji | None:
            """Retrieve an emoji from the cache. Return None if not found."""
            return await _cache_emoji(bot, emoji)

    class Rest:
        """Retrieve an object by fetching it from Discord. Return None if not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.RESTGuild | None:
            """Retrieve a guild by fetching it from Discord. Return None if not found."""
            return await _rest_guild(bot, guild)

        @staticmethod
        async def banned(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.GuildBan | None:
            """Retrieve a ban by fetching it from Discord. Return None if not found."""
            return await _rest_banned(bot, guild, user)

        @staticmethod
        async def user(
            bot: hikari.GatewayBot | hikari.RESTBot,
            user: int | hikari.User | None,
        ) -> hikari.User | None:
            """Retrieve a user by fetching it from Discord. Return None if not found."""
            return await _rest_user(bot, user)

        @staticmethod
        async def member(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member | None:
            """Retrieve a member by fetching it from Discord. Return None if not found."""
            return await _rest_member(bot, guild, user)

        @staticmethod
        async def members(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve members by fetching them from Discord. Return None if not found."""
            return await _rest_members(bot, guild)

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
            """Retrieve boosters by fetching them from Discord. Return None if not found."""
            return await _rest_boosters(bot, guild)

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel | None:
            """Retrieve a channel by fetching it from Discord. Return None if not found."""
            return await _rest_channel(bot, channel)

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
            """Retrieve channels by fetching them from Discord. Return None if not found."""
            return await _rest_channels(bot, guild)

        @staticmethod
        async def dms(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.PrivateChannel | None,
        ) -> hikari.PrivateChannel | None:
            """Retrieve a private channel by fetching it from Discord. Return None if not found."""
            return await _rest_dms(bot, channel)

        @staticmethod
        async def dm(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.DMChannel | None,
        ) -> hikari.DMChannel | None:
            """Retrieve a DM channel by fetching it from Discord. Return None if not found."""
            return await _rest_dm(bot, channel)

        @staticmethod
        async def group(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GroupDMChannel | None,
        ) -> hikari.GroupDMChannel | None:
            """Retrieve a group DM channel by fetching it from Discord. Return None if not found."""
            return await _rest_group(bot, channel)

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel | None:
            """Retrieve a textable channel by fetching it from Discord. Return None if not found."""
            return await _rest_textable(bot, channel)

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
            """Retrieve textable channels by fetching them from Discord. Return None if not found."""
            return await _rest_textables(bot, guild)

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel | None:
            """Retrieve a permissible channel by fetching it from Discord. Return None if not found."""
            return await _rest_permissible(bot, channel)

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
            """Retrieve permissible channels by fetching them from Discord. Return None if not found."""
            return await _rest_permissibles(bot, guild)

        @staticmethod
        async def category(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory | None:
            """Retrieve a category channel by fetching it from Discord. Return None if not found."""
            return await _rest_category(bot, channel)

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
            """Retrieve category channels by fetching them from Discord. Return None if not found."""
            return await _rest_categories(bot, guild)

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel | None:
            """Retrieve a voice channel by fetching it from Discord. Return None if not found."""
            return await _rest_voice(bot, channel)

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
            """Retrieve voice channels by fetching them from Discord. Return None if not found."""
            return await _rest_voices(bot, guild)

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel | None:
            """Retrieve a stage channel by fetching it from Discord. Return None if not found."""
            return await _rest_stage(bot, channel)

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
            """Retrieve stage channels by fetching them from Discord. Return None if not found."""
            return await _rest_stages(bot, guild)

        @staticmethod
        async def text(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel | None:
            """Retrieve a text channel by fetching it from Discord. Return None if not found."""
            return await _rest_text(bot, channel)

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
            """Retrieve text channels by fetching them from Discord. Return None if not found."""
            return await _rest_texts(bot, guild)

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel | None:
            """Retrieve a thread channel by fetching it from Discord. Return None if not found."""
            return await _rest_thread(bot, channel)

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
            """Retrieve thread channels by fetching them from Discord. Return None if not found."""
            return await _rest_threads(bot, guild)

        @staticmethod
        async def public(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
            """Retrieve a public thread or news thread by fetching it from Discord. Return None if not found."""
            return await _rest_public(bot, channel)

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
            """Retrieve public/news threads by fetching them from Discord. Return None if not found."""
            return await _rest_publics(bot, guild)

        @staticmethod
        async def private(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread | None:
            """Retrieve a private thread by fetching it from Discord. Return None if not found."""
            return await _rest_private(bot, channel)

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
            """Retrieve private threads by fetching them from Discord. Return None if not found."""
            return await _rest_privates(bot, guild)

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel | None:
            """Retrieve a forum channel by fetching it from Discord. Return None if not found."""
            return await _rest_forum(bot, channel)

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
            """Retrieve forum channels by fetching them from Discord. Return None if not found."""
            return await _rest_forums(bot, guild)

        @staticmethod
        async def news(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel | None:
            """Retrieve a news channel by fetching it from Discord. Return None if not found."""
            return await _rest_news(bot, channel)

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
            """Retrieve news channels by fetching them from Discord. Return None if not found."""
            return await _rest_newses(bot, guild)

        @staticmethod
        async def role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role | None:
            """Retrieve a role by fetching it from Discord. Return None if not found."""
            return await _rest_role(bot, guild, role)

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
            """Retrieve roles belonging to a member or a guild by fetching them from Discord. Return None if not found."""
            return await _rest_roles(bot, guild, member)

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role | None:
            """Retrieve the top role of a member or guild by fetching it from Discord. Return None if not found."""
            return await _rest_top_role(bot, guild, member)

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role | None:
            """Retrieve the booster role of a guild by fetching it from Discord. Return None if not found."""
            return await _rest_booster_role(bot, guild)

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot | hikari.RESTBot,
            emoji: int | str | hikari.Emoji | None,
            guild: int | hikari.Guild | None = None,
        ) -> hikari.Emoji | None:
            """Retrieve an emoji by fetching it from Discord. Return None if not found."""
            return await _rest_emoji(bot, emoji, guild)


class Mandatory:
    class Either:
        """Retrieve an object from the cache or fetch it from Discord if not found. Raise an exception if still not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.GatewayGuild | hikari.RESTGuild:
            """Retrieve a guild from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_guild := await _either_guild(bot, guild)):
                raise MandatoryGuildNotFound

            return resolved_guild

        @staticmethod
        async def banned(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.GuildBan:
            """Retrieve a ban by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_ban := await _rest_banned(bot, guild, user)):
                raise MandatoryBanNotFound

            return resolved_ban

        @staticmethod
        async def user(
            bot: hikari.GatewayBot | hikari.RESTBot,
            user: int | hikari.User | None,
        ) -> hikari.User:
            """Retrieve a user from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_user := await _either_user(bot, user)):
                raise MandatoryUserNotFound

            return resolved_user

        @staticmethod
        async def member(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member:
            """Retrieve a member from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_member := await _either_member(bot, guild, user)):
                raise MandatoryMemberNotFound

            return resolved_member

        @staticmethod
        async def members(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve members from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
            if not (resolved_members := await _either_members(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve boosters from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
            if not (resolved_members := await _either_boosters(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel:
            """Retrieve a channel from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_channel := await _either_channel(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel]:
            """Retrieve channels from the cache. If not found, fetch them from Discord. Raise an exception if still not found."""
            if not (resolved_channels := await _either_channels(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def dms(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.PrivateChannel | None,
        ) -> hikari.PrivateChannel:
            """Retrieve a private channel from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_channel := await _rest_dms(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def dm(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.DMChannel | None,
        ) -> hikari.DMChannel:
            """Retrieve a DM channel from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_channel := await _rest_dm(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def group(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GroupDMChannel | None,
        ) -> hikari.GroupDMChannel:
            """Retrieve a group DM channel from the cache. If not found, fetch it from Discord. Raise an exception if still not found."""
            if not (resolved_channel := await _rest_group(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel:
            """Retrieve a textable channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_textable(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel]:
            """Retrieve textable channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_textables(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel:
            """Retrieve a permissible channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_permissible(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel]:
            """Retrieve permissible channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_permissibles(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def category(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory:
            """Retrieve a category channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_category(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory]:
            """Retrieve category channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_categories(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel:
            """Retrieve a voice channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_voice(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel]:
            """Retrieve voice channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_voices(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel:
            """Retrieve a stage channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_stage(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel]:
            """Retrieve stage channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_stages(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def text(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel:
            """Retrieve a text channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_text(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel]:
            """Retrieve text channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_texts(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel:
            """Retrieve a thread channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_thread(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel]:
            """Retrieve thread channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_threads(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def public(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread:
            """Retrieve a public thread or news thread from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_public(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread]:
            """Retrieve public/news threads from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_publics(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def private(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread:
            """Retrieve a private thread from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_private(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread]:
            """Retrieve private threads from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_privates(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel:
            """Retrieve a forum channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_forum(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel]:
            """Retrieve forum channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_forums(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def news(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel:
            """Retrieve a news channel from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _either_news(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel]:
            """Retrieve news channels from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _either_newses(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role:
            """Retrieve a role from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_role := await _either_role(bot, guild, role)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role]:
            """Retrieve roles belonging to a member or a guild from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_roles := await _either_roles(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_roles

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role:
            """Retrieve the top role of a member or guild from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_role := await _either_top_role(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role:
            """Retrieve the booster role of a guild from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_role := await _either_booster_role(bot, guild)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot | hikari.RESTBot,
            emoji: int | str | hikari.Emoji | None,
            guild: int | hikari.Guild | None = None,
        ) -> hikari.Emoji:
            """Retrieve an emoji from the cache or fetch from Discord. Raise an exception if not found."""
            if not (resolved_emoji := await _either_emoji(bot, emoji, guild)):
                raise MandatoryEmojiNotFound

            return resolved_emoji

    class Cache:
        """Retrieve an object from the cache. Raise an exception if not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.GatewayGuild:
            """Retrieve a guild from the cache. Raise an exception if not found."""
            if not (resolved_guild := await _cache_guild(bot, guild)):
                raise MandatoryGuildNotFound

            return resolved_guild

        @staticmethod
        async def user(
            bot: hikari.GatewayBot,
            user: int | hikari.User | None,
        ) -> hikari.User:
            """Retrieve a user from the cache. Raise an exception if not found."""
            if not (resolved_user := await _cache_user(bot, user)):
                raise MandatoryUserNotFound

            return resolved_user

        @staticmethod
        async def member(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member:
            """Retrieve a member from the cache. Raise an exception if not found."""
            if not (resolved_member := await _cache_member(bot, guild, user)):
                raise MandatoryMemberNotFound

            return resolved_member

        @staticmethod
        async def members(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve members from the cache. Raise an exception if not found."""
            if not (resolved_members := await _cache_members(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve boosters from the cache. Raise an exception if not found."""
            if not (resolved_members := await _cache_boosters(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel:
            """Retrieve a channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_channel(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel]:
            """Retrieve channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_channels(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel:
            """Retrieve a textable channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_textable(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel]:
            """Retrieve textable channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_textables(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel:
            """Retrieve a permissible channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_permissible(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel]:
            """Retrieve permissible channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_permissibles(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def category(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory:
            """Retrieve a category channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_category(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory]:
            """Retrieve category channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_categories(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel:
            """Retrieve a voice channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_voice(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel]:
            """Retrieve voice channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_voices(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel:
            """Retrieve a stage channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_stage(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel]:
            """Retrieve stage channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_stages(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def text(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel:
            """Retrieve a text channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_text(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel]:
            """Retrieve text channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_texts(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel:
            """Retrieve a thread channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_thread(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel]:
            """Retrieve thread channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_threads(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def public(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread:
            """Retrieve a public thread or news thread from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_public(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread]:
            """Retrieve public/news threads from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_publics(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def private(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread:
            """Retrieve a private thread from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_private(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread]:
            """Retrieve private threads from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_privates(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel:
            """Retrieve a forum channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_forum(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel]:
            """Retrieve forum channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_forums(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def news(
            bot: hikari.GatewayBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel:
            """Retrieve a news channel from the cache. Raise an exception if not found."""
            if not (resolved_channel := await _cache_news(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel]:
            """Retrieve news channels from the cache. Raise an exception if not found."""
            if not (resolved_channels := await _cache_newses(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role:
            """Retrieve a role from the cache. Raise an exception if not found."""
            if not (resolved_role := await _cache_role(bot, guild, role)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role]:
            """Retrieve roles belonging to a member or a guild from the cache. Raise an exception if not found."""
            if not (resolved_roles := await _cache_roles(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_roles

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role:
            """Retrieve the top role of a member or guild from the cache. Raise an exception if not found."""
            if not (resolved_role := await _cache_top_role(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role:
            """Retrieve the booster role of a guild from the cache. Raise an exception if not found."""
            if not (resolved_role := await _cache_booster_role(bot, guild)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot,
            emoji: int | str | hikari.Emoji | None,
        ) -> hikari.Emoji:
            """Retrieve an emoji from the cache. Raise an exception if not found."""
            if not (resolved_emoji := await _cache_emoji(bot, emoji)):
                raise MandatoryEmojiNotFound

            return resolved_emoji

    class Rest:
        """Retrieve an object by fetching it from Discord. Raise an exception if not found."""

        @staticmethod
        async def guild(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.RESTGuild:
            """Retrieve a guild by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_guild := await _rest_guild(bot, guild)):
                raise MandatoryGuildNotFound

            return resolved_guild

        @staticmethod
        async def banned(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.GuildBan:
            """Retrieve a ban by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_ban := await _rest_banned(bot, guild, user)):
                raise MandatoryBanNotFound

            return resolved_ban

        @staticmethod
        async def user(
            bot: hikari.GatewayBot | hikari.RESTBot,
            user: int | hikari.User | None,
        ) -> hikari.User:
            """Retrieve a user by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_user := await _rest_user(bot, user)):
                raise MandatoryUserNotFound

            return resolved_user

        @staticmethod
        async def member(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            user: int | hikari.User | None,
        ) -> hikari.Member:
            """Retrieve a member by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_member := await _rest_member(bot, guild, user)):
                raise MandatoryMemberNotFound

            return resolved_member

        @staticmethod
        async def members(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve members by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_members := await _rest_members(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def boosters(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Member]:
            """Retrieve boosters by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_members := await _rest_boosters(bot, guild)):
                raise MandatoryMemberNotFound

            return resolved_members

        @staticmethod
        async def channel(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildChannel:
            """Retrieve a channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_channel(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def channels(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel]:
            """Retrieve channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_channels(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def dms(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.PrivateChannel | None,
        ) -> hikari.PrivateChannel:
            """Retrieve a private channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_dms(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def dm(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.DMChannel | None,
        ) -> hikari.DMChannel:
            """Retrieve a DM channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_dm(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def group(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GroupDMChannel | None,
        ) -> hikari.GroupDMChannel:
            """Retrieve a group DM channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_group(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def textable(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.TextableGuildChannel:
            """Retrieve a textable channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_textable(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def textables(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel]:
            """Retrieve textable channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_textables(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def permissible(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.PermissibleGuildChannel:
            """Retrieve a permissible channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_permissible(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def permissibles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel]:
            """Retrieve permissible channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_permissibles(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def category(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildCategory:
            """Retrieve a category channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_category(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def categories(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory]:
            """Retrieve category channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_categories(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def voice(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildVoiceChannel:
            """Retrieve a voice channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_voice(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def voices(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel]:
            """Retrieve voice channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_voices(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def stage(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildStageChannel:
            """Retrieve a stage channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_stage(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def stages(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel]:
            """Retrieve stage channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_stages(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def text(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildTextChannel:
            """Retrieve a text channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_text(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def texts(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel]:
            """Retrieve text channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_texts(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def thread(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildThreadChannel:
            """Retrieve a thread channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_thread(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def threads(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel]:
            """Retrieve thread channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_threads(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def public(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPublicThread | hikari.GuildNewsThread:
            """Retrieve a public thread or news thread by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_public(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def publics(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread]:
            """Retrieve public/news threads by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_publics(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def private(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildPrivateThread:
            """Retrieve a private thread by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_private(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def privates(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread]:
            """Retrieve private threads by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_privates(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def forum(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildForumChannel:
            """Retrieve a forum channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_forum(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def forums(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel]:
            """Retrieve forum channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_forums(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def news(
            bot: hikari.GatewayBot | hikari.RESTBot,
            channel: int | hikari.GuildChannel | None,
        ) -> hikari.GuildNewsChannel:
            """Retrieve a news channel by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_channel := await _rest_news(bot, channel)):
                raise MandatoryChannelNotFound

            return resolved_channel

        @staticmethod
        async def newses(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel]:
            """Retrieve news channels by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_channels := await _rest_newses(bot, guild)):
                raise MandatoryChannelNotFound

            return resolved_channels

        @staticmethod
        async def role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            role: int | hikari.Role | None,
        ) -> hikari.Role:
            """Retrieve a role by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_role := await _rest_role(bot, guild, role)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def roles(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> typing.Mapping[hikari.Snowflake, hikari.Role]:
            """Retrieve roles belonging to a member or a guild by fetching them from Discord. Raise an exception if not found."""
            if not (resolved_roles := await _rest_roles(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_roles

        @staticmethod
        async def top_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
            member: int | hikari.Member | None,
        ) -> hikari.Role:
            """Retrieve the top role of a member or guild by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_role := await _rest_top_role(bot, guild, member)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def booster_role(
            bot: hikari.GatewayBot | hikari.RESTBot,
            guild: int | hikari.Guild | None,
        ) -> hikari.Role:
            """Retrieve the booster role of a guild by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_role := await _rest_booster_role(bot, guild)):
                raise MandatoryRoleNotFound

            return resolved_role

        @staticmethod
        async def emoji(
            bot: hikari.GatewayBot | hikari.RESTBot,
            emoji: int | str | hikari.Emoji | None,
            guild: int | hikari.Guild | None = None,
        ) -> hikari.Emoji:
            """Retrieve an emoji by fetching it from Discord. Raise an exception if not found."""
            if not (resolved_emoji := await _rest_emoji(bot, emoji, guild)):
                raise MandatoryEmojiNotFound

            return resolved_emoji


async def _either_guild(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> hikari.GatewayGuild | hikari.RESTGuild | None:
    if not guild:
        return None

    return (await _cache_guild(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_guild(bot, guild))


async def _cache_guild(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> hikari.GatewayGuild | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    return bot.cache.get_guild(guild)


async def _rest_guild(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> hikari.RESTGuild | None:
    if not guild:
        return None

    try:
        return await bot.rest.fetch_guild(guild)
    except hikari.NotFoundError:
        return None


async def _rest_banned(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    user: int | hikari.User | None,
) -> hikari.GuildBan | None:
    if not guild or not user:
        return None

    try:
        return await bot.rest.fetch_ban(guild, user)
    except hikari.NotFoundError:
        return None


async def _either_user(
    bot: hikari.GatewayBot | hikari.RESTBot,
    user: int | hikari.User | None,
) -> hikari.User | None:
    if not user:
        return None

    return (await _cache_user(bot, user) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_user(bot, user))


async def _cache_user(
    bot: hikari.GatewayBot,
    user: int | hikari.User | None,
) -> hikari.User | None:
    if not user:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    return bot.cache.get_user(user)


async def _rest_user(
    bot: hikari.GatewayBot | hikari.RESTBot,
    user: int | hikari.User | None,
) -> hikari.User | None:
    if not user:
        return None

    try:
        return await bot.rest.fetch_user(user)
    except hikari.NotFoundError:
        return None


async def _either_member(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    user: int | hikari.User | None,
) -> hikari.Member | None:
    if not guild or not user:
        return None

    return (await _cache_member(bot, guild, user) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_member(bot, guild, user))


async def _cache_member(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
    user: int | hikari.User | None,
) -> hikari.Member | None:
    if not guild or not user:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    return bot.cache.get_member(guild, user)


async def _rest_member(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    user: int | hikari.User | None,
) -> hikari.Member | None:
    if not guild or not user:
        return None

    try:
        return await bot.rest.fetch_member(guild, user)
    except hikari.NotFoundError:
        return None


async def _either_members(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    return (await _cache_members(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_members(bot, guild))


async def _cache_members(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    return bot.cache.get_members_view_for_guild(guild if isinstance(guild, int) else guild.id)


async def _rest_members(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    try:
        return {member.id: member async for member in bot.rest.fetch_members(guild)}
    except hikari.NotFoundError:
        return None


async def _either_boosters(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    return (await _cache_boosters(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_boosters(bot, guild))


async def _cache_boosters(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_members = await _cache_members(bot, guild)
    return {member.id: member for member in resolved_members.values() if member.premium_since} if resolved_members else None


async def _rest_boosters(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.Member] | None:
    if not guild:
        return None

    resolved_members = await _rest_members(bot, guild)
    return {member.id: member for member in resolved_members.values() if member.premium_since} if resolved_members else None


async def _either_channel(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildChannel | None:
    if not channel:
        return None

    return (await _cache_channel(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_channel(bot, channel))


async def _cache_channel(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = bot.cache.get_guild_channel(channel)
    return resolved_channel


async def _rest_channel(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildChannel | None:
    if not channel:
        return None

    try:
        resolved_channel = await bot.rest.fetch_channel(channel)

        if not isinstance(resolved_channel, hikari.GuildChannel):
            resolved_channel = None
    except hikari.NotFoundError:
        resolved_channel = None

    return resolved_channel


async def _either_channels(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
    if not guild:
        return None

    return (await _cache_channels(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_channels(bot, guild))


async def _cache_channels(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    return bot.cache.get_guild_channels_view_for_guild(guild)


async def _rest_channels(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildChannel] | None:
    if not guild:
        return None

    try:
        return {channel.id: channel for channel in await bot.rest.fetch_guild_channels(guild)}
    except hikari.NotFoundError:
        return None


async def _rest_dms(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.PrivateChannel | None,
) -> hikari.PrivateChannel | None:
    if not channel:
        return None

    try:
        resolved_channel = await bot.rest.fetch_channel(channel)

        if not isinstance(resolved_channel, hikari.PrivateChannel):
            resolved_channel = None
    except hikari.NotFoundError:
        resolved_channel = None

    return resolved_channel


async def _rest_dm(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.DMChannel | None,
) -> hikari.DMChannel | None:
    if not channel:
        return None

    resolved_dm = await _rest_dms(bot, channel)
    return resolved_dm if isinstance(resolved_dm, hikari.DMChannel) else None


async def _rest_group(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GroupDMChannel | None,
) -> hikari.GroupDMChannel | None:
    if not channel:
        return None

    resolved_group = await _rest_dms(bot, channel)
    return resolved_group if isinstance(resolved_group, hikari.GroupDMChannel) else None


async def _either_textable(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.TextableGuildChannel | None:
    if not channel:
        return None

    return (await _cache_textable(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_textable(bot, channel))


async def _cache_textable(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.TextableGuildChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.TextableGuildChannel) else None


async def _rest_textable(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.TextableGuildChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.TextableGuildChannel) else None


async def _either_textables(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
    if not guild:
        return None

    return (await _cache_textables(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_textables(bot, guild))


async def _cache_textables(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.TextableGuildChannel)} if resolved_channels else None


async def _rest_textables(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.TextableGuildChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.TextableGuildChannel)} if resolved_channels else None


async def _either_permissible(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.PermissibleGuildChannel | None:
    if not channel:
        return None

    return (await _cache_permissible(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_permissible(bot, channel))


async def _cache_permissible(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.PermissibleGuildChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.PermissibleGuildChannel) else None


async def _rest_permissible(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.PermissibleGuildChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.PermissibleGuildChannel) else None


async def _either_permissibles(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
    if not guild:
        return None

    return (await _cache_permissibles(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_permissibles(bot, guild))


async def _cache_permissibles(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.PermissibleGuildChannel)} if resolved_channels else None


async def _rest_permissibles(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.PermissibleGuildChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.PermissibleGuildChannel)} if resolved_channels else None


async def _either_category(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildCategory | None:
    if not channel:
        return None

    return (await _cache_category(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_category(bot, channel))


async def _cache_category(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildCategory | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildCategory) else None


async def _rest_category(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildCategory | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildCategory) else None


async def _either_categories(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
    if not guild:
        return None

    return (await _cache_categories(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_categories(bot, guild))


async def _cache_categories(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildCategory)} if resolved_channels else None


async def _rest_categories(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildCategory] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildCategory)} if resolved_channels else None


async def _either_voice(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildVoiceChannel | None:
    if not channel:
        return None

    return (await _cache_voice(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_voice(bot, channel))


async def _cache_voice(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildVoiceChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildVoiceChannel) else None


async def _rest_voice(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildVoiceChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildVoiceChannel) else None


async def _either_voices(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
    if not guild:
        return None

    return (await _cache_voices(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_voices(bot, guild))


async def _cache_voices(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildVoiceChannel)} if resolved_channels else None


async def _rest_voices(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildVoiceChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildVoiceChannel)} if resolved_channels else None


async def _either_stage(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildStageChannel | None:
    if not channel:
        return None

    return (await _cache_stage(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_stage(bot, channel))


async def _cache_stage(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildStageChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildStageChannel) else None


async def _rest_stage(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildStageChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildStageChannel) else None


async def _either_stages(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
    if not guild:
        return None

    return (await _cache_stages(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_stages(bot, guild))


async def _cache_stages(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildStageChannel)} if resolved_channels else None


async def _rest_stages(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildStageChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildStageChannel)} if resolved_channels else None


async def _either_text(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildTextChannel | None:
    if not channel:
        return None

    return (await _cache_text(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_text(bot, channel))


async def _cache_text(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildTextChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildTextChannel) else None


async def _rest_text(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildTextChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildTextChannel) else None


async def _either_texts(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
    if not guild:
        return None

    return (await _cache_texts(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_texts(bot, guild))


async def _cache_texts(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildTextChannel)} if resolved_channels else None


async def _rest_texts(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildTextChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildTextChannel)} if resolved_channels else None


async def _either_thread(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildThreadChannel | None:
    if not channel:
        return None

    return (await _cache_thread(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_thread(bot, channel))


async def _cache_thread(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildThreadChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildThreadChannel) else None


async def _rest_thread(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildThreadChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildThreadChannel) else None


async def _either_threads(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
    if not guild:
        return None

    return (await _cache_threads(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_threads(bot, guild))


async def _cache_threads(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildThreadChannel)} if resolved_channels else None


async def _rest_threads(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildThreadChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildThreadChannel)} if resolved_channels else None


async def _either_public(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
    if not channel:
        return None

    return (await _cache_public(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_public(bot, channel))


async def _cache_public(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, (hikari.GuildPublicThread, hikari.GuildNewsThread)) else None


async def _rest_public(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPublicThread | hikari.GuildNewsThread | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, (hikari.GuildPublicThread, hikari.GuildNewsThread)) else None


async def _either_publics(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
    if not guild:
        return None

    return (await _cache_publics(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_publics(bot, guild))


async def _cache_publics(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, (hikari.GuildPublicThread, hikari.GuildNewsThread))} if resolved_channels else None


async def _rest_publics(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPublicThread | hikari.GuildNewsThread] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, (hikari.GuildPublicThread, hikari.GuildNewsThread))} if resolved_channels else None


async def _either_private(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPrivateThread | None:
    if not channel:
        return None

    return (await _cache_private(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_private(bot, channel))


async def _cache_private(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPrivateThread | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildPrivateThread) else None


async def _rest_private(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildPrivateThread | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildPrivateThread) else None


async def _either_privates(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
    if not guild:
        return None

    return (await _cache_privates(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_privates(bot, guild))


async def _cache_privates(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildPrivateThread)} if resolved_channels else None


async def _rest_privates(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildPrivateThread] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildPrivateThread)} if resolved_channels else None


async def _either_forum(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildForumChannel | None:
    if not channel:
        return None

    return (await _cache_forum(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_forum(bot, channel))


async def _cache_forum(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildForumChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildForumChannel) else None


async def _rest_forum(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildForumChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildForumChannel) else None


async def _either_forums(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
    if not guild:
        return None

    return (await _cache_forums(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_forums(bot, guild))


async def _cache_forums(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildForumChannel)} if resolved_channels else None


async def _rest_forums(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildForumChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildForumChannel)} if resolved_channels else None


async def _either_news(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildNewsChannel | None:
    if not channel:
        return None

    return (await _cache_news(bot, channel) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_news(bot, channel))


async def _cache_news(
    bot: hikari.GatewayBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildNewsChannel | None:
    if not channel:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channel = await _cache_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildNewsChannel) else None


async def _rest_news(
    bot: hikari.GatewayBot | hikari.RESTBot,
    channel: int | hikari.GuildChannel | None,
) -> hikari.GuildNewsChannel | None:
    if not channel:
        return None

    resolved_channel = await _rest_channel(bot, channel)
    return resolved_channel if isinstance(resolved_channel, hikari.GuildNewsChannel) else None


async def _either_newses(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
    if not guild:
        return None

    return (await _cache_newses(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_newses(bot, guild))


async def _cache_newses(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_channels = await _cache_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildNewsChannel)} if resolved_channels else None


async def _rest_newses(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> typing.Mapping[hikari.Snowflake, hikari.GuildNewsChannel] | None:
    if not guild:
        return None

    resolved_channels = await _rest_channels(bot, guild)
    return {channel.id: channel for channel in resolved_channels.values() if isinstance(channel, hikari.GuildNewsChannel)} if resolved_channels else None


async def _either_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    role: int | hikari.Role | None,
) -> hikari.Role | None:
    if not guild or not role:
        return None

    return (await _cache_role(bot, guild, role) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_role(bot, guild, role))


async def _cache_role(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
    role: int | hikari.Role | None,
) -> hikari.Role | None:
    if not guild or not role:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_role = bot.cache.get_role(role)
    return resolved_role if isinstance(resolved_role, hikari.Role) else None


async def _rest_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    role: int | hikari.Role | None,
) -> hikari.Role | None:
    if not guild or not role:
        return None

    try:
        resolved_role = await bot.rest.fetch_role(guild, role)
        return resolved_role if isinstance(resolved_role, hikari.Role) else None
    except hikari.NotFoundError:
        return None


async def _either_roles(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None = None,
) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
    if not guild:
        return None

    return (await _cache_roles(bot, guild, member) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_roles(bot, guild, member))


async def _cache_roles(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None = None,
) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
    if not guild and not member:
        return None
    elif not guild:
        guild = await _cache_guild(bot, member.guild_id if isinstance(member, hikari.Member) else member)

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    guild_roles = await _cache_roles(bot, guild)

    if not member:
        return guild_roles
    else:
        resolved_member = await _cache_member(bot, guild, member)
        return {role.id: role for role in guild_roles.values() if role.id in resolved_member.role_ids} if guild_roles and resolved_member else None


async def _rest_roles(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None = None,
) -> typing.Mapping[hikari.Snowflake, hikari.Role] | None:
    if not guild and not member:
        return None
    elif not guild:
        guild = await _rest_guild(bot, member.guild_id if isinstance(member, hikari.Member) else member)

    try:
        guild_roles = await _rest_roles(bot, guild)

        if not member:
            resolved_roles = guild_roles
        else:
            resolved_member = await _rest_member(bot, guild, member)
            resolved_roles = {role.id: role for role in guild_roles.values() if role.id in resolved_member.role_ids} if guild_roles and resolved_member else None

        return resolved_roles
    except hikari.NotFoundError:
        return None


async def _either_top_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None,
) -> hikari.Role | None:
    if not guild or not member:
        return None

    return (await _cache_top_role(bot, guild, member) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_top_role(bot, guild, member))


async def _cache_top_role(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None,
) -> hikari.Role | None:
    if not guild and not member:
        return None
    elif not guild:
        guild = await _cache_guild(bot, member.guild_id if isinstance(member, hikari.Member) else member)

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    guild_roles = await _cache_roles(bot, guild)
    sorted_roles = sorted(guild_roles.values(), key=lambda role: role.position, reverse=True) if guild_roles else []

    if not member:
        top_role = sorted_roles[0] if sorted_roles else None
    else:
        resolved_member = await _cache_member(bot, guild, member)
        top_role = next((role for role in sorted_roles if role.id in resolved_member.role_ids), None) if resolved_member else None

    return top_role


async def _rest_top_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
    member: int | hikari.Member | None,
) -> hikari.Role | None:
    if not guild and not member:
        return None
    elif not guild:
        guild = await _rest_guild(bot, member.guild_id if isinstance(member, hikari.Member) else member)

    try:
        guild_roles = await _rest_roles(bot, guild)
        sorted_roles = sorted(guild_roles.values(), key=lambda role: role.position, reverse=True) if guild_roles else []

        if not member:
            top_role = sorted_roles[0] if sorted_roles else None
        else:
            resolved_member = await _rest_member(bot, guild, member)
            top_role = next((role for role in sorted_roles if role.id in resolved_member.role_ids), None) if resolved_member else None

        return top_role
    except hikari.NotFoundError:
        return None


async def _either_booster_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> hikari.Role | None:
    if not guild:
        return None

    return (await _cache_booster_role(bot, guild) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_booster_role(bot, guild))


async def _cache_booster_role(
    bot: hikari.GatewayBot,
    guild: int | hikari.Guild | None,
) -> hikari.Role | None:
    if not guild:
        return None

    if not isinstance(bot, hikari.GatewayBot):
        raise InvalidBot

    resolved_roles = await _cache_roles(bot, guild)
    return next((role for role in resolved_roles.values() if role.is_premium_subscriber_role), None) if resolved_roles else None


async def _rest_booster_role(
    bot: hikari.GatewayBot | hikari.RESTBot,
    guild: int | hikari.Guild | None,
) -> hikari.Role | None:
    if not guild:
        return None

    try:
        resolved_roles = await _rest_roles(bot, guild)
        return next((role for role in resolved_roles.values() if role.is_premium_subscriber_role), None) if resolved_roles else None
    except hikari.NotFoundError:
        return None


async def _either_emoji(
    bot: hikari.GatewayBot | hikari.RESTBot,
    emoji: int | str | hikari.Emoji | None,
    guild: int | hikari.Guild | None = None,
) -> hikari.Emoji | None:
    if not emoji:
        return None

    return (await _cache_emoji(bot, emoji) if isinstance(bot, hikari.GatewayBot) else None) or (await _rest_emoji(bot, emoji, guild))


async def _cache_emoji(
    bot: hikari.GatewayBot,
    emoji: int | str | hikari.Emoji | None,
) -> hikari.Emoji | None:
    resolved_emoji = None

    if isinstance(emoji, hikari.CustomEmoji):
        resolved_emoji = bot.cache.get_emoji(emoji)
    elif isinstance(emoji, hikari.UnicodeEmoji):
        resolved_emoji = hikari.UnicodeEmoji.parse(emoji.name)
    elif isinstance(emoji, str):
        if emoji in emojis.EMOJI_DATA:
            resolved_emoji = hikari.UnicodeEmoji.parse(emoji)
        else:
            try:
                resolved_emoji = hikari.CustomEmoji.parse(emoji)
            except ValueError:
                resolved_emoji = None
    elif isinstance(emoji, int):
        try:
            if (unicode_char := chr(emoji)) in emojis.EMOJI_DATA:
                resolved_emoji = hikari.UnicodeEmoji.parse(unicode_char)
        except ValueError:
            resolved_emoji = None

    return resolved_emoji


async def _rest_emoji(
    bot: hikari.GatewayBot | hikari.RESTBot,
    emoji: int | str | hikari.Emoji | None,
    guild: int | hikari.Guild | None = None,
) -> hikari.Emoji | None:
    resolved_emoji = None

    if isinstance(emoji, hikari.CustomEmoji):
        try:
            resolved_emoji = (await bot.rest.fetch_emoji(guild, emoji)) if guild else None
        except hikari.NotFoundError:
            resolved_emoji = None
    elif isinstance(emoji, hikari.UnicodeEmoji):
        resolved_emoji = hikari.UnicodeEmoji.parse(emoji.name)
    elif isinstance(emoji, str):
        if emoji in emojis.EMOJI_DATA:
            resolved_emoji = hikari.UnicodeEmoji.parse(emoji)
        else:
            try:
                resolved_emoji = hikari.CustomEmoji.parse(emoji)
                resolved_emoji = (await bot.rest.fetch_emoji(guild, resolved_emoji)) if guild else None
            except (ValueError, hikari.NotFoundError):
                resolved_emoji = None
    elif isinstance(emoji, int):
        try:
            if (unicode_char := chr(emoji)) in emojis.EMOJI_DATA:
                resolved_emoji = hikari.UnicodeEmoji.parse(unicode_char)
        except ValueError:
            resolved_emoji = None

    return resolved_emoji

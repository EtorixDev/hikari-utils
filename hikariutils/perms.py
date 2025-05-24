import hikari

from hikariutils.getfetch import Mandatory


async def is_above(
    bot: hikari.GatewayBot,
    first: hikari.Member | hikari.Role,
    second: hikari.Member | hikari.Role,
) -> bool:
    """Check if the first member is above the second member in the hierarchy."""
    first_role = await Mandatory.Either.role(bot, first.guild_id, first.id) if isinstance(first, hikari.Role) else await Mandatory.Either.top_role(bot, first.guild_id, first.id)
    second_role = await Mandatory.Either.role(bot, second.guild_id, second.id) if isinstance(second, hikari.Role) else await Mandatory.Either.top_role(bot, second.guild_id, second.id)
    return first_role.position > second_role.position


async def resolve_perms(
    bot: hikari.GatewayBot,
    member: hikari.Member,
    channel: hikari.GuildChannel | None = None,
) -> hikari.Permissions:
    """Resolve the permissions for a member in a guild."""
    base_role = await Mandatory.Either.role(bot, member.guild_id, member.guild_id)
    member_roles = await Mandatory.Either.roles(bot, member.guild_id, member.id)
    permissions = base_role.permissions

    for role in member_roles.values():
        permissions |= role.permissions

    if permissions & hikari.Permissions.ADMINISTRATOR:
        return hikari.Permissions.all_permissions()

    channel = await Mandatory.Either.permissible(bot, channel.parent_id if isinstance(channel, hikari.GuildThreadChannel) else channel.id) if channel else None

    if not channel:
        return permissions

    channel_overwrites = channel.permission_overwrites
    everyone_overwrite = channel_overwrites.get(member.guild_id)
    role_overwrites = everyone_overwrite if everyone_overwrite else hikari.PermissionOverwrite(id=member.guild_id, type=hikari.PermissionOverwriteType.ROLE)

    for role in member_roles.values():
        if role_overwrite := channel_overwrites.get(role.id):
            role_overwrites.deny |= role_overwrite.deny
            role_overwrites.allow |= role_overwrite.allow

    permissions &= ~role_overwrites.deny
    permissions |= role_overwrites.allow

    if member_overwrite := channel_overwrites.get(member.id):
        permissions &= ~member_overwrite.deny
        permissions |= member_overwrite.allow

    return permissions


async def can_timeout(
    bot: hikari.GatewayBot,
    moderator: hikari.Member,
    target: hikari.Member,
) -> bool:
    """Check if a member can timeout another member."""
    guild = await Mandatory.Either.guild(bot, moderator.guild_id)

    moderator_perms = await resolve_perms(bot, moderator)
    target_perms = await resolve_perms(bot, target)

    moderator_is_admin = bool(moderator_perms & hikari.Permissions.ADMINISTRATOR)
    target_is_admin = bool(target_perms & hikari.Permissions.ADMINISTRATOR)

    moderator_is_owner = moderator.id == guild.owner_id
    target_is_owner = target.id == guild.owner_id

    if not (target_is_owner or target_is_admin) and (moderator_perms & hikari.Permissions.MODERATE_MEMBERS or moderator_is_admin or moderator_is_owner) and await is_above(bot, moderator, target):
        return True

    return False


async def can_kick(
    bot: hikari.GatewayBot,
    moderator: hikari.Member,
    target: hikari.Member,
) -> bool:
    """Check if a member can kick another member."""
    guild = await Mandatory.Either.guild(bot, moderator.guild_id)

    moderator_perms = await resolve_perms(bot, moderator)
    moderator_is_admin = bool(moderator_perms & hikari.Permissions.ADMINISTRATOR)

    moderator_is_owner = moderator.id == guild.owner_id
    target_is_owner = target.id == guild.owner_id

    if moderator.id == target.id:
        return False
    elif moderator_is_owner:
        return True
    elif moderator_is_admin or moderator_perms & hikari.Permissions.KICK_MEMBERS:
        if target_is_owner:
            return False

        return await is_above(bot, moderator, target)

    return False


async def can_ban(
    bot: hikari.GatewayBot,
    moderator: hikari.Member,
    target: hikari.Member,
) -> bool:
    """Check if a member can ban another member."""
    guild = await Mandatory.Either.guild(bot, moderator.guild_id)

    moderator_perms = await resolve_perms(bot, moderator)
    moderator_is_admin = bool(moderator_perms & hikari.Permissions.ADMINISTRATOR)

    moderator_is_owner = moderator.id == guild.owner_id
    target_is_owner = target.id == guild.owner_id

    if moderator.id == target.id:
        return False
    elif moderator_is_owner:
        return True
    elif moderator_is_admin or moderator_perms & hikari.Permissions.BAN_MEMBERS:
        if target_is_owner:
            return False

        return await is_above(bot, moderator, target)

    return False

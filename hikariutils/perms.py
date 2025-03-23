import hikari

from hikariutils.getfetch import Mandatory


async def is_above(bot: hikari.GatewayBot, first: hikari.Member, second: hikari.Member) -> bool:
    """Check if the first member is above the second member in the hierarchy."""
    first_top_role = await Mandatory.top_role(bot, first.guild_id, first.id)
    second_top_role = await Mandatory.top_role(bot, second.guild_id, second.id)
    return first_top_role.position > second_top_role.position


async def resolve_perms(bot: hikari.GatewayBot, member: hikari.Member, channel: hikari.GuildChannel | None = None) -> hikari.Permissions:
    """Resolve the permissions for a member in a guild."""
    base_role = await Mandatory.role(bot, member.guild_id, member.guild_id)
    member_roles = member.get_roles() or await member.fetch_roles()
    permissions = base_role.permissions

    for role in member_roles:
        permissions |= role.permissions

    if permissions & hikari.Permissions.ADMINISTRATOR:
        return hikari.Permissions.all_permissions()

    if not isinstance(channel, hikari.PermissibleGuildChannel):
        return permissions

    channel_overwrites = channel.permission_overwrites
    everyone_overwrite = channel_overwrites.get(member.guild_id)
    role_overwrites = everyone_overwrite if everyone_overwrite else hikari.PermissionOverwrite(id=member.guild_id, type=hikari.PermissionOverwriteType.ROLE)

    for role in member_roles:
        if role_overwrite := channel_overwrites.get(role.id):
            role_overwrites.deny |= role_overwrite.deny
            role_overwrites.allow |= role_overwrite.allow

    permissions &= ~role_overwrites.deny
    permissions |= role_overwrites.allow

    if member_overwrite := channel_overwrites.get(member.id):
        permissions &= ~member_overwrite.deny
        permissions |= member_overwrite.allow

    return permissions


async def can_moderate(bot: hikari.GatewayBot, moderator: hikari.Member, target: hikari.Member, mod_perms: hikari.Permissions) -> bool:
    """Check if a member can moderate another member."""
    guild = await Mandatory.guild(bot, moderator.guild_id)

    if not is_above(bot, moderator, target) or target.id == guild.owner_id:
        return False

    moderator_perms = await resolve_perms(bot, moderator)

    if moderator_perms & hikari.Permissions.ADMINISTRATOR:
        return True

    return bool(moderator_perms & mod_perms)

class HikariUtilsError(Exception):
    """Base class for hikari-utils exceptions."""


class MandatoryGuildNotFound(HikariUtilsError):
    """Exception raised when a guild is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryMemberNotFound(HikariUtilsError):
    """Exception raised when a member is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryUserNotFound(HikariUtilsError):
    """Exception raised when a user is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryChannelNotFound(HikariUtilsError):
    """Exception raised when a channel is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryRoleNotFound(HikariUtilsError):
    """Exception raised when a role is needed but couldn't be found in the cache or fetched from Discord."""

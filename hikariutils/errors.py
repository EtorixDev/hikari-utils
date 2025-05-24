class HikariUtilsError(Exception):
    """Base class for hikari-utils exceptions."""


class InvalidBot(HikariUtilsError):
    """Exception raised when an incompatible bot type was passed to a method."""


class MandatoryGuildNotFound(HikariUtilsError):
    """Exception raised when a guild is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryBanNotFound(HikariUtilsError):
    """Exception raised when a ban is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryMemberNotFound(HikariUtilsError):
    """Exception raised when a member is needed but couldn't be fetched from Discord."""


class MandatoryUserNotFound(HikariUtilsError):
    """Exception raised when a user is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryChannelNotFound(HikariUtilsError):
    """Exception raised when a channel is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryRoleNotFound(HikariUtilsError):
    """Exception raised when a role is needed but couldn't be found in the cache or fetched from Discord."""


class MandatoryEmojiNotFound(HikariUtilsError):
    """Exception raised when an emoji is needed but couldn't be found in the cache or fetched from Discord."""

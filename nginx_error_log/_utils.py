"""Various utilities."""
import datetime
import enum
import logging
import re

# Format:
# YYYY/MM/DD HH:MM:SS [LEVEL] PID#TID: *CID MESSAGE
# See https://stackoverflow.com/a/26125951
LOG_REGEX = re.compile(
    r"^(?P<date_string>[\d/: ]{19}) "
    r"\[(?P<level>[a-z]+)\] "
    r"(?P<pid>\d+)#(?P<tid>\d+): "
    r"(\*(?P<cid>\d+) )?"
    r"(?P<message>.*)",
    re.DOTALL,
)
DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S"


class ParseError(Exception):
    pass


class Level(enum.IntEnum):
    DEBUG = logging.DEBUG  # 10
    INFO = logging.INFO  # 20
    NOTICE = 25
    WARNING = logging.WARNING  # 30
    ERROR = logging.ERROR  # 40
    CRITICAL = logging.CRITICAL  # 50
    ALERT = 60
    EMERGENCY = 70


level_mapping = {
    "debug": Level.DEBUG,
    "info": Level.INFO,
    "notice": Level.NOTICE,
    "warn": Level.WARNING,
    "error": Level.ERROR,
    "crit": Level.CRITICAL,
    "alert": Level.ALERT,
    "emerg": Level.EMERGENCY,
}


def parse_level(data: str) -> Level:
    if data not in level_mapping:
        raise ParseError("Could not parse level {!r}.".format(data))
    return level_mapping[data]


def parse_timestamp(date_string: str) -> datetime.datetime:
    try:
        return datetime.datetime.strptime(date_string, DATETIME_FORMAT)
    except ValueError as e:
        raise ParseError(
            "Could not parse {!r} to a datetime.".format(date_string)
        ) from e

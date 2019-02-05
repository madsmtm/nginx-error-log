"""Nginx error log parser."""

from ._utils import ParseError, Level, parse_level, parse_timestamp
from ._parser import LogEntry


parse_line = LogEntry.parse_line

__version__ = "0.1.0"
__all__ = (
    "ParseError",
    "Level",
    "LogEntry",
    "parse_line",
)

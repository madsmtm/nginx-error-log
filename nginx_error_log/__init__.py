"""Nginx error log parser."""

from ._utils import ParseError, Level, parse_level, parse_timestamp
from ._parser import LogEntry
from ._helpers import parse_lines, parse_lines_merge_multiple


parse_line = LogEntry.parse_line

__version__ = "0.1.1"
__all__ = (
    "ParseError",
    "Level",
    "LogEntry",
    "parse_line",
    "parse_lines",
    "parse_lines_merge_multiple",
)

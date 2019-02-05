"""Parser helpers."""
from typing import Iterable

from ._utils import ParseError
from ._parser import LogEntry


def parse_lines(lines: Iterable[str]) -> Iterable[LogEntry]:
    """Parse an iterable of error_log lines.

    Raises:
        `ParseError` if a line could not be parsed.
    """
    for line in lines:
        yield LogEntry.parse_line(line)


def parse_lines_merge_multiple(lines: Iterable[str]) -> Iterable[LogEntry]:
    """Parse an iterable of error_log debug lines.

    If one of the logs are split over multiple lines, this will attempt to merge
    these into a single `LogEntry`. Only use this on `debug` level log files!

    Raises:
        `ParseError` if the first line could not be parsed.
    """
    prev = None
    for line in lines:
        try:
            current = LogEntry.parse_line(line)
        except ParseError:
            if not prev:
                raise
            object.__setattr__(prev, "message", prev.message + "\n" + line.strip())
            continue
        if prev:
            yield prev
        prev = current
    if prev:
        yield prev

"""Log entry parser."""
import dataclasses
import datetime

from typing import Optional, Type, TypeVar

from ._utils import ParseError, Level, parse_level, parse_timestamp, LOG_REGEX


T = TypeVar("T", bound="LogEntry")


@dataclasses.dataclass(frozen=True)
class LogEntry:
    timestamp: datetime.datetime
    level: Level
    message: str
    pid: int
    tid: int
    cid: Optional[int]

    @classmethod
    def parse_line(cls: Type[T], line: str) -> T:
        """Parse a single error_log line.

        Raises:
            `ParseError` if the line could not be parsed.
        """
        m = LOG_REGEX.match(line)
        if not m:
            raise ParseError("Could not parse {!r}.".format(line))
        return cls(
            timestamp=parse_timestamp(m.group("date_string")),
            level=parse_level(m.group("level")),
            message=m.group("message").strip(),
            pid=int(m.group("pid")),
            tid=int(m.group("tid")),
            cid=int(m.group("cid")) if m.group("cid") is not None else None,
        )

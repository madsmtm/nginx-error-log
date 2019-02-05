from nginx_error_log import parse_line, LogEntry, Level, ParseError
from pytest import mark
from datetime import datetime


def test_parse_line():
    entry = parse_line("2019/01/23 12:34:56 [info] 1234#5678: Some data")
    assert entry == LogEntry(
        timestamp=datetime(2019, 1, 23, 12, 34, 56),
        level=Level.INFO,
        message="Some data",
        pid=1234,
        tid=5678,
        cid=None,
    )


def test_parse_line_with_cid():
    entry = parse_line("2019/01/23 12:34:56 [info] 1234#5678: *90 Some data")
    assert entry.cid == 90


def test_parse_line_removes_message_whitespace():
    entry = parse_line("2019/01/23 12:34:56 [info] 1234#5678:   Some data \n")
    assert entry.message == "Some data"


@mark.raises(exception=ParseError)
@mark.parametrize(
    "line",
    [
        "invalid",
        "2019/01/23 112:34:56 [info] 1234#5678: Some data",
        "2019/01/23 12:34:56  [info] 1234#5678: Some data",
        "2019:01:23 12/34/56 [info] 1234#5678: Some data",
        "2019/01/23 12:34:56 [invalid] 1234#5678: Some data",
        "2019/01/23 12:34:56 [info] #5678: Some data",
        "2019/01/23 12:34:56 [info] 1234#: Some data",
        "2019:01:23 12/34/56 [info]: Some data",
    ],
)
def test_parse_line_invalid(line):
    parse_line(line)

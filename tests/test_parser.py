from nginx_error_log import parse_line, ParseError
from pytest import mark


def test_parse_line(line, entry):
    assert parse_line(line) == entry


def test_parse_line_without_cid():
    entry = parse_line("2019/01/23 12:34:56 [info] 1234#5678: Some data")
    assert entry.cid == None
    assert entry.message == "Some data"


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

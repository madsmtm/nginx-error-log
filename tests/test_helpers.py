from nginx_error_log import parse_lines, parse_lines_merge_multiple, ParseError
from pytest import mark, raises


def test_parse_lines(line, entry):
    entry1, entry2 = parse_lines((line, line))
    assert entry1 == entry2 == entry


def test_parse_lines_invalid(line, entry):
    entries = parse_lines((line, "invalid"))
    assert next(entries) == entry
    with raises(ParseError):
        next(entries)


def test_parse_lines_merge_multiple(line, entry):
    entry1, entry2 = parse_lines_merge_multiple((line, line))
    assert entry1 == entry2 == entry


def test_parse_lines_merge_multiple_split_lines(line, entry):
    lines = (
        line,
        "2019/01/23 12:34:56 [debug] 1234#5678: *90 http proxy header:",
        '"GET /example HTTP/1.1',
        "Host: example.com",
        "Connection: close",
        "",
        '"',
        line,
    )
    entries = parse_lines_merge_multiple(lines)
    assert next(entries) == entry
    assert next(entries).message == (
        "http proxy header:\n"
        '"GET /example HTTP/1.1\n'
        "Host: example.com\n"
        'Connection: close\n\n"'
    )
    assert next(entries) == entry

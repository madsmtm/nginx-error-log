from datetime import datetime
from nginx_error_log import ParseError, Level, parse_level, parse_timestamp
from pytest import mark


def test_parse_level():
    assert parse_level("debug") == Level.DEBUG
    assert parse_level("emerg") == Level.EMERGENCY


@mark.raises(exception=ParseError)
def test_parse_level_invalid():
    parse_level("invalid")


def test_parse_timestamp():
    assert parse_timestamp("2018/1/15 5:43:21") == datetime(2018, 1, 15, 5, 43, 21)
    assert parse_timestamp("2019/01/23 12:34:56") == datetime(2019, 1, 23, 12, 34, 56)


@mark.raises(exception=ParseError)
def test_parse_timestamp_invalid():
    parse_timestamp("2019/13/23 12:34:56")

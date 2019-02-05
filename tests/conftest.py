from datetime import datetime
from nginx_error_log import Level, LogEntry
from pytest import fixture


@fixture
def line():
    return "2019/01/23 12:34:56 [info] 1234#5678: *90 Some data"


@fixture
def entry():
    return LogEntry(
        timestamp=datetime(2019, 1, 23, 12, 34, 56),
        level=Level.INFO,
        message="Some data",
        pid=1234,
        tid=5678,
        cid=90,
    )

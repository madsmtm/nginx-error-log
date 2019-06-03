from nginx_error_log import parse_lines, parse_lines_merge_multiple


def _run_sample_test(filename):
    with open(filename, "r") as f:
        for log in parse_lines(f):
            print(log.message)


def test_samples():
    _run_sample_test("tests/output-samples/error.log")
    _run_sample_test("tests/output-samples/warn.log")
    _run_sample_test("tests/output-samples/info.log")
    _run_sample_test("tests/output-samples/notice.log")

    with open("tests/output-samples/debug.log", "r") as f:
        for log in parse_lines_merge_multiple(f):
            print(log.message)

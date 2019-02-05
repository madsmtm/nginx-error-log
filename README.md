# nginx-error-log
Nginx error log parser.

[![Build Status](https://travis-ci.com/madsmtm/nginx-error-log.svg)](https://travis-ci.com/madsmtm/nginx-error-log)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This project provides a clean parsing of nginx error logs, produced by the
[`error_log`](https://nginx.org/en/docs/ngx_core_module.html#error_log) directive (not
access logs). The implementation is based on
[this](https://stackoverflow.com/a/26125951) stackoverflow answer.

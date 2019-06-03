# nginx-error-log
Nginx error log parser.

[![License](https://img.shields.io/pypi/l/nginx-error-log.svg)](https://github.com/madsmtm/nginx-error-log/blob/master/LICENSE.txt)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/nginx-error-log.svg)
![Implementations](https://img.shields.io/pypi/implementation/nginx-error-log.svg)
![Project Status](https://img.shields.io/pypi/status/nginx-error-log.svg)
[![Version](https://img.shields.io/pypi/v/nginx-error-log.svg)](https://pypi.org/project/nginx-error-log/)
[![Build Status](https://travis-ci.com/madsmtm/nginx-error-log.svg)](https://travis-ci.com/madsmtm/nginx-error-log)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This project provides a clean parsing of nginx error logs, produced by the
[`error_log`](https://nginx.org/en/docs/ngx_core_module.html#error_log) directive (not
access logs). The implementation is based on
[this](https://stackoverflow.com/a/26125951) stackoverflow answer.


## Installation
```sh
pip install nginx-error-log
```


## License
MIT, see `LICENSE.txt`.

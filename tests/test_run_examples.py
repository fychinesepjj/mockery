#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings

if __name__ == "__main__":
    loadSettings('examples.settings')
    from mockery import management
    tests = [
        (('test.py', 'run', 'examples'), 'run success')
    ]

    for test in tests:
        param, info = test
        print('\nExpect result:' + info)
        management.execute_from_command_line(param)
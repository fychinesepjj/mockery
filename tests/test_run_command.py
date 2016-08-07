#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings


if __name__ == "__main__":
    loadSettings('examples.settings')
    from mocker import management
    tests = [
        (('test.py',), 'help'), # help
        (('test.py', 'help'), 'help'), # help
        (('test.py', 'run'), 'help'), # help
        (('test.py', 'run', 'examples'), 'run success'), # auto load examples.cases
        (('test.py', 'run', 'examples/case.py'), 'load error'), # load error
        (('test.py', 'run', 'examples/cases.py'), 'run success'), # explicit load examples.cases
        (('test.py', 'create'), 'help') # help
    
    for test in tests:
        param, info = test
        print('Expect result: ----------------------------------->' + info)
        management.execute_from_command_line(param)
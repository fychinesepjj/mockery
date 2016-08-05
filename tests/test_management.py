#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings


if __name__ == "__main__":
    loadSettings('examples.settings')
    from mocker import management
    tests = [
        ('test.py',), # help
        ('test.py', 'help'), # help
        ('test.py', 'run'), # help
        ('test.py', 'run', 'examples/case.py'), # loadmodule error
        ('test.py', 'create'), # help
        ('test.py', 'create', 'examples')] # ('create', 'projectName')
    
    for test in tests:
        management.execute_from_command_line(test)
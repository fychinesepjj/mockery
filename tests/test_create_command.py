#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings


if __name__ == "__main__":
    loadSettings('settings')
    from mocker import management
    param = ('test.py', 'create', 'createdProject')
    management.execute_from_command_line(param)
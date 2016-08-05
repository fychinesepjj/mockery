#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

try:
    import sys
    sys.path.append('./mocker')
except:
    pass
'''
from core.request import Request
os.environ.setdefault("MOCKER_SETTINGS_MODULE", "tests.settings")


class Test(object):
    def __init__(self, parent):
        self.parent = parent
    
    def get(self, func):
        def wrapper(*args, **kw):
            print('-->wrapped ' + self.parent)
            return func(*args, **kw)
        return wrapper

a = Test('A')
b = Test('B')

@a.get
def hello(name):
    print(name)

@b.get
def hello2(name):
    print(name)
'''  

class ManagementUtility(object):
    
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.cmd = self.argv[1] if len(self.argv) >= 2 else None
        self.param = self.argv[2] if len(self.argv) >= 3 else None
        self.prog_name = os.path.basename(self.argv[0])

    def help(self, *argv):
        usage = 'mocker usage:\n1. %(cmd)s help\n2. %(cmd)s run caseFile\n3. %(cmd)s create projectName\n' % {'cmd': self.prog_name}
        print(usage)
        
    def run(self, value):
        print('run', value)
    
    def create(self, value):
        print('create', value)
    
    def getCommand(self):
        if len(self.argv[1:]) <= 1:
            return self.help
        else:
            if hasattr(self, self.cmd):
                return getattr(self, self.cmd)
            else:
                self.help

    def execute(self):
        print('execute')
        print(self.argv)
        self.getCommand()(self.param)

if __name__ == '__main__':
    ManagementUtility().execute()
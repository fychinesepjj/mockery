#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

try:
    import sys
    sys.path.append('./core')
except:
    pass

from core.request import Request
os.environ.setdefault("MOCKER_SETTINGS_MODULE", "projectTest.settings")

'''
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

if __name__ == '__main__':
    req = Request()
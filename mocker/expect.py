#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

import functools
from mocker.utils import matchDict, isNumber, Console

# 检查Expect是否Pass
def validate(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            this, isValid = func(*args, **kw)
            action = '.' + this.action if this.action else ''
            if isValid:
                msg = '#%s Expect%s.%s  Pass' % (this.rank, action, func.__name__)
                Console.success(msg.rjust(8, '>'))
            else:
                msg = '#%s Expect%s.%s  Fail' % (this.rank, action, func.__name__)
                Console.error(msg.rjust(8, '>'))
            return isValid
        except Exception as e:
            Console.error('@validate Exception:' + str(e))
    return wrapper
    
'''
from mocker.expect import Expect
from mocker.response import Response
import requests
t=requests.get('http://192.168.95.1:8080/json/baidu.json')
res = Response(t)
ept = Expect(res)
ept.code.eq(200)
'''
class Expect(object):
    action = ''
    rank = 0
    
    def __init__(self, obj=None, counter=True):
        if not obj:
            raise Exception('Expect initialize: only accept non-null obj')
        self.obj = obj
        if counter:
            self.__class__.rank += 1
    
    def __getattr__(self, name):
        self.__class__.action = name
        if type(self.obj) == dict:
            value = self.obj.get(name, None)
            if value:
                return self.__class__(value, counter=False)
        elif hasattr(self.obj, name):
            return self.__class__(getattr(self.obj, name, None), counter=False)
        else:
            self.__class__.action = ''
            raise AttributeError('Expect attribute: <%s> is not exist' % name)
    
    @validate
    def eq(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj == value)
    
    @validate
    def gt(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj > value)
    
    @validate
    def lt(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj < value)
    
    @validate
    def toBe(self, value):
        return (self, self.obj == value)
    
    @validate
    def match(self, value):
        if not value: return (self, False)
        
        if isinstance(self.obj, dict) and isinstance(value, dict):
            return (self, matchDict(self.obj, value))
        
        elif isNumber(self.obj) and isNumber(value):
            return self.eq(value)
        
        elif isinstance(self.obj, str) and isinstance(value, str):
            return (self, value in self.obj)
        else:
            return self.toBe(value)
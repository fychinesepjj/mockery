#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

import functools
from mockery.utils import matchDict, isNumber, Console

# Validate Expect func result
def validate(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            param = args[1] if len(args) > 1 else None
            this, isValid = func(*args, **kw)
            action = '.' + this.action if this.action else ''
            if isValid:
                msg = ' ' * 12 + '#%s Expect%s.%s  [Pass]\n' % (this.rank, action, func.__name__)
                msg += ' ' * 15 + 'Expect: %s, Result: %s' % (this.obj, param)
                Console.success(msg)
            else:
                msg = ' ' * 12 + '#%s Expect%s.%s  [Fail]\n' % (this.rank, action, func.__name__)
                msg += ' ' * 15 + 'Expect: %s, Result: %s' % (this.obj, param)
                Console.error(msg)
            return isValid
        except Exception as e:
            Console.error('@validate Exception:' + str(e))
    return wrapper
    

class Expect(object):
    '''
    from mockery.expect import Expect
    from mockery.response import Response
    import requests
    t=requests.get('http://localhost/test.json')
    res = Response(t)
    ept = Expect(res)
    ept.code.eq(200)
    '''
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
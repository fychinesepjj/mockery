#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import json
import traceback
import functools
from mockery.conf import settings
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
                msg = ' ' * 12 + '#%s Expect%s.%s  [Pass]' % (this.rank, action, func.__name__)
                Console.success(msg)
                msg = ' ' * 15 + 'Expect: %s, %s: %s\n' % (this.obj, func.__name__, param)
                Console.log(msg)
            else:
                msg = ' ' * 12 + '#%s Expect%s.%s  [Fail]' % (this.rank, action, func.__name__)
                Console.warn(msg)
                msg = ' ' * 15 + 'Expect: %s, %s: %s\n' % (this.obj, func.__name__, param)
                Console.log(msg)
            return (this, isValid)
        except Exception as e:
            Console.error('@validate Exception:' + str(e))
            if settings.DEBUG:
                msg = traceback.format_exc()
                Console.error(msg)
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
    
    def _eq(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj == value)
    
    def _gt(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj > value)
    
    def _lt(self, value):
        if not value:
            return (self, False)
        if not isNumber(self.obj) or not isNumber(value):
            return (self, False)
        return (self, self.obj < value)
    
    def _toBe(self, value):
        return (self, self.obj == value)
    
    @validate
    def eq(self, value):
        return self._eq(value)
    
    @validate
    def gt(self, value):
        return self._gt(value)
    
    @validate
    def lt(self, value):
        return self._lt(value)
    
    @validate
    def toBe(self, value):
        return self._toBe(value)
    
    @validate
    def contain(self, value):
        if not value: return (self, False)
        if isinstance(self.obj, dict) and isinstance(value, dict):
            return (self, matchDict(self.obj, value))
        
        elif isNumber(self.obj) and isNumber(value):
            return self._eq(value)
        elif isinstance(self.obj, str) and isinstance(value, str):
            # Try Json convert
            try:
                jsonObj = json.loads(self.obj)
                jsonValue = json.loads(value)
                if isinstance(jsonObj, dict) and isinstance(jsonValue, dict):
                    return (self, matchDict(jsonObj, jsonValue))
            except:
                pass
            return (self, value in self.obj)
        else:
            return self._toBe(value)
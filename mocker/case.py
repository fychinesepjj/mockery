#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import os
import types
import functools
from mocker.conf import settings
from mocker.utils import Console, loadModule, dumpJson


# 汇报Case执行情况
def report(desc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if(desc is None):
                Console.log('%s--->begin' % func.__name__)
            else:
                Console.log('%s--->begin' % desc)
            func(*args, **kw)
            if(desc is None):
                Console.log('%s--->end' % func.__name__)
            else:
                Console.log('%s--->end' % desc)
        return wrapper
    return decorator


class Case(object):
    
    def __init__(self):
        # used to load case data
        self._setup()
        if hasattr(self, 'init'):
            self.init()
        info = '%s--->init' % self.__class__.__name__
        Console.log(info.rjust(4, '>'))
        
    def _setup(self):
        # TODO
        dataPath = os.path.join(settings.DATA_PATH, settings.DATA_DIR)
        if os.path.exists(dataPath) and hasattr(self.__class__, 'data'):
            moduleName = '%s.%s' % (settings.DATA_DIR, self.__class__.data)
            define.clear()
            mod = loadModule(moduleName)
            definedData = define.getAll()
            self.data = definedData.get(self.__class__.data, None)
            
    def run(self):
        raise NotImplementedError('Case is a abstract class used for subclass')
        

class Define(object):
    store = {}
    
    def __call__(self, name, value, convert=None):
        try:
            if convert is None and settings.DEFINE_DEFAULT_CONVERT and settings.DEFINE_DEFAULT_CONVERT == 'json':
                convert = dumpJson
            if convert:
                if type(convert) == types.FunctionType:
                    self.store[name] = convert(value)
            else:
                self.store[name] = value
        except Exception as e:
            Console.error('@define Exception: ' + str(e))
    
    def clear(self):
        self.store = {}
        
    def getAll(self):
        return self.store

define = Define()

    


    

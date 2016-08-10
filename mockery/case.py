#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import os
import types
import functools
import traceback
from mockery.conf import settings
from mockery.utils import Console, loadModule, dumpJson


# Print Case running status
def report(desc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if(desc is None):
                msg = ' ' * 8 + '%s--->begin' % func.__name__
            else:
                msg = ' ' * 8 + '%s--->begin' % desc
            Console.log(msg)
            func(*args, **kw)
            if(desc is None):
                msg = ' ' * 8 + '%s--->end' % func.__name__
            else:
                msg = ' ' * 8 + '%s--->end' % desc
            Console.log(msg)
        return wrapper
    return decorator


class Case(object):
    
    def __init__(self):
        # Load case data
        self._setup()
        if hasattr(self, 'init'):
            self.init()
        info = ' ' * 4 + '%s--->init' % self.__class__.__name__
        Console.log(info)
        
    def _setup(self):
        currentPathName = os.path.basename(os.getcwd())
        dataPathName = os.path.basename(settings.DATA_PATH)
        if dataPathName != currentPathName:
            dataPath = os.path.join(os.path.abspath(settings.DATA_PATH), settings.DATA_DIR)
        else:
            dataPath = os.path.join(os.getcwd(), settings.DATA_DIR)

        if os.path.exists(dataPath) and hasattr(self.__class__, 'data'):
            moduleName = '%s.%s' % (settings.DATA_DIR, self.__class__.data)
            define.clear()
            mod = loadModule(moduleName)
            definedData = define.getAll()
            self.data = definedData
        else:
            Console.warn(' ' * 4 + '@%s setup: no data loaded!' % self.__class__.__name__)
    def run(self):
        raise NotImplementedError('Case is a abstract class used for subclass')
        

class Define(object):
    store = {}
    
    def __call__(self, name, value, convert=''):
        try:
            if convert == 'json' or \
                convert == '' and \
                settings.DEFINE_DEFAULT_CONVERT and \
                settings.DEFINE_DEFAULT_CONVERT == 'json':
                convert = dumpJson

            if convert:
                if type(convert) == types.FunctionType:
                    Define.store[name] = convert(value)
                else:
                    Define.store[name] = value
            else:
                Define.store[name] = value
        except Exception as e:
            Console.error('@define Exception: ' + str(e))
            if settings.DEBUG:
                msg = traceback.format_exc()
                Console.error(msg)
    
    def clear(self):
        Define.store = {}
        
    def getAll(self):
        return Define.store

define = Define()

    


    

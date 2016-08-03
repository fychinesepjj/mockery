#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import functools
from core.utils import Console


# 汇报Case执行情况
def report(desc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if(desc is None):
                Console.log('\n%s--->begin' % func.__name__)
			else:
				Console.log('\n%s--->begin' % desc)
			func(*args, **kw)
            if(desc is None):
                Console.log('\n%s--->end' % func.__name__)
			else:
				Console.log('\n%s--->end' % desc)
        return wrapper
    return decorator


class Case(object):
    
    def __init__(self, caseName):
		# used to load case data
        self.name = caseName
		self._setup()
		if hasattr(self, 'init'):
			self.init()
		info = '\n%s--->init' % self.name
    	console.log(info.rjust(4))
		
	def _setup(self):
		# TODO
		# find path and load data
		pass
	
    def run(self):
    	raise NotImplementedError('Case is a abstract class used for subclass')
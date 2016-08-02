#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from core.color import getColor
clr = getColor()

class Console(object):
    @staticmethod
    def log(text):
        print(text)
        
    @staticmethod
    def success(text):
        clr.print_green_text(text)
        
    @staticmethod
    def warn(text):
        clr.print_blue_text(text)
    
    @staticmethod
    def error(text):
        clr.print_red_text(text)

        
def loadModuleFile(module_file):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name, fromlist=['*'])
        return module
    except ImportError as e:
        Console.error('loadModuleFile:' + str(e))

        
def loadModule(module_name):
    try:
        module = __import__(module_name, fromlist=['*'])
        return module
    except ImportError as e:
        Console.error('loadModule:' + str(e))


if __name__ == "__main__":
    Console.log('hello world')
    Console.success('hello world')
    Console.warn('hello world')
    Console.error('hello world')
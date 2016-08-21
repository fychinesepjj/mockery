#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings, test_print

if __name__ == "__main__":
    loadSettings('examples.settings')
    
    from mockery.utils import Console
    from mockery.loader.file import FileLoader
    def testStrLoader():
        yield FileLoader('./examples/data/examples.json'), str
        
    def checkStr(result, status):
        data = result.load()
        if isinstance(data, status):
            return True
        return False
    
    test_print(testStrLoader, checkStr)
    
    def testJsonLoader():
        yield FileLoader('./examples/data/examples.json'), dict
        
    def checkDict(result, status):
        data = result.load()
        import json
        try:
            data = json.loads(data)
        except:
            data = None
        if isinstance(data, status):
            return True
        return False
    
    test_print(testJsonLoader, checkDict)
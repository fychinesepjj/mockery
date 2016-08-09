#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

import os
import sys
import json

from mockery.color import getColor
clr = getColor()

class Console(object):
    @staticmethod
    def log(text):
        clr.print_white_text(text)
        
    @staticmethod
    def success(text):
        clr.print_green_text(text)
        
    @staticmethod
    def warn(text):
        clr.print_yellow_text(text)
    
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
    module = None
    try:
        module = __import__(module_name, fromlist=['*'])
    except ImportError as e:
        Console.error('@loadModule:' + str(e))
    return module


def dumpJson(data):
	return json.dumps(data, sort_keys=True)


def matchDict(origin, dest):
	if not isinstance(origin, dict) or not isinstance(dest, dict):
		return False
	if len(dest) == 0:
		if len(origin) == 0:
			return True
		else:
			return False
	for k in dest.keys():
		status = True
		if k in origin:
			if isinstance(origin[k], dict) and isinstance(dest[k], dict):
				status = matchDict(origin[k], dest[k])
				if not status:
					return status
			elif origin[k] != dest[k]:
				return False
		else:
			return False
	return status


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def loadPath(new_path):
    try:
        if os.path.exists(new_path):
            sys.path.append(new_path)
    except:
        pass

    
if __name__ == "__main__":
    pass
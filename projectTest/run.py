#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import types

#未部署情况下，在本地目录使用core依赖
DEBUG = True
if DEBUG:
    try:
        full_path = os.path.realpath(__file__)
        base_path = os.path.dirname(os.path.dirname(full_path))
        sys.path.append(base_path)
    except Exception as e:
        print(e)

from core.utils import loadModule, Console
from core.case import Case
        
if __name__ == "__main__":
    setting_name = 'settings.py'
    if(os.path.exists(setting_name)):
        name, ext = os.path.splitext(setting_name)
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", name)
    else:
        raise Exception('Project settings is not exist!')
    
    if len(sys.argv) > 1:
        # case module must be relative to run.py
        fullName = sys.argv[1:2][0]
        name, ext = os.path.splitext(fullName)
        mod = loadModule(name)
        if not mod:
            sys.exit(0)
        caseClasses = []
        for k in dir(mod):
            m = getattr(mod, k)
            if type(m) == types.TypeType and issubclass(m, Case) and m != Case:
                caseClasses.append(m)
        print(caseClasses)
    else:
        Console.warn('usage: python run.py caseName')
    
            
	
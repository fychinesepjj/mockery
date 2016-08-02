#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#未部署情况下，在本地目录使用core依赖
DEBUG = True
if DEBUG:
    try:
        import sys
        full_path = os.path.realpath(__file__)
        base_path = os.path.dirname(os.path.dirname(full_path))
        sys.path.append(base_path)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    setting_name = 'settings.py'
    name, ext = os.path.splitext(setting_name)
    if(os.path.exists(setting_name)):
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", name)
    else:
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", 'core.settings')

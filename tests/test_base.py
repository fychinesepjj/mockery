#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def loadSettings(settings_name):
    settings_name = settings_name if settings_name else 'settings'
    try:
        import os
        import sys
        full_path = os.path.abspath('../.')
        print('\n[import path: %s]' % full_path)
        sys.path.append(full_path)
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", "settings")
    except:
        pass

if __name__ == '__main__':
    pass
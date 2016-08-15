#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_print(cases):
    print('\n---------------Test Start---------------\n')
    action = cases()
    try:
        while True:
            result, status = action.next()
            if result == status:
                print('--->[Passed]\n')
            else:
                print('--->[Fail]\nExpect=%s\nResult=%s\n\n' % (result, status))
            
    except StopIteration:
        return
    except Exception as e:
        print(e)
    finally:
        print('\n---------------Test End---------------\n')

def loadSettings(settings_name=None):
    settings_name = settings_name if settings_name else 'settings'
    try:
        import os
        import sys
        full_path = os.path.abspath('../.')
        print('\n[import path: %s]' % full_path)
        sys.path.append(full_path)
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", settings_name)
    except:
        pass

if __name__ == '__main__':
    pass
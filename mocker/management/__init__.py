#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import os
import sys
from mocker.utils import Console
    

class ManagementUtility(object):
    
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.cmd = self.argv[1] if len(self.argv) >= 2 else None
        self.param = self.argv[2] if len(self.argv) >= 3 else None
        self.prog_name = os.path.basename(self.argv[0])

    def help(self, *argv):
        usage = 'mocker usage:\n1. %(cmd)s help\n2. %(cmd)s run caseFile\n3. %(cmd)s create projectName\n' % {'cmd': self.prog_name}
        Console.warn(usage)
        
    def run(self, value):
        print('run', value)
    
    def create(self, value):
        print('create', value)
    
    def getCommand(self):
        if len(self.argv[1:]) <= 1:
            return self.help
        else:
            if hasattr(self, self.cmd):
                return getattr(self, self.cmd)
            else:
                self.help

    def execute(self):
        self.getCommand()(self.param)


def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = ManagementUtility(argv)
    utility.execute()
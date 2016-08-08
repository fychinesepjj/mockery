#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import os
import sys
import traceback
from mocker.conf import settings
from mocker.utils import Console, loadModule, loadPath
from mocker.case import Case
    

class ManagementUtility(object):

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.cmd = self.argv[1] if len(self.argv) >= 2 else None
        self.param = self.argv[2] if len(self.argv) >= 3 else None
        self.prog_name = os.path.basename(self.argv[0])

    def help(self, *argv):
        usage = 'Mocker usage:\n1. %(cmd)s help\n2. %(cmd)s run caseFile\n3. %(cmd)s create projectName\n' % {'cmd': self.prog_name}
        Console.warn(usage)
        
    def run(self, name):
        runPath = os.path.abspath(os.getcwd())
        filePath = os.path.abspath(name)

        if not os.path.exists(filePath):
            Console.error('@run: %s is not exists' % name)
            return
        if len(runPath) > len(filePath):
            Console.error('@run: running directory error!')
            return

        fullName = filePath.replace(runPath, '')
        pathName, ext = os.path.splitext(fullName)
        
        setting_dir = filePath
        # Support direct run project, default case name is cases.py
        if not ext.startswith('.py'):
            pathName = os.path.join(pathName, 'cases.py')
            setting_path = os.path.join(setting_dir, 'settings.py')
        else:
            setting_dir = os.path.dirname(filePath)
            setting_path = os.path.join(setting_dir, 'settings.py')
        
        if not os.path.exists(setting_path):
            desc = "settings.py"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable MOCKER_SETTINGS_MODULE "
                % desc)
        
        # configuare setting path
        setting_name = '%s.%s' % (os.path.basename(setting_dir), 'settings')
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", setting_name)
        
        # load run path
        loadPath(runPath)
        
        name = pathName.replace('\\\\','.').replace('\\','.').replace('//','.').replace('/','.') \
            .strip('.').strip('.py')

        mod = loadModule(name)
        if not mod:
            return

        caseClasses = []
        for k in dir(mod):
            cls = getattr(mod, k)
            if type == type(cls) and issubclass(cls, Case) and cls != Case:
                caseClasses.append(cls)

        for cls in caseClasses:
            try:
                msg = '\n%s--->before run' % cls.__name__
                Console.log(msg.rjust(4, '>'))
                cls().run()
            except Exception as e:
                Console.error('@run cls().run: ' + str(e))
                if settings.DEBUG:
                    msg = traceback.format_exc()
                    print(msg)
            finally:
                msg = '%s--->after run\n' % cls.__name__
                Console.log(msg.rjust(4, '>'))
    
    def create(self, projectName):
        import shutil
        from mocker import conf

        runPath = os.path.abspath(os.getcwd())
        targetDir = os.path.join(runPath, projectName)
        if os.path.exists(targetDir):
            Console.warn('Project directory <%s> has exists, Please use another name!' % projectName)
            return

        _PROJECT_TEMPLATE_NAME = 'project_template'
        _PROJECT_TEMPLATE_DIR = getattr(conf, '__path__', [])
        _PROJECT_TEMPLATE_DIR = _PROJECT_TEMPLATE_DIR[0] if len(_PROJECT_TEMPLATE_DIR) else ''

        _PROJECT_TEMPLATE = os.path.join(_PROJECT_TEMPLATE_DIR, _PROJECT_TEMPLATE_NAME)
        if os.path.exists(_PROJECT_TEMPLATE):
            try:
                shutil.copytree(_PROJECT_TEMPLATE, targetDir)
            except Exception as e:
                Console.error('@create Exception: ' + str(e))
        else:
            Console.warn('Project template is lost, Please create project manually!')
            return
    
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
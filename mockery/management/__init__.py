#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
import os
import sys
import traceback
from cookiecutter.main import cookiecutter

from mockery.conf import settings
from mockery.utils import Console, loadModule, loadPath
from mockery.case import Case
    

class ManagementUtility(object):

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.cmd = self.argv[1] if len(self.argv) >= 2 else None
        self.param = self.argv[2] if len(self.argv) >= 3 else None
        self.prog_name = os.path.basename(self.argv[0])

    def help(self, *argv):
        usage = 'Mockery usage:\n1. %(cmd)s help\n2. %(cmd)s run caseFile\n3. %(cmd)s create projectName\n' % {'cmd': self.prog_name}
        Console.warn(usage)
        
    def run(self, name):
        runPath = os.path.abspath(os.getcwd())
        filePath = os.path.abspath(name)

        if not os.path.exists(filePath):
            Console.error('@run: %s is not exists' % name)
            return

        pathName, ext = os.path.splitext(filePath)
        load_path = pathName
        
        # Support direct run project, default case name is cases.py
        if not ext.startswith('.py'):
            pathName = os.path.join(pathName, 'cases.py')
        else:
            load_path = os.path.dirname(pathName)
        
        setting_path = os.path.join(load_path, 'settings.py')
        if not os.path.exists(setting_path):
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable MOCKER_SETTINGS_MODULE "
                % setting_path)

        # add run path
        loadPath(load_path)

        # configuare setting path
        os.environ.setdefault("MOCKER_SETTINGS_MODULE", 'settings')
        
        name = os.path.basename(pathName).strip('py').strip('.')
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
                msg = ' %s--->before run' % cls.__name__
                Console.log(msg)
                cls().run()
            except Exception as e:
                Console.error('@run cls().run: ' + str(e))
                if settings.DEBUG:
                    msg = traceback.format_exc()
                    Console.error(msg)
            finally:
                msg = ' %s--->after run\n' % cls.__name__
                Console.log(msg)
    
    def create(self, projectName):
        from mockery import conf

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
                status = cookiecutter(
                    _PROJECT_TEMPLATE,
                    output_dir=runPath,
                    no_input=True,
                    extra_context={'directory_name': projectName}
                )
                Console.success('Project created: ' + status)
            except Exception as e:
                Console.error('@create Exception: ' + str(e))
                if settings.DEBUG:
                    msg = traceback.format_exc()
                    Console.error(msg)
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
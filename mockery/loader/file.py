#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

import os
import traceback
from mockery.conf import settings
from mockery.utils import Console
from mockery.loader import BaseLoader

class FileLoader(BaseLoader):
    
    def __init__(self, fileName):
        self.fp = None
        if os.path.exists(fileName):
            self.fp = open(fileName, 'r')
        else:
            Console.error('@FileLoader init fail: file <%s> is not exists' % fileName)

    def load(self):
        ''' load data of the file '''
        result = None
        if self.fp:
            try:
                result = self.fp.read().strip('\r\n')
            except Exception as e:
                Console.error('@FileLoader load Exception: ' + str(e))
                if settings.DEBUG:
                    msg = traceback.format_exc()
                    Console.error(msg)
        return result
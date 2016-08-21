#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

class BaseLoader(object):
    
    def load(self):
        """
        Must be implemented by subclasses to initialize the wrapped object.
        """
        raise NotImplementedError('subclasses of BaseLoader must provide a load() method')
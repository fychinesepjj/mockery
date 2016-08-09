#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings
from mockery.utils import Console

if __name__ == "__main__":
    loadSettings()
    Console.log('hello world')
    Console.success('hello world')
    Console.warn('hello world')
    Console.error('hello world')
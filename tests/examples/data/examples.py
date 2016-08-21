#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from mockery.case import define
from mockery.loader.file import FileLoader

# Must use absolute path
exampleFile = os.path.join(os.path.dirname(__file__), './examples.json')

define('jsonData', {
    "name": "abc",
    "age": 28,
    "desc": "this is a json mock"
});

define('dictData', {
    "name": "abc",
    "age": 28
}, convert=None);

define('strData','string data', convert=None);

define('numberData',123456789, convert=None);

define('fileStr', loader=FileLoader(exampleFile), convert=None);
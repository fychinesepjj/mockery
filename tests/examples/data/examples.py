#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mockery.case import define

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
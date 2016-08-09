#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings
from mockery.utils import matchDict

if __name__ == "__main__":
    loadSettings()
    #True
    origin={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    print(matchDict(origin, dest), True)

    #False
    origin={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    dest={}
    print(matchDict(origin, dest), False)

    #False
    origin={}
    dest={'a':1, 'b':[1,2,3], 'c': 2222}
    print(matchDict(origin, dest), False)

    #False
    origin={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': 2222}
    print(matchDict(origin, dest), False)

    #True
    origin={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': {}}
    print(matchDict(origin, dest), True)

    #False
    origin={'a':1, 'b':[1,2,3], 'c': {}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': {'e':2222}}
    print(matchDict(origin, dest), False)

    #False
    origin={'a':1, 'b':[1,2,3], 'c': {'e':2222, 't':'cccc'}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': {}}
    print(matchDict(origin, dest), False)

    #True:
    origin={'a':1, 'b':[1,2,3], 'c': {'e':2222, 't':'cccc'}, 'd':'aaaaa'}
    dest={'a':1, 'b':[1,2,3], 'c': {'e':2222}}
    print(matchDict(origin, dest), True)
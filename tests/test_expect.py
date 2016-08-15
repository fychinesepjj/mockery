#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan
from test_base import loadSettings, test_print

if __name__ == "__main__":
    loadSettings('settings')
    from mockery.expect import Expect
    
    def cases():
        yield Expect(200).eq(200)[1], True
        yield Expect(200).eq(404)[1], False
        # validate json
        j1 = '{"name": "abc", "age": 12}'
        j2 = '{"name": "abc", "age": 12, "height": 178}'
        yield Expect(j1).toBe(j1)[1], True
        yield Expect(j1).toBe(j2)[1], False
        yield Expect(j1).contain(j1)[1], True
        yield Expect(j1).contain(j2)[1], False
        yield Expect(j2).contain(j1)[1], True

        # validate dict
        d1 = {'name': 'abc', 'age': 12}
        d2 = {'name': 'abc', 'age': 12, 'height':178}
        yield Expect(d1).contain(d1)[1], True
        yield Expect(d2).contain(d1)[1], True
        yield Expect(d1).contain(d2)[1], False

        # validate number
        yield Expect(123456789).contain(123456789)[1], True
        yield Expect(123456789).contain(123)[1], False

        # validate string
        s1 = 'source string'
        s2 = 'other string'
        yield Expect(s1).contain(s1)[1], True
        yield Expect(s1).contain(s2)[1], False

    test_print(cases)
    
    

    
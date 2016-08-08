#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mocker.request import Request, Api, catch


req = Request()

class TestExampleApi(Api):
    @req.get('http://192.168.1.101:8080/json/test.json')
    @catch
    def getExample(self, res):
        self.exampleResponse = res

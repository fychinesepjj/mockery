#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mockery.request import Request, Api, catch


req = Request()

class TestExampleApi(Api):

    @req.get('http://localhost:8080/json/test.json')
    @catch
    def getExample(self, res):
        self.exampleResponse = res

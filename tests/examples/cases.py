#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mockery.case import Case, report
from mockery.expect import Expect

from request import TestExampleApi

class TestExampleCase(Case):
    data = 'examples'
    
    def init(self):
        self.exampleApi = TestExampleApi()

    @report(u'Test example')
    def testExample(self):
        # fetch data
        self.exampleApi.getExample()
        
        # validate response
        Expect(self.exampleApi.exampleResponse).code.eq(200)
        
        # validate json
        Expect(self.exampleApi.exampleResponse.json).toBe(self.data.get('jsonData'))
        
        # validate dict
        Expect(self.exampleApi.exampleResponse.dict).contain(self.data.get('dictData'))
        
        # validate number
        Expect(123456789).contain(self.data.get('numberData'))
        
        # validate string
        Expect('source string').contain(self.data.get('strData'))

    def run(self):
        self.testExample()
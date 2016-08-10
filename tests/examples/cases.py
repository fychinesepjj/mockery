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
        Expect(self.exampleApi.exampleResponse.dict).match(self.data.get('dictData'))

    def run(self):
        self.testExample()
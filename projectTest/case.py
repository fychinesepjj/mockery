#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from core.case import Case, report
from core.expect import Expect
from request import TestMovieApi

class TestCase(Case):
    def init(self):
        self.testApi = TestMovieApi()

    @report(u'测试影片Api接口')
    def testMovie(self):
        # fetch data
        self.testApi.getMovie()
        # testing
        Expect(self.testApi.movieResponse).code.eq(200)

    def run(self):
        self.testMovie()
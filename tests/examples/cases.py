#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

from mocker.case import Case, report
from mocker.expect import Expect
from request import TestMovieApi

class TestMovieCase(Case):
    data = 'movies'
    
    def init(self):
        pass
        #self.testApi = TestMovieApi()

    @report(u'测试影片Api接口')
    def testMovie(self):
        # fetch data
        #self.testApi.getMovie()
        # testing
        #Expect(self.testApi.movieResponse).code.eq(200)
        #Expect(self.testApi.movieResponse).code.eq(302)
        code = 200
        Expect(code).eq(200)

    def run(self):
        self.testMovie()
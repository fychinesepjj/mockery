#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

from mocker.request import Request, Api, catch

# req = Request(session=True)
req = Request()

class TestMovieApi(Api):
    #@req.get('http://192.168.1.101:8080/json/baidu.json')
    @req.get('http://192.168.95.1:8080/json/baidu.json')
    @catch
    def getMovie(self, res):
        self.movieResponse = res
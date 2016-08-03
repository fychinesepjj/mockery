#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from core.request import Request, Api, catch

# req = Request(session=True)
req = Request()

class TestMovieApi(Api):

	@req.get('http://192.168.1.175/json/baidu.json')
	@catch
	def getMovie(self, res):
		self.movieResponse = res
		

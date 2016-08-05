#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: jjpan

import requests
from mocker.utils import Console, dumpJson

'''
from mocker.response import Response
import requests
t=requests.get('http://192.168.95.1:8080/json/baidu.json')
res = Response(t)
res.dict
res.json
'''
class Response(object):
	
	def __init__(self, res):
		if not isinstance(res, requests.models.Response):
			raise Exception('Response initialize: only accept requests.models.Response type object')
		self._res = res
		self.status = res.reason # ok
		self.code = res.status_code # 200
		self.content = res.content # text and images
		self.text = res.text # only text
		self.headers = res.headers
		self.cookies = res.cookies
		self.encoding = res.encoding #utf-8
	
	@property
	def json(self):
		return dumpJson(self.dict)

	@property
	def dict(self):
		json_result = {}
		if(self._res):
			try:
				json_result = self._res.json()
			except ValueError as e:
				Console.error(e)
			finally:
				return json_result
		return json_result

	def __repr__(self):
		return '<%(cls)s "%(code)s">' % {'cls': self.__class__.__name__, 'code': self.code}
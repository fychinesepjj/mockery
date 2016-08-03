#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import functools
import json
from core.response import Response
from core.utils import Console
from core.conf import settings


# 捕获decorated func执行过程中的异常
def catch(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            Console.error('@catch Exception:' + str(e))
    return wrapper


# 检查response成功状态
def checkStatus(code=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if(code is None):
                Console.warn(str(func.__name__) + '-> @checkStatus Warn:' + ' parameter code missing!')
                return
            res = kw.get('res', None)
            if(res):
                if(res.status_code == code):
                    Console.success('response status: ok, %s' % res.status_code)
                    return func(*args, **kw)
                Console.error('response status: %s !== %s(required)' % (res.status_code, code))
        return wrapper
    return decorator


class Request(object):
    def __init__(self, session=False):
        if(session):
            self.requests.Session()
        else:
            self.requests = requests
    
    # GET请求
    def get(self, url=None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                if(url is None):
                    Console.warn(str(func.__name__) + '-> @get Warn:' + ' parameter url missing!')
                    return
                try:
                    kw['timeout'] = kw['timeout'] if kw.get('timeout', None) else settings.TIME_OUT
                    kw['params'] = kw['data'] if kw.get('data', None) else kw.get('params', None)
                    res = self.requests.get(url, **kw)
                    wrappedResponse = Response(res)
                    return func(res=wrappedResponse)
                except Exception as e:
                    Console.error('@get Exception:' + str(e))
            return wrapper
        return decorator

    # POST请求
    def post(self, url=None):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                if(url is None):
                    Console.warn(str(func.__name__) + '-> @post Warn:' + ' parameter url missing!')
                    return
                try:
                    kw['timeout'] = kw['timeout'] if kw.get('timeout', None) else settings.TIME_OUT
                    kw['data'] = json.dumps(kw['json']) if kw.get('json', None) else kw.get('data', None)
                    res = self.requests.post(url, **kw)
                    wrappedResponse = Response(res)
                    return func(res=wrappedResponse)
                except Exception as e:
                    Console.error('@post Exception:' + str(e))
            return wrapper
        return decorator


class Api(object):

    def __getattr__(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        raise AttributeError('Api attribute: <%s> is not exist' % name)

        
if __name__ == '__main__':
    url = 'http://localhost/php/get.php'
    req = Request()
    
    '''
    Usage Examples
    '''
    @req.get(url)
    @checkStatus(code=200)
    @catch
    def get_request(res):
        print(res.text)
        
    # Only GET
    #get_request()
    
    # GET with params
    #get_request(data={'name':'abc', 'age': 12})
    #get_request(data={'name':'abc', 'age': 12}) == #get_baidu(params={'name':'abc', 'age': 12})

    url2 = 'http://localhost/php/request.php'
    @req.post(url2)
    @checkStatus(code=200)
    @catch
    def post_request(res):
        print(res.text)

    # POST Form data
    #post_request(data={'name':'abc', 'age': 12})
    
    # POST Json data
    #post_request(json={'data': {'name':'abc', 'age': 12}})
    
    # POST a file
    #post_request(files = {'file': open('touxiang.png', 'rb')})
    
    # POST with cookies
    #cookies = {'cookies_are':'working'}
    #post_request(cookies = cookies)
    
    # POST with headers
    #headers = {'content-type': 'application/json'}
    #post_request(headers = headers)
    
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:23:40 2018

@author: Herbert
"""
import urllib

response_1 = urllib.request.urlopen("http://www.baidu.com")

print(response_1.getcode())

cont = response_1.read()

print(len(cont))

import http.cookiejar as hc

cj = hc.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

urllib.request.install_opener(opener)

response = urllib.request.urlopen("http://www.baidu.com")

print(len(response.read()))
print(cj)

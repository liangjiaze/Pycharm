'''
Created on 2018年3月17日

@author: jade
'''
import os
import requests

print(os.getcwd())

r = requests.get('http://blog.sina.com.cn')
print(r.url)
print(r.encoding)

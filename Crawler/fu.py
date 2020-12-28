# coding=utf8

import urllib
import subprocess

MAX_RETRY_TIME = 3


def run_command(cmd):
    retry = 0
    while retry < MAX_RETRY_TIME:
        (status, output) = subprocess.getstatusoutput(cmd)
        if status != 0:
            retry += 1
            continue
        return status, output


def search(word):
    params = {'word': word}
    url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&%s" % urllib.parse.urlencode(params)
    cmd = u'open "{}"'.format(url)
    run_command(cmd)


if __name__ == '__main__':
   result =  search('花')  # 调用search(word)函数，传入自定义参数

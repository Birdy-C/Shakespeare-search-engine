# -*- coding:utf-8 -*-

#导入一些需要用到的标准库
import urllib2
import re
import sys
import time

#定义获取html的函数
def getHtml(url):
    #为了防止被网页禁掉设置的Header
    setheader = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    #建立一个请求
    request = urllib2.Request(url,headers = setheader)
    #用urlopen获取页面代码
    response = urllib2.urlopen(request)
    #读取
    content = response.read()
    #为了防止出现乱码，先用utf-8解码再用系统编码
    content = content.decode('utf-8','replace').encode(sys.getfilesystemencoding())
    return content

#定义解析html的函数
def parseContent(html):
    #正则表达式
    pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
    #进行匹配
    getlist=re.findall(pattern,html)
    #打印
    for i in range(0,len(getlist)):
        print('<----------------------------------------------------------------->\n')
        #去掉空格
        print(replace(getlist[i].strip(' ')))
        print('\n')

#定义去掉超链接的函数
def replace(li):
    #用正则表达式去掉所有含超链接的部分
    li=re.sub(re.compile('<a.*?>|</a>'),'',li)
    return li

#主要部分    
for i in range(2,10):
    #调用函数getHtml,对各页进行打印
    content = getHtml("http://tieba.baidu.com/p/2109233792?pn=" + str(i))
    #调用函数parseContent
    parseContent(content)
    #设置一个暂停时间，防止连续请求使对方服务器奔溃
    time.sleep(5)

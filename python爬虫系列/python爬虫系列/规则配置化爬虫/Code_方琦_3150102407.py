# -*- coding:utf-8 -*-
#导入要用到的库
import urllib2
import re
import sys
import time
import json


#定义一个全局变量list，包含txt文本中的正则表达式
allrules=[]


#定义获取html的函数
def getHtml(url):
    #为了防止被禁，设置header
    setheader = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url,headers = setheader)
    response = urllib2.urlopen(request)
    content = response.read()
    #为了防止出现乱码，先用utf-8解码再用系统编码    
    content = content.decode('utf-8','replace').encode(sys.getfilesystemencoding())
    return content

#定义解析html的函数
def parseContent(html,rulelist):
    for rule in rulelist:
        name = rule["name"]
        sinrule = rule["rule"]
        pattern = re.compile(sinrule, re.S)
        result = re.findall(pattern, html)
        print(replace(name.decode("utf-8","replace").encode(sys.getfilesystemencoding())+"="+result[0].strip()))
        print('<----------------------------------------------------------------->\n')

#定义读取文本并输出信息的函数
def readConf():
    #打开“zhengze.txt”文本
    getfile = open("conf.txt","r")
    while True:
        #读出每一行
        line = getfile.readline()
        if line:
            #通过制表符分隔url和rules
            line = line.strip().split("\t")
            url = line[0]
            rules = line[1]
            #读取json
            rulelist = json.loads(rules)
            #将信息放入字典
            dic = dict()
            dic["url"] = url
            dic["rulelist"] = rulelist
            #把字典添加到列表里
            allrules.append(dic)
        else:
            break
    #关闭
    getfile.close()

def replace(li):
    #用正则表达式去掉一些无用部分
    li=re.sub(re.compile('<p>|</p>|<!--repaste.body.end-->|&rdquo|&ldquo'),'',li)
    return li

readConf()

for rule in allrules:
    url = rule["url"]
    rulelist = rule["rulelist"]
    content = getHtml(url)
    parseContent(content,rulelist)
    time.sleep(2)
            
    

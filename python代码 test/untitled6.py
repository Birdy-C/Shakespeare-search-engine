# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:11:09 2017

@author: Cherry
"""

import re
import requests

# 获取网页内容
r = requests.get('http://shakespeare.mit.edu/allswell/allswell.1.2.html')
data = r.text
# 利用正则查找所有连接

link_list =re.findall(r'<blockquote>.+?<A NAME=.+?>(.+?)</a>.+?</blockquote>'
                      ,data)
#link_list =re.findall(r'<a name=".+?">(.+?)</a>'
#                      ,data)

#link_list =re.compile(r'(?<=<a>)(.*?)(?=</a>)')
#link_list =re.findall(r"(?<=href=\")(?!http|/).+?(?=\")" ,data)
file_object = open('1-1.txt', 'w')

for url in link_list:
    file_object.write(url+'\n')
    #print url
    
file_object.close()


# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:22:23 2017

@author: Cherry
"""

# coding:utf-8
import re
import requests

# 获取网页内容
r = requests.get('http://shakespeare.mit.edu/1henryiv/index.html')
data = r.text

# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\")(?!http|/|full).+?(?=\")" ,data)
#link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
file_object = open('1-1.txt', 'w')

for url in link_list:
    file_object.write('http://shakespeare.mit.edu/'+url+'\n')
    #print url
    
file_object.close()


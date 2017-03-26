# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:39:51 2017
@author: Birdy 
"""

import re
import requests

# 获取网页内容
r = requests.get('http://shakespeare.mit.edu/')
data = r.text

link_list =re.findall(r'<a href=".+?">(.+?)</a>'
                      ,data)
file_object = open('title.txt', 'w')

for title in link_list:
    file_object.write(title+'\n')
    print title
    
file_object.close()


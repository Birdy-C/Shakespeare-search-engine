# coding:utf-8
import re
import requests

# 获取网页内容
r = requests.get('http://shakespeare.mit.edu/index.html')
data = r.text

# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\")(?!http|/).+?(?=\")" ,data)
#link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
file_object = open('thefile.txt', 'w')

for url in link_list:
    file_object.write('http://shakespeare.mit.edu/'+url+'\n')
    #print url
    
file_object.close()


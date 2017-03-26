#-*- coding:utf-8 -*-

import re
import urllib
import urllib2
from bs4 import BeautifulSoup
import urlparse
import chardet
import socket

import os #文件操作需要的库
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
socket.setdefaulttimeout(60)

def get_content(url):
	html = urllib.urlopen(url)
	content = html.read()
	#可将源码保存	
	#local = 'try.txt'
	#urllib.urlretrieve(url,local)
	return content

def get_essay(info,num):
	soup = BeautifulSoup(info,"lxml")
	[script.extract() for script in soup.findAll('script')]
	[style.extract() for style in soup.findAll('style')]
	name = str(num) +'.txt'

	print name
	
	f = file(name,'w')
	for title in soup.select('body') :
		f.writelines(title.get_text())
		f.writelines(" ")
		
		
	#f.writelines(information);
	f.close() 
	return 0


def get_url_index(url):
	website = urllib.urlopen(url)
	html = website.read()
	
	fp = open("index.txt", 'a')			#创建空文件
	
	#target_url_h = re.compile(r'\".*?/index.html\"').findall(html)
	target_url_h = re.compile(r'\".*?.html\"').findall(html)
	 
	target_num_h = len(target_url_h)
	print target_url_h
	#for j in range(37 ,target_num_h):
	for j in range(39 ,target_num_h):#这以部分没有目录
		url_1 =  url + target_url_h[j][1:-1] #e.g.http://shakespeare.mit.edu/Poetry/LoversComplaint.html
	
		new= target_url_h[j].replace('index.html','')
		website_1 = urllib.urlopen(url_1)
		html_1 = website_1.read()
		number_1 = 4
		number_2 = j-38
		number_2 += 1;

		#print target_num_1
		new_url = url+new[1:-1]
			
		info = get_content(new_url)
		print new_url
		number = number_1*100000+number_2*1000+1 #code the file 
		get_essay(info,number)
		docid = str(number) + ' '
		fp.write(docid)
		fp.write(new_url+'\n')


get_url_index("http://shakespeare.mit.edu/")
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
	print info
	soup = BeautifulSoup(info,"lxml")
	

	[script.extract() for script in soup.findAll('script')]
	[style.extract() for style in soup.findAll('style')]
	
	name = str(num) +'.txt'
	
	print name
	
	f = file(name,'w+')
	#reg = re.compile(r"<[^>]+>",re.S)
	#information = reg.sub("",info)
	#list = soup.find_all('blockquote')
	#print list
	#list1 = soup.select('blockquote')
	#print list1
	for title in soup.select('body') :
		f.writelines(title.get_text())
		f.writelines(" ")
		
		
	#f.writelines(information);
	f.close() 
	
	return 0

def get_url_index(url):


	info = get_content(url)
		
	get_essay(info,0123)



get_url_index("http://shakespeare.mit.edu/Poetry/elegy.html")
#-*- coding:utf-8 -*-

import re
import urllib
import urllib2
from bs4 import BeautifulSoup
import urlparse
import chardet
import socket

import os #�ļ�������Ҫ�Ŀ�
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

socket.setdefaulttimeout(60)

def get_content(url):
	html = urllib.urlopen(url)
	content = html.read()
	#�ɽ�Դ�뱣��	
	#local = 'try.txt'
	#urllib.urlretrieve(url,local)
	return content

def get_essay(info,num):

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
	website = urllib.urlopen(url)
	html = website.read()
	
	fp = open("mulu1.txt", 'w')			#�������ļ�
	
	#target_url_h = re.compile(r'\".*?/index.html\"').findall(html)
	target_url_h = re.compile(r'\".*?.html\"').findall(html)
	 
	target_num_h = len(target_url_h)
	print target_url_h
	#for j in range(37 ,target_num_h):
	for j in range(39 ,target_num_h):
		url_1 =  url + target_url_h[j][1:-1]
	
		new= target_url_h[j].replace('index.html','')
		website_1 = urllib.urlopen(url_1)
		html_1 = website_1.read()
		#target_url_1 = re.compile(r'\".*?.html\"').findall(html_1)
		#target_num_1 = len(target_url_1)
		if j>=0 and j<=16:
			number_1 = 1
			number_2 = j
		elif j>=17 and j<=26:
			number_1 = 2
			number_2 = j-17
		elif j>=27 and j<=36:
			number_1 = 3
			number_2 = j-27
		elif j>=37:
			number_1 = 4
			number_2 = j-38
		
		number_2 += 1;

		#print target_num_1
		#for k in range(0,target_num_1):
			#new_url = url+new[1:-1] +target_url_1[k][1:-1]
		new_url = url+new[1:-1]
			
		info = get_content(new_url)
		print new_url
		number = number_1*100000+number_2*1000+1
		get_essay(info,number)
		docid = str(number) + ' '
		fp.write(docid)
		fp.write(new_url+'\n')


get_url_index("http://shakespeare.mit.edu/")
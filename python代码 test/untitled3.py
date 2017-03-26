# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:50:52 2017

@author: Cherry
"""
# -*- coding: utf-8 -*-

def get_page(url):   #获取源码
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(page):   #寻找剩下的页面出现的网址
    start_link = page.find('<a href="http://shakespeare.mit.edu/')
    if start_link == -1: 
        return None, 0
    start_link=start_link-8
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):     #连接
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):  #获取当前页出现的网址

    links = []
    while True:
        url,endpos = get_next_target(page) #处理函数
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_pages):  #从一个seed url开始挖，挖到一定数量停止
    tocrawl = [seed]
    crawled = []
    index = [] #update
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages: #爬到一定的页数停止，不然会一直查下去
            content = get_page(page) #get the content of the url
            add_page_to_index(index,page,content) # 把源码，网址，列表，送去处理
            union(tocrawl,get_all_links(content)) #连接未挖掘的和当前网页中的子连接
            crawled.append(page)  #已挖
    return index 


def lookup(index,keyword):#还没使用的，查找函数
    for i in index:
        if i[0] == keyword:
           return i[1]
    return []



print crawl_web("http://shakespeare.mit.edu/index.html",2) 
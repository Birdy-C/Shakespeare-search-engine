# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:41:26 2017

@author: Cherry
"""

import requests,bs4,re
url="http://shakespeare.mit.edu/"
  
def getLinks(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    links = []
  
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
  
    return links
  
list_links=getLinks(url)
print( getLinks(url) )
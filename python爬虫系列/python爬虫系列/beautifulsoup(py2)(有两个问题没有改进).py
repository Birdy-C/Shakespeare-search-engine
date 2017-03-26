# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

for pagenum in range(1,5):   #多页
    f = open('C:/Users/fangqi/Desktop/a/tucao.txt','w')  # a表示追加模式
    url = "https://www.zhihu.com/collection/27109279?page="+str(pagenum)
    page = urllib2.urlopen(url) #打开网址
    content = page.read() #读取网址所有源代码
    #print content
    
    soup = BeautifulSoup(content,"html.parser")#建立一个bs对象
    All = soup.findAll(attrs = {'class':["zm-item-title","zh-summary summary clearfix"]}) #下面class代表样式，在需要的内容上右键，检查，找到对应的class，复制过来。若有多个的，放入列表。 
    #print All     #从源码中间找到标签所在的内容
    ########这里的findAll和re模块里的findAll用法稍微有点差异##########
    ########这里All里面是2个样式里的内容，包括标签，若只想要文字，要么用正则，要么用下面的处理########

    ########不用正则的话，需要下面的处理去掉All里面不需要的字符#########
    for each in All:  #打印话题+回复内容(All是一个列表)
        try:
            if each.name =='h2': #右键检查后，发现标题前有h2标签（标签是h2类型），而回复前没有这个标签，因此可以用它来区分标题和回复
             
#  <a target="_blank" href="/question/38627388">开车的人和不开车的人思维有什么区别？</a>
             #  标题在上面这个a标签里，用string可以获取标签里的文字
                print each.a.string #获取的内容在a标签里面
                if each.a.string: #如果有内容
                    f.write('问题： '+each.a.string+'\n') #把抓取的内容写到文件里面
                else:
                    f.write("无内容")
            else: #代表回复的内容
                print each.get_text()+'\n'
                if each.get_text():
                    content = each.get_text().replace('显示全部','')
                    f.write('回复： '+content.strip()+'\n\n')
                else:
                    f.write("无内容")
        except Exception as e:
            continue
f.close()


###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
###############这个程序有两个问题，第一是写不进txt里，第二是replace去不掉“显示全部”##############################
'''
#bsp不需要正则表达式，但获取的内容是包括标签的，我们需要的是标签里的文字

html = '<title>同学们好棒</title>'
soup = BeautifulSoup(html)
print soup.title

#访问本地文件内容
html = ''
soup = BeautifulSoup(open('a.html'),'html.parser')  #如果不加html.parser，则会出现标签
print soup.prettify()#打印本地文件内容，格式化打印内容

'''

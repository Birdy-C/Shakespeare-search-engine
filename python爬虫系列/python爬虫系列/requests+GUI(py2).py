# -*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText   #文本滚动条
import urllib,requests
import re   #正则表达式
import threading #多线程处理与控制

url_name = [] #url+name
a = 1
def get():
    global a #全局变量
    
    #用模拟浏览器访问来防止反爬虫机制
    #浏览器--F12--network--F5--点击左边name任意一处--查看右边headers
    hd = {'User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'http://www.budejie.com/video/'+str(a)  #多个页面
    varl.set('已经获取到第%s页视频'%(a))
    html = requests.get(url,headers=hd).text #.text表示获取源码
    #print html
    a+=1
    url_content = re.compile(r'<div class="j-r-list-c">.*?</div>.*?</div>',re.S)  #前面匹配视频，而re.S匹配换行符
    url_contents = re.findall(url_content,html) #从html中找到url_content，即从后者找到前者
    #中文在可迭代对象里是unicode编码
    #print url_contents
    
    for i in url_contents:   #包括名字和视频的一个列表
        url_reg = r'data-mp4="(.*?)">' #匹配地址
        url_items = re.findall(url_reg,i)  #视频的列表
        #print url_items
        if url_items:     #判断视频列表是否存在，如果不存在，就不抓它的名字
            #a表示超链接标签
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</\w',re.S)
            name_items = re.findall(name_reg,i)  #名字的列表
            for i,k in zip(name_items,url_items):
                url_name.append([i,k])
                print i, k
    return url_name

id = 1 #视频的个数
def write():    #下载
    global id #全局变量
    while id<10:
        url_name = get()
        for i in url_name:  #名字+地址
            #下载,我们看到的需要gbk编码
            urllib.urlretrieve(i[1],'video\\%s.mp4'%(i[0].decode('utf-8').encode('gbk')))
            text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')  #把文字加入到下面的GUI界面里
            url_name.pop(0)  #每显示一个之后就把这个删掉，进行下一个
            id+=1
    varl.set('视频链接和名字抓取完毕,over')
                                
def start():  #多线程
    th = threading.Thread(target = write)     #实例化
    th.start() #start触发

################################GUI图形界面###########################################

#设置窗口
root = Tk()        #实例化一个变量（可以把root理解为一个窗口）
root.title('窗口标题')  #更改窗口名称
root.geometry('500x300+300+100')  #让窗口出现在屏幕指定位置(乘号表示大小，加号表示位置)

#设置文本滚动条
text = ScrolledText(root,font=('微软雅黑',10))  #对文本的字体进行设置
text.grid()   #布局的方法//还可以用pack方法（比较简单的布局）

#设置按钮,点击之后触发start多线程
button = Button(root,text = '开始爬取',font=('微软雅黑',10),command = start)
button.grid()

#设置变化的文字
varl = StringVar()  #设置一个变量
label = Label(root,font=('微软雅黑',10),fg='red',textvariable=varl)
label.grid()
varl.set('已准备...')

#主循环
root.mainloop()    #创建窗口的指令，进入消息循环

################################GUI图形界面###########################################

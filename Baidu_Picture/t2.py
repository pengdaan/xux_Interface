# -*- coding:utf-8 -*-
import re,ssl
import urllib
from urllib.request import urlopen,urlretrieve
#获取抓取页面的源代码

def getHtml(url):
    context = ssl._create_unverified_context()
    page = urllib.request.urlopen(url,context=context)
    html = str(page.read())
    page.close()
    return html
#通过源代码以及正则表达式，匹配我们的url
def getImg(html):
    reg = r'<img class="BDE_Image" src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urlretrieve(imgurl,'C:\\Users\\Water\\PycharmProjects\\test\\image\\%s-%s.jpg' % (i,x))
        x = x + 1
#调用函数
i = 1
while i < 83:
    html = getHtml("http://tieba.baidu.com/p/3125473879?pn=" + str(i))
    getImg(html)
    i+=1
    print(i)
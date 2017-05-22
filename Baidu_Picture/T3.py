# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:49:43 2016


@author: hhxsym
"""


import os
import requests
from bs4 import BeautifulSoup
import urllib #用于下载图形




inpath="D:\\xux_project\\Baidu_Picture\\image"
inpath = unicode(inpath , "utf8") 
os.chdir(inpath)  #不做编码转换后，中文路径无法打开，更改




#实现单页访问
def download_jpg(url):
    response = requests.get(url) #请求网页，获得响应的内容
    print response.status_code  #打印状态码
    
    soup = BeautifulSoup(response.text, 'lxml') #解析响应的内容 BeautifulSoup(响应变量，解析器)
    #print soup
    urls = soup.find_all('img', 'BDE_Image') # find_all方法，基于CSS返回到元素，获取图片的地址， soup.find_all(标签， CSS样式)
    #print urls
    for url in urls:
        url=url.get('src')  #通过标签获取到元素，用get方法，直接获取解析标签对应的属性值
        print url
        urllib.urlretrieve(url,'%s' % url.split('/')[-1]) #下载图片，命名
        urllib.urlretrieve(url,'img/%s' % url.split('/')[-1]) #下载图片，命名,放到指定文件夹，注：img文件夹必须提前创建
    


#实现多页访问
def get_all_jpg(url, pages):
    for page in range(1, pages+1):
        new_url=url + '?pn=' + str(page) #构造地址
        download_jpg(new_url)
        




if __name__ == '__main__':
    #download_jpg("http://tieba.baidu.com/p/3797994694?pn=1")
    get_all_jpg("http://tieba.baidu.com/p/3797994694", 5)
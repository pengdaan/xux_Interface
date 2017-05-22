# -*- coding:utf-8 -*-
import ssl
import urllib
import urllib.request
import urllib.error
import re
import os
from pip._vendor.distlib.compat import raw_input



class Tool:
    #去除img标签,1-7位空格, 
    removeImg = re.compile('<img.*?>| {1,7}| ')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()将前后多余内容删除
        return x.strip()


class tieba:
    def __init__(self,baseUrl2,seeLZ1):
        
         #初始化，传入基地址，是否只看楼主的参数
        self.baseUrl = baseUrl2
        
        self.seeLZ = '?see_lz='+str(seeLZ1)
        print('kanlouzhu' + self.seeLZ)
        self.file = None
        self.floor = 1               
        self.tool = Tool()
    def getPage(self,pageNum):
        try:
            context = ssl._create_unverified_context()
            Url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            print('url',Url)
            request = urllib.request.Request(Url)
            response = urllib.request.urlopen(request, context=context)
            print('getpage')
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('连接失败，错误原因：',e.reason)
                return None
    
    #获取帖子标题      
    def getTitle(self,page):
        pattern = re.compile('<h1 class="core_title_txt.*?</span>(.*?)</h1>',re.S)
        result = re.search(pattern, page)
        if result:
            print('gettitle')
            return result.group(1).strip()
        else:
            return None
        
    #获取帖子页数
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        print('duyeshu')
        result = re.search(pattern,page)
        if result:
            print('getpagenum')
            return result.group(1).strip()
        else:
            return None
        #获取所有图片
    def getImg(self,page):
        #以下注释的两行，如果保留，只会获取每页第一贴的内容中的图片，注释后，获取的是整页的图片
        #pattern = re.compile('<div id="post_content_.*?>(.*?)></div>', re.S)
        #content = re.search(pattern,page)
       
       #正则表达式，根据需要，随时改进
        patternImg = re.compile('<img class="BDE_Image.*? src="(.*?)" pic_ext.*?>', re.S)
        
        #patternImg = re.compile('<img class="BDE_Image" src="(.*?)" width="560.*?>', re.S)
        
        imgs = re.findall(patternImg,page)
        print (imgs)
        print('getimgs')
        return imgs
    
    #保存多张图片
    def saveImgs(self,imgs,floor,lujing):
        number = 1
               
        print('发现' + str(floor) + '页共有',len(imgs), '张图片')
        for imageURL in imgs:
            splitpath = imageURL.split('.')
            fTail = splitpath.pop()
            if len(fTail) > 3:
                fTail = 'jpg'
            
            filename = floor + str(number) + '.' + fTail
            number += 1
                       
            print('saveimgs')
            self.saveImg(imageURL,filename,lujing)
            
    def saveImg(self,imageURL,filename,lujing):
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open( str(lujing) + '\\' + filename,'wb')
        f.write(data)
        print('正悄悄保存一张图片为',filename)
        f.close()
        
    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        print('mkdir')
        if not isExists:
            print('创建了名字叫做',path,'的文件夹')
            os.makedirs(path)
            
            print('路径1111111111')
            return path
        else:
            print('名为',path,'的文件夹已存在')
            print('路径2',path)
            return path
            
    def start(self):
        indexPage = self.getPage(1)
        print('1')
        pageNum = self.getPageNum(indexPage)
        print('2')
        title = self.getTitle(indexPage)
        print('3')
        
        print('4')
        path = self.mkdir("d:\pa")
        #path = self.mkdir("d:\pa" + title)
        print('path',path)
        
        print('7')
        if pageNum == None:
            print ("URL已失效，请重试")
            return
        try:
            print ("该帖子共有" + str(pageNum) + "页")
            for i in range(1,int(pageNum)+1):
                print ("正在写入第" + str(i) + "页数据")
                page = self.getPage(i)
                
                images = self.getImg(page)
                self.saveImgs(images,str(i),path)
        #出现写入异常
        except IOError as e:
            print ("写入异常，原因" + e.message)
        finally:
            print ("写入任务完成")
            
            
#print ("请输入帖子代号")

baseURL = 'https://tieba.baidu.com/p/' + str(raw_input(u'https://tieba.baidu.com/p/'))
seeLZ =  raw_input("是否只获取楼主发言，是输入1，否输入0\n")
print(seeLZ)

bdtb = tieba(baseURL,seeLZ)
print('abccc',baseURL,seeLZ)
bdtb.start()
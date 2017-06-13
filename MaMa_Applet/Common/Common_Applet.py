# -*- coding: utf-8 -*-
import requests
import json
import re
__author__ = 'leo'
class Applet_Driver(object):
    def __init__(self):
        pass



    def result_json(self,result):
        """
        将json解析成python的数据类型,以特定的格式输出，且处理中文显示问题
        """
        try:
            js = json.loads(result)#将json解析成python的数据类型
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10)) #转化为json，以特定的格式输出，且处理中文显示问题
            return js
        except:
            print (result)


    def Post_data(self,test_data,url,headers=None):
        """
        Post请求的方法
        """
        if headers==None:
            r=requests.post(url, params=test_data)
            result=r.text
            js=self.result_json(result)
        else:
            r=requests.post(url, params=test_data,headers=headers)
            result=r.text
            js=self.result_json(result)
        return js


    def Get_data(self,test_data,url,headers=None):
        """
        Get请求的方法
        """
        if headers==None:
            r=requests.get(url, params=test_data)
            result=r.text
            js=self.result_json(result)
        else:
            r=requests.get(url, params=test_data,headers=headers)
            result=r.text
            js=self.result_json(result)
        return js


    def parse_data(self,test_data,regular_data):
        """
        从输出结果的json中提取需要的内容，其中regular_data为正则表达式
        如regular_data='.+order_status:(.+?\d+),?.*'
        处理json的特殊字符test_data.replac可以写多一点
        """
        test_data=json.dumps(test_data)
        test_data = test_data.replace("\\", "")
        test_data = test_data.replace("\"", "")
        test_data = test_data.replace("\'", "")
        data=re.compile(regular_data).findall(test_data)
        if data[0]==None:
            print 'The data correspond to the requirement dont exist.'
        else:
            datas=data[0]
            datas=datas.replace("\\n", "")
            datas=datas.replace(" ", "")
            return datas

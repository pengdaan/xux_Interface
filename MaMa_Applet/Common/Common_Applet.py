# -*- coding: utf-8 -*-
import requests
import json
import re
import MaMa_Applet.Common.DBConns
import pickle
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
        test_data=json.dumps(test_data,ensure_ascii=False)#防止输出中文转换成Ascii 编号
        test_data = test_data.replace("\\", "")
        test_data = test_data.replace("\"", "")
        test_data = test_data.replace("\'", "")
        data=re.compile(regular_data).findall(test_data)
        if data==[]:
            print 'The data correspond to the requirement dont exist.'
        else:
            datas=data[0]
            datas=datas.replace("\\n", "")
            datas=datas.replace(" ", "")
            datas =datas.replace("}", "")
            datas =datas.replace(",", "")
            return datas

    def Limit_data(self,sql_data,send_data):
        data=sql_data
        mysql = MaMa_Applet.Common.DBConns.Mysql()
        datas=mysql.get_one(data)
        if send_data in datas:
            return datas[send_data]
        else:
            return 'The data does not exist'


    def store(self,data_name,data,model):
        '''持久化保存'''
        test={data_name:data}
        path='/xux_project/MaMa_Applet/Run_data/'
        filename=path +'data_%s.pkl'% model
        output=open(filename,'wb')
        pickle.dump(test,output)


    def load(self,value,model):
        path='/xux_project/MaMa_Applet/Run_data/'
        filename=path +'data_%s.pkl'% model
        pkl_file=open(filename,'rb')
        data=pickle.load(pkl_file)[value]
        pkl_file.close()
        print data
        return data

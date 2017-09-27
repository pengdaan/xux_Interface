# -*- coding: utf-8 -*-
__author__ = 'leo'
import sys
import pickle
sys.path.append('..')
import re
import hashlib
import XSX_InTerFace.Setting.DBConns
import XSX_InTerFace.Setting.SupplierDBConns
import requests
import json
import time
times= int(time.time())
class XsxDriver(object):
    def __init__(self):
        pass



    def checkapi_key(self,test_data):
        """
        判断test_data里面api_Key是否存在
        """

        test_data=json.loads(test_data)
        if isinstance(test_data,dict):
            api_key=test_data.get('api_key')
            return api_key
        else:
            print(u"api_key 不存在，请检查接口数据！")
            return None


    def checkapi_secret(self,test_data):

        """
        通过api_key查询，判断secret是否存在
        """
        api_key=self.checkapi_key(test_data)
        Api_key = "SELECT * FROM mall_app WHERE api_key='%s'"%api_key
        api_secret = "SELECT api_secret FROM mall_app WHERE api_key='%s'"%api_key
        mysql = XSX_InTerFace.Setting.DBConns.Mysql()
        datas=mysql.get_all(Api_key)
        if (datas!= None):
            data=mysql.get_one(api_secret)
            return data['api_secret']
        else:
            print 'api_key不存在'



    def api_signs(self,test_data,api_secret):

        """
        生成验签算法
        """
        api_sign=[]
        for (key,value) in test_data.items():
            api_sign.append( key +str(value))
        #获取所有键值对，并升序排列
        api_sign.sort()
        api_signs = "".join(api_sign)
        pj=api_secret+api_signs+api_secret
        #对字符串内部的特殊字符进行转义
        pj = pj.replace("\\n", "\n")
        pj = pj.replace("\\r", "\n")
        pj = pj.replace("\\", "")
        #MD5加密
        md5jm= hashlib.new("md5", pj).hexdigest()
        return md5jm.upper()


    def test_datas(self,test_data,api_secret):

        """
        重新组装测试数据，把生成的验签插入TestData
        """
        api_sign=self.api_signs(test_data,api_secret)
        print(api_sign)
        test_data.setdefault('api_sign',api_sign)
        return test_data



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


    def send_data(self,test_data,url,api_secret):
        test_data=self.test_datas(test_data,api_secret)
        #print test_data
        r=requests.post(url, params=test_data)
        result=r.text
        js=self.result_json(result)
        return js


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


    def parse_data(self,test_data,regular_data):
        """
        从输出结果的json中提取需要的内容，其中regular_data为正则表达式
        如regular_data='.+order_status:(.+?\d+),?.*'
        处理json的特殊字符test_data.replac可以写多一点
        """
        print(test_data)
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


    def Updatexux_Order(self,XUXorder):
        """
        通过修改数据库更改订单状态为已审核状态，只能改普通的直邮订单
        """
        XUXorders = "UPDATE mall_order_info SET order_status='1',order_amount='0',confirm_time='%(time)s' WHERE order_sn='%(XUX_OrderApi)s'"%{'time':times,"XUX_OrderApi":XUXorder}
        mysql = XSX_InTerFace.Setting.DBConns.Mysql()
        mysql.get_one(XUXorders)
        mysql.commit()

    def Limit_data(self,sql_data,send_data):
        data=sql_data
        mysql = XSX_InTerFace.Setting.DBConns.Mysql()
        datas=mysql.get_one(data)
        if send_data in datas:
            return datas[send_data]
        else:
            return 'The data does not exist'


    def Supplier_data(self,sql_data,send_data):
        data=sql_data
        mysql = XSX_InTerFace.Setting.SupplierDBConns.Mysql()
        datas=mysql.get_one(data)
        if send_data in datas:
            return datas[send_data]
        else:
            return 'The data does not exist'


    def Limit_Title(self):
        data="SELECT * FROM mall_promotion_info ORDER BY id DESC LIMIT 1"
        mysql = XSX_InTerFace.Setting.DBConns.Mysql()
        datas=mysql.get_one(data)
        mysql.commit()
        return datas['title']


    def store(self,data_name,data,model,status=None):
        '''持久化保存'''
        if status==None:
            test={data_name:data}
            path='/xux_project/XSX_InTerFace/Run_data/'
            filename=path +'data_%s.pkl'% model
            output=open(filename,'wb')
            pickle.dump(test,output)
        elif status==1:
            test=data
            path='/xux_project/XSX_InTerFace/Run_data/'
            filename=path +'data_%s.pkl'% model
            output=open(filename,'wb')
            pickle.dump(test,output)


    def load(self,value,model,status=None):
        path='/xux_project/XSX_InTerFace/Run_data/'
        filename=path +'data_%s.pkl'% model
        pkl_file=open(filename,'rb')
        if status==None:
            data=pickle.load(pkl_file)[value]
            pkl_file.close()
            return data
        elif status==1and value==None:
            data=pickle.load(pkl_file)
            pkl_file.close()
            return data

    def addWord(self,theIndex,word,pagenumber):
        theIndex.setdefault(word, []).append(pagenumber)












































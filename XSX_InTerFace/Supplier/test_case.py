# -*- coding: utf-8 -*-
__author__ = 'leo'
import json
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''获得当前文件（比如配置文件）所在的路径'''
sys.path.insert(0,parentdir)
import time
import test_data
import XSX_InTerFace.Common.All_secrets
import XSX_InTerFace.Supplier.interface_Supplier
import XSX_InTerFace.Common.XSX_Driver
times= int(time.time())

class Test(XSX_InTerFace.Supplier.interface_Supplier.MyTest):
    '''商家中心接口'''

    def test_Register_sucess(self):
        '''创建供应商'''
        Register=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets= XSX_InTerFace.Common.All_secrets.supplier_secrets
        Registers=test_data.register_data()
        Register.store(data_name='Update_data',data=Registers,model='Supplier',status=1)
        Registers=Register.send_data(Registers,self.registerUrl,api_secret=api_secrets)
        self.msgs=Register.parse_data(Registers,regular_data='.+msg:(.+?\d+),?.*')

    def test_update_sucess(self):
        '''更新供应商'''
        Register=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets= XSX_InTerFace.Common.All_secrets.supplier_secrets
        Test_data=Register.load(value=None,model='Supplier',status=1)
        userName=Register.parse_data(Test_data,regular_data='.+userName:(.+?_\d+)')
        data="select * from SuppUser where userName='%s'"%userName
        #id=Register.Supplier_data(sql_data=data,send_data='id')
        id=1354
        d='"uid":"1354"'
        Register.addWord(Test_data,'data',d)


        # Test_data['data'].setdefault("uid",str(id))
        # print type(Test_data)
        print Test_data
        Registers=Test_data
        Registers={'timestamp': 1500458475, 'api_key': '091e63850fce13f7bee3774c92e0c9e5', 'data': '{"catId":17,"groupId":9,"userName":"Test_DP01_20332","signatoryId":2,"merchantsOfficial":"test","confirmStatus":1,"confirmReason":"","payMethodId":2,"depositStatus":3,"deposit":"0","billingCycle":"","bank":"u62dbu5546u94f6u884c","bankAccount":"6222023602080752132","bankUserName":"Test","returnContacts":"Tesst","returnMobile":"13800138000","callNo":"","returnAddress":"Test_Adress","province":19,"city":307,"district":3146,"zipCode":"","contacts":"Test","mobile":"13800138000","email":"","address":"","businesScope":"","remark":"","ip":"192.168.14.37","operatorId":1,"taxpayerNo":"","swiftCode":"","moneyTypeId":142,"alias":"","deliverTimeLimit":0,"delaySettle":0,"userType":0,"commissionList":[{"rate":"9","goodsCatId":"0","brandId":"0","catLevel":0}],"billingDays":"1","uid": "1354"}'}
        print Registers
        Registers=Register.send_data(Registers,self.updatUrl,api_secret=api_secrets)
        self.msgs=Register.parse_data(Registers,regular_data='.+msg:(.+?\d+),?.*')
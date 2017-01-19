# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,json,time
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import interface_ly

times= int(time.time())

class Test(interface_ly.MyTest):

    '''旅游接口'''
    def test_OrderBySnTour_sucess(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_key=setting.DBConns.Api_secret(**test_data.test_OrderBySnTour)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.test_OrderBySnTour
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderBySnTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderByGoTime_sucess(self):
        '''旅游通过出行日期查询已支付的订单接口检查'''
        api_key=setting.DBConns.Api_secret(**test_data.test_OrderByGoTime)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.test_OrderByGoTime
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderByGoTime_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_UserOrderListTour_success(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_key=setting.DBConns.Api_secret(**test_data.test_UserOrderListTour)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.test_UserOrderListTour
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderListTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)

                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'

            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_UserOrderNums_sucess(self):
        '''旅游根据订单分类获取分类订单总数接口检查'''
        api_key=setting.DBConns.Api_secret(**test_data.test_UserOrderNums)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.test_UserOrderNums
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderNums_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")



if __name__=='__main__':
    unittest.main()





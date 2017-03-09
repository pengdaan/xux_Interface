# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests, time
import setting.api_signs
import setting.result_jsons
import setting.DBConns
from order import test_data
from order import interface_order
import common.common_Order
import common.common_data
times= int(time.time())

class Test(interface_order.MyTest):

    def test_UserLimitedSpecialOrderNum_sucess(self):
        '''获取用户商品下单商品数量'''
        api_key=setting.DBConns.Api_secret(**test_data.UserLimitedSpecialOrderNum_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.UserLimitedSpecialOrderNum_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserLimitedSpecialOrderNum_url, params=payload)
              #  print payload
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


    def test_OrderGoodsNumTour_sucess(self):
        '''获取用户购买的商品数量'''
        api_key=setting.DBConns.Api_secret(**test_data.OrderGoodsNumTour_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.OrderGoodsNumTour_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderGoodsNumTour_url, params=payload)
              #  print payload
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


    def test_receiveOrderReturn_sucess(self):#现在这个没有调通
        '''接收open域回推要出发订单信息'''
        api_key=setting.DBConns.Api_secret(**test_data.receiveOrderReturn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.receiveOrderReturn_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.receiveOrderReturn_url, params=payload)
              #  print payload
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


    def test_createOrderXsx_sucess(self):
        '''小树熊下单接口'''
        payload= test_data.data_createOrderXsx
        r=requests.post(self.createOrderXsx_url,params=payload)
        #print payload
        self.code=r.status_code
        self.result=r.text
        js=setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'


    def test_OrderBySn_sucess(self):#现在这个没有调通
        '''根据订单号获取订单详情接口'''
        api_key=setting.DBConns.Api_secret(**test_data.OrderBySn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.OrderBySn_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderBySn_url, params=payload)
              #  print payload
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

    def test_normalShip_sucess(self):
        '''订单直接分单发货'''
        order=common.common_Order.order()
        order_sns=order.updatePayDPStatu(status=3)
        order.Updatexux_Order(order_sns)#更新订单状态为已审核
        payloads=test_data.normalShip_data
        payloads.setdefault('order_sn',order_sns)
       # print payloads
        api_key=setting.DBConns.Api_secret(**test_data.normalShip_data)#返回api_key

        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.normalShip_url, params=payload)
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





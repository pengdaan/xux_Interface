# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,time
import test_data
import xux_Interface.setting.api_signs
import xux_Interface.setting.result_jsons
import xux_Interface.setting.DBConns
import interface_dp
import xux_Interface.common.common_Order
import xux_Interface.common.common_data

times= int(time.time())

class Test(interface_dp.MyTest):

    '''点评接口'''
    def test_post_orderDP_sucess(self):
        '''创建点评订单接口检查'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.data_OrderDPSuces)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.data_OrderDPSuces
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.orderDP_url, params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                        order_dp= xux_Interface.setting.result_jsons.DP_order(self.result)
                        print order_dp

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_UserOrderListDP_sucess(self):
        '''获取用户订单列表-点评项目'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.data_UserOrderListDP)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.data_UserOrderListDP
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderListDP_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_cancelOrder_sucess(self):
        '''取消订单-点评'''
        payloads= test_data.cancelOrder_data
        #order_sns=create_data.post_orderDP()#生成订单号
        order= xux_Interface.common.common_Order.order()
        order_sns=order.orderDP(order_data=xux_Interface.common.common_data.data_OrderDPSuces)
        print order_sns
        payloads.setdefault('order_sn',order_sns) #插入订单号
        #print payloads
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.cancelOrder_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)

                r=requests.post(self.cancelOrder_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_applyRefund_sucess(self):
        '''取用户申请退款-点评项目'''
        payloads= test_data.applyRefund_data
        order= xux_Interface.common.common_Order.order()
        order_sns=order.orderDP(order_data=xux_Interface.common.common_data.data_OrderDPSuce)
        order.updatePayDPStatu(status=2,DP_order=order_sns)
        payloads.setdefault('order_sn',order_sns) #插入订单号
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.applyRefund_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
               # print payload
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.applyRefund_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_OrderBySnDianping_sucess(self):
        '''获取订单详情-点评项目'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.OrderBySnDianping_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.OrderBySnDianping_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderBySnDianping_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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





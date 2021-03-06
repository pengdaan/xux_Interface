# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,time
import test_data
import  xux_Interface.setting.api_signs
import  xux_Interface.setting.result_jsons
import  xux_Interface.setting.DBConns
import interface_www
import  xux_Interface.all_secrets

times= int(time.time())

class Test(interface_www.MyTest):

    '''www接口'''
    def test_PromotionNums_sucess(self):
        '''获取秒杀订单实际秒杀购买数'''
        api_key=  xux_Interface.setting.DBConns.Api_secret(**test_data.PromotionNums_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.PromotionNums_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PromotionNums_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_updateRemindMsg_sucess(self):
        '''更新订单客服留言接口'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.updateRemindMsg_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.updateRemindMsg_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updateRemindMsg_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_RemindMsg_sucess(self):
        '''获取订单客服留言接口'''
        api_key=  xux_Interface.setting.DBConns.Api_secret(**test_data.RemindMsg_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.RemindMsg_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.RemindMsg_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_createOrderTour_sucess(self):
        '''旅游创建订单'''
        api_key=  xux_Interface.setting.DBConns.Api_secret(**test_data.createOrderTour_data)#返回api_key
        print api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.createOrderTour_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.createOrderTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_OutOrderSn_sucess(self):
        '''对接要出发回调设置外部订单号'''
        api_key=  xux_Interface.setting.DBConns.Api_secret(**test_data.OutOrderSn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.OutOrderSn_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OutOrderSn_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_ChildOrderTour_sucess(self):
        '''根据订单号获取订单列表'''
        api_key=  xux_Interface.setting.DBConns.Api_secret(**test_data.ChildOrderTour_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=  xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.ChildOrderTour_data
                api_sign=  xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.ChildOrderTour_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=  xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'SUCCESS')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_query_sucess(self):
        '''获取用户购买的商品数量'''
        api_key=xux_Interface.setting.DBConns.Api_secret(**test_data.query_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.query_data
                api_sign=xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.query_url, params=payload)
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


    def test_CouponCode_sucess(self):
        '''获取用户购买的商品数量'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.CouponCode_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.CouponCode_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.ByCouponCode_url, params=payload)
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


    def test_updatePayStatus_sucess(self):
        '''更新订单支付状态更新订单支付状态'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.data_updatePayStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.data_updatePayStatus
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updatePayStatus_url, params=payload)
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


    def test_OrderByProductId_sucess(self):
        '''通过商品id获取订单列表'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.data_OrderByProductId)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.data_OrderByProductId
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderByProductId_url, params=payload)
                print payload
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

    def test_UserOrderNums_sucess(self):
        '''根据订单分类获取分类订单总数'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.UserOrderNums_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.UserOrderNums_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.UserOrderNums_url, params=payload)
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


    def test_De_AllStatus_sucess(self):
        '''获取所有的发货单状态'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.De_AllStatus_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.De_AllStatus_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.de_AllStatus_url, params=payload)
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

    def test_AllStatus_sucess(self):
        '''获取所有的订单状态（综合状态）'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.AllStatus_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.AllStatus_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.AllStatus_url, params=payload)
                #print payload
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


    def test_OrderPromotionList_sucess(self):
        '''获取用户购买的促销订单信息'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.OrderPromotionList_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.OrderPromotionList_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.OrderPromotionList_url, params=payload)
                #print payload
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


    def test_G_dingdan_sucess(self):
        '''获取订单来源参数列表'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.G_dingdan_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.G_dingdan_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.G_dingdan_url, params=payload)
                #print payload
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


    def test_ProductId_sucess(self):
        '''通过商品id获取订单列表'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.ProductId_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.ProductId_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.ProductId_url, params=payload)
                #print payload
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

    def test_verify_sucess(self):
        '''验证使用消费券'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.verify_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.verify_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.verify_url, params=payload)
                #print payload
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

    def test_ship_sucess(self):
        '''发送消费券'''
        api_secrets= xux_Interface.all_secrets.www_secrets
        payload= test_data.ship_data()
        api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(self.ship_url, params=payload)
        print payload,'入参'
        self.code=r.status_code
        self.result=r.text
        js= xux_Interface.setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'

    def test_add_XUJ_sucess(self):
        '''重复发送消费券接口'''
        api_secrets=xux_Interface.all_secrets.www_secrets
        add_Tdata= test_data.add_data()
        add_data=add_Tdata[0]
        ship_data=add_Tdata[1]
        print add_data
        print ship_data
        api_sign= xux_Interface.setting.api_signs.api_signs(add_data,api_secrets)
        api_sign_ship= xux_Interface.setting.api_signs.api_signs(ship_data,api_secrets)
        add_data.setdefault('api_sign',api_sign)
        ship_data.setdefault('api_sign',api_sign_ship)
        requests.post(self.ship_url, params=ship_data)
        r=requests.post(self.add_XUJ_url, params=add_data)
        print add_data,'重复发送消费券接口'
        self.code=r.status_code
        self.result=r.text
        js= xux_Interface.setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'


    def test_hipWithoutCoupon_sucess(self):
        '''不输入消费券直接发货'''
        api_secrets= xux_Interface.all_secrets.www_secrets
        payload= test_data.shipw_data()
        print payload
        api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(self.shipWithoutCoupon_url, params=payload)
        print payload,'不输入消费券直接发货'
        self.code=r.status_code
        self.result=r.text
        js= xux_Interface.setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'

    def test_getStock_sucess(self):
        '''获取单个商品的库存'''
        api_secrets= xux_Interface.all_secrets.open_secrets
        payload= test_data.getStock
        api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(self.getStocks_url, params=payload)
        print payload
        self.code=r.status_code
        self.result=r.text
        js= xux_Interface.setting.result_jsons.result_json(self.result)
        if js.has_key('msg')==True:
            self.msgs=js.get('msg')
            self.assertEquals(self.code,200)
            self.assertEqual(self.msgs, 'SUCCESS')
        else:
            print 'NO msg'


    def test_BatchSn_sucess(self):
        '''订单发货获取减库存批次接口'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.BatchSn_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.BatchSn_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.InventoryBatchSn_url, params=payload)
                #print payload
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





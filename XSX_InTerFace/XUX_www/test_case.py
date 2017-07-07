# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import XSX_InTerFace.Setting.api_signs
import XSX_InTerFace.Setting.result_jsons
import XSX_InTerFace.Setting.DBConns
import interface_www
import XSX_InTerFace.Common.All_secrets
import requests, time
import test_data
import XSX_InTerFace.Common.All_secrets
import XSX_InTerFace.Common.XSX_Driver

times= int(time.time())

class Test(interface_www.MyTest):

    '''www接口'''
    def test_PromotionNums_sucess(self):
        '''获取秒杀订单实际秒杀购买数'''
        PromotionNums=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Test_data=test_data.PromotionNums_data
        PromotionNums.send_data(Test_data,self.PromotionNums_url,api_secrets)


    def test_updateRemindMsg_sucess(self):
        '''更新订单客服留言接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        UpdateRemindMsg=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.updateRemindMsg_data
        UpdateRemindMsg.send_data(Test_data,self.updateRemindMsg_url,api_secrets)

    def test_RemindMsg_sucess(self):
        '''获取订单客服留言接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        RemindMsg=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.RemindMsg_data
        RemindMsg.send_data(Test_data,self.RemindMsg_url,api_secrets)

    def test_createOrderTour_sucess(self):
        '''旅游创建订单'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        CreateOrderTour=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.createOrderTour_data
        CreateOrderTour.send_data(Test_data,self.createOrderTour_url,api_secrets)


    def test_OutOrderSn_sucess(self):
        '''对接要出发回调设置外部订单号'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        OutOrderSn=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        CreateOrderTour=test_data.createOrderTour_data
        datas=OutOrderSn.send_data(CreateOrderTour,self.createOrderTour_url,api_secrets)
        Order_sn=OutOrderSn.parse_data(datas,regular_data='.+order_sn:(.+?\d+),?.*')
        Test_data=test_data.OutOrderSn_data(Order_sn)
        OutOrderSn.send_data(Test_data,self.OutOrderSn_url,api_secrets)

    def test_ChildOrderTour_sucess(self):
        '''根据订单号获取订单列表'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        ChildOrderTour=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.ChildOrderTour_data
        ChildOrderTour.send_data(Test_data,self.ChildOrderTour_url,api_secrets)

    def test_updatePayStatus_sucess(self):
        '''更新订单支付状态'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Test_data=test_data.data_createOrderXsx
        UpdatePayStatus=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        result=requests.post(self.createOrderXsx_url,params=Test_data)
        Data_Order_sn=UpdatePayStatus.result_json(result.text)
        Order_sn=UpdatePayStatus.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=UpdatePayStatus.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus=test_data.data_updatePayStatus(Order_sn,Order_amount)
        UpdatePayStatus.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)


    def test_OrderByProductId_sucess(self):
        '''通过商品id获取订单列表'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        OrderByProductId=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.data_OrderByProductId
        OrderByProductId.send_data(Test_data,self.OrderByProductId_url,api_secrets)


    def test_UserOrderNums_sucess(self):
        '''根据订单分类获取分类订单总数'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        UserOrderNums=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data= test_data.UserOrderNums_data
        UserOrderNums.send_data(Test_data,self.UserOrderNums_url,api_secrets)



    def test_OrderPromotionList_sucess(self):
        '''获取用户购买的促销订单信息'''
        api_secrets=XSX_InTerFace.Common.All_secrets.www_secrets
        OrderPromotionList=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.OrderPromotionList_data
        OrderPromotionList.send_data(Test_data,self.OrderPromotionList_url,api_secrets)



    def test_G_dingdan_sucess(self):
        '''获取订单来源参数列表'''
        api_secrets=XSX_InTerFace.Common.All_secrets.www_secrets
        Test_data=test_data.G_dingdan_data
        G_dingdan=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        G_dingdan.send_data(Test_data,self.G_dingdan_url,api_secrets)



    def test_getStock_sucess(self):
        '''获取单个商品的库存'''
        GetStock=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Test_data=test_data.getStock
        GetStock.send_data(Test_data,self.getStocks_url,api_secrets)


    def test_ship_sucess(self):
        '''输入消费券发货'''
        Send_ship=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Creata_ly=test_data.createOrderTour_data
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Data_Order_sn=Send_ship.send_data(Creata_ly,self.createOrderTour_url,api_secrets)
        Order_id=Send_ship.parse_data(Data_Order_sn,regular_data='.+order_id:(.+?\d+),?.*')
        Order_sn=Send_ship.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=Send_ship.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus=test_data.data_updatePayStatus(Order_sn,Order_amount)
        Send_ship.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        coupon=test_data.couponId()
        Test_data=test_data.ship_data(Order_id,coupon)
        Send_ship.send_data(Test_data,self.ship_url,api_secrets)



    def test_add_XUJ_sucess(self):
        '''重复发送消费券接口'''
        Add_Sendship=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Creata_ly=test_data.createOrderTour_data
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Data_Order_sn=Add_Sendship.send_data(Creata_ly,self.createOrderTour_url,api_secrets)
        Order_id=Add_Sendship.parse_data(Data_Order_sn,regular_data='.+order_id:(.+?\d+),?.*')
        Order_sn=Add_Sendship.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=Add_Sendship.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus=test_data.data_updatePayStatus(Order_sn,Order_amount)
        Add_Sendship.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        coupon=test_data.couponId()
        Test_data=test_data.ship_data(Order_id,coupon)
        Add_Sendship.send_data(Test_data,self.ship_url,api_secrets)
        Add_send_data=test_data.Add_XUJ_data(Order_id)
        Add_Sendship.send_data(Add_send_data,self.add_XUJ_url,api_secrets)



    def test_hipWithoutCoupon_sucess(self):
        '''不输入消费券直接发货'''
        HipWithoutCoupon=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Creata_ly=test_data.createOrderTour_data
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Data_Order_sn=HipWithoutCoupon.send_data(Creata_ly,self.createOrderTour_url,api_secrets)
        Order_id=HipWithoutCoupon.parse_data(Data_Order_sn,regular_data='.+order_id:(.+?\d+),?.*')
        Order_sn=HipWithoutCoupon.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=HipWithoutCoupon.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus=test_data.data_updatePayStatus(Order_sn,Order_amount)
        HipWithoutCoupon.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        Test_data=test_data.ShipWithoutCoupon_data(Order_sn,Order_id)
        HipWithoutCoupon.send_data(Test_data,self.shipWithoutCoupon_url,api_secrets)



    def test_verify_sucess(self):
        '''验证使用消费券'''
        Verify_ship=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Creata_ly=test_data.createOrderTour_data
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Data_Order_sn=Verify_ship.send_data(Creata_ly,self.createOrderTour_url,api_secrets)
        Order_id=Verify_ship.parse_data(Data_Order_sn,regular_data='.+order_id:(.+?\d+),?.*')
        Order_sn=Verify_ship.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=Verify_ship.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus=test_data.data_updatePayStatus(Order_sn,Order_amount)
        Verify_ship.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        coupon=test_data.couponId()
        Test_data=test_data.ship_data(Order_id,coupon)
        Verify_ship.send_data(Test_data,self.ship_url,api_secrets)
        Verify_data=test_data.verify_data(Order_sn,coupon)
        Verify_ship.send_data(Verify_data,self.verify_url,api_secrets)


    def test_KJ_data_sucess(self):
        '''模拟科捷回推数据到open'''
        Kj_data=test_data.test_data
        KJurl=self.KJ_Url+Kj_data
        r=requests.post(KJurl)
        print r.text








if __name__=='__main__':
    unittest.main()





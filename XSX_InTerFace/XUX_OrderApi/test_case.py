# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests, time
from XSX_InTerFace.XUX_OrderApi import interface_order
import test_data
import XSX_InTerFace.Common.All_secrets
import XSX_InTerFace.Common.XSX_Driver
times= int(time.time())

class Test(interface_order.MyTest):


    def test_UserLimitedSpecialOrderNum_sucess(self):
        '''获取用户商品下单商品数量'''
        api_secrets=XSX_InTerFace.Common.All_secrets.dp_secrets
        Test_data=test_data.UserLimitedSpecialOrderNum_data
        UserLimitedSpecialOrder=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        UserLimitedSpecialOrder.send_data(Test_data,self.UserLimitedSpecialOrderNum_url,api_secret=api_secrets)


    def test_OrderGoodsNumTour_sucess(self):
        '''获取用户购买的商品数量'''
        api_secrets=XSX_InTerFace.Common.All_secrets.dp_secrets
        Test_data=test_data.OrderGoodsNumTour_data
        OrderGoodsNumTours=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        OrderGoodsNumTours.send_data(Test_data,self.OrderGoodsNumTour_url,api_secrets)


    def test_receiveOrderReturn_sucess(self):
        '''接收open域回推要出发订单信息'''
        api_secrets=XSX_InTerFace.Common.All_secrets.www_secrets
        Test_data=test_data.receiveOrderReturn_data
        receiveOrder=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        receiveOrder.send_data(Test_data,self.receiveOrderReturn_url,api_secrets)


    def test_createOrderXsx_sucess(self):
        '''小树熊下单接口'''
        Test_data=test_data.data_createOrderXsx
        CreateOrder=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        result=requests.post(self.createOrderXsx_url,params=Test_data)
        results=CreateOrder.result_json(result.text)
        Order_sn=CreateOrder.parse_data(results,regular_data='.+order_sn:(.+?\d+),?.*')
        print Order_sn
        CreateOrder.store(data_name='Order_sn',data=Order_sn,model='Order_sn')
        CreateOrder.load(value='Order_sn',model='Order_sn')


    def test_OrderBySn_sucess(self):
        '''根据订单号获取订单详情接口'''
        Test_data=test_data.OrderBySn_data
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        OrderBySns=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        OrderBySns.send_data(Test_data,self.OrderBySn_url,api_secrets)



    def test_normalShip_sucess(self):
        '''订单直接分单发货'''
        api_secrets=XSX_InTerFace.Common.All_secrets.update_dpStatus
        Test_data=test_data.data_createOrderXsx
        Data_updatePayStatus=test_data.data_updatePayStatus
        NormalShip=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        result=requests.post(self.createOrderXsx_url,params=Test_data)
        Data_Order_sn=NormalShip.result_json(result.text)
        Order_sn=NormalShip.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=NormalShip.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus.setdefault('order_sn',Order_sn)
        Data_updatePayStatus.setdefault('order_amount',Order_amount)
        NormalShip.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        NormalShip.Updatexux_Order(Order_sn)#更新订单状态为已审核
        Data_NormalShip=test_data.normalShip_data
        Data_NormalShip.setdefault('order_sn',Order_sn)
        print Data_NormalShip
        NormalShip.send_data(Data_NormalShip,self.normalShip_url,api_secrets)




if __name__=='__main__':
    unittest.main()





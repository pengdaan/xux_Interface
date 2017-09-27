# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests, time
from XSX_InTerFace.XUX_OrderApi import interface_order
from XSX_InTerFace.XUX_OrderApi import test_data
from XSX_InTerFace.Common import XSX_Driver
from XSX_InTerFace.Common import All_secrets
times= int(time.time())
Driver=XSX_Driver.XsxDriver()
class Test(interface_order.MyTest):


    def test_UserLimitedSpecialOrderNum_sucess(self):
        '''获取用户商品下单商品数量'''
        api_secrets=All_secrets.dp_secrets
        Test_data=test_data.UserLimitedSpecialOrderNum_data
        Driver.send_data(Test_data,self.UserLimitedSpecialOrderNum_url,api_secret=api_secrets)


    def test_OrderGoodsNumTour_sucess(self):
        '''获取用户购买的商品数量'''
        api_secrets=All_secrets.dp_secrets
        Test_data=test_data.OrderGoodsNumTour_data
        Driver.send_data(Test_data,self.OrderGoodsNumTour_url,api_secrets)


    def test_receiveOrderReturn_sucess(self):
        '''接收open域回推要出发订单信息'''
        api_secrets=All_secrets.www_secrets
        Test_data=test_data.receiveOrderReturn_data
        Driver.send_data(Test_data,self.receiveOrderReturn_url,api_secrets)


    def test_createOrderXsx_sucess(self):
        '''小树熊下单接口'''
        Test_data=test_data.data_createOrderXsx
        result=requests.post(self.createOrderXsx_url,params=Test_data)
        results=Driver.result_json(result.text)
        Order_sn=Driver.parse_data(results,regular_data='.+order_sn:(.+?\d+),?.*')
        print Order_sn
        Driver.store(data_name='Order_sn',data=Order_sn,model='Order_sn')
        Driver.load(value='Order_sn',model='Order_sn')


    def test_OrderBySn_sucess(self):
        '''根据订单号获取订单详情接口'''
        Test_data=test_data.OrderBySn_data
        api_secrets=All_secrets.update_dpStatus
        Driver.send_data(Test_data,self.OrderBySn_url,api_secrets)



    def test_normalShip_sucess(self):
        '''订单直接分单发货'''
        api_secrets=All_secrets.update_dpStatus
        Test_data=test_data.data_createOrderXsx
        Data_updatePayStatus=test_data.data_updatePayStatus
        result=requests.post(self.createOrderXsx_url,params=Test_data)
        Data_Order_sn=Driver.result_json(result.text)
        Order_sn=Driver.parse_data(Data_Order_sn,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=Driver.parse_data(Data_Order_sn,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus.setdefault('order_sn',Order_sn)
        Data_updatePayStatus.setdefault('order_amount',Order_amount)
        Driver.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secrets)
        Driver.Updatexux_Order(Order_sn)#更新订单状态为已审核
        Data_NormalShip=test_data.normalShip_data
        Data_NormalShip.setdefault('order_sn',Order_sn)
        print Data_NormalShip
        Driver.send_data(Data_NormalShip,self.normalShip_url,api_secrets)




if __name__=='__main__':
    unittest.main()





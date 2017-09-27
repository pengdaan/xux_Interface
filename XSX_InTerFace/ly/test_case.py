# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''获得当前文件（比如配置文件）所在的路径'''
sys.path.insert(0,parentdir)
import time
import test_data
from XSX_InTerFace.Common import All_secrets
from XSX_InTerFace.Common import XSX_Driver
times= int(time.time())
import interface_ly
Driver=XSX_Driver.XsxDriver()

class Test(interface_ly.MyTest):

    '''旅游接口'''
    def test_OrderBySnTour_sucess(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_secrets=All_secrets.dp_secrets
        Driver.send_data(test_data.test_OrderBySnTour,self.OrderBySnTour_url,api_secret=api_secrets)


    def test_OrderByGoTime_sucess(self):
        '''旅游通过出行日期查询已支付的订单接口检查'''
        api_secrets=All_secrets.dp_secrets
        Data_OrderByGoTime=test_data.test_OrderByGoTime
        Driver.send_data(Data_OrderByGoTime,self.OrderByGoTime_url,api_secret=api_secrets)



    def test_UserOrderListTour_success(self):
        '''旅游获取用户所有的订单列表接口检查'''
        api_secrets=All_secrets.dp_secrets
        Data_UserOrderLists=test_data.test_UserOrderListTour
        Driver.send_data(Data_UserOrderLists,self.UserOrderListTour_url,api_secret=api_secrets)


    def test_UserOrderNums_sucess(self):
        '''旅游根据订单分类获取分类订单总数接口检查'''
        api_secrets=All_secrets.dp_secrets
        Data_UserOrderNums=test_data.test_UserOrderNums
        Driver.send_data(Data_UserOrderNums,self.UserOrderNums_url,api_secret=api_secrets)



if __name__=='__main__':
    unittest.main()





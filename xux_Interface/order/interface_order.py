# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):

        #order接口
        self.applyRefund_url='http://order.api.xiaoshuxiong.com/order/applyRefund'
        self.create_url='http://order.api.xiaoshuxiong.com/order/create'
        self.createOrderXsx_url='http://order.api.xiaoshuxiong.com/Order/createOrderXsx '
        self.UserLimitedSpecialOrderNum_url='http://order.api.xiaoshuxiong.com/order/getUserLimitedSpecialOrderNum'
        self.receiveOrderReturn_url='http://order.api.xiaoshuxiong.com/order/receiveOrderReturn'
        self.OrderGoodsNumTour_url='http://order.api.xiaoshuxiong.com/order/getOrderGoodsNumTour'
        self.OrderBySn_url='http://order.api.xiaoshuxiong.com/order/getOrderBySn'
        self.normalShip_url='http://order.api.xiaoshuxiong.com/delivery/normalShip'


    def tearDown(self):
       # pass

        print(self.code,self.msgs)

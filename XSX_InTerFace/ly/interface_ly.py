# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''旅游相关接口'''

        self.OrderBySnTour_url ="http://www.xiaoshuxiong.com/api/order/getOrderBySnTour"
        self.OrderByGoTime_url='http://www.xiaoshuxiong.com/api/order/getOrderByGoTime'
        self.UserOrderListTour_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListTour'
        self.UserOrderNums_url='http://www.xiaoshuxiong.com/api/order/getUserOrderNums'


    def tearDown(self):
        pass

        #print(self.code,self.msgs)

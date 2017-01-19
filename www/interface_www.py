# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):

        #www域接口
        self.PromotionNums_url='http://www.xiaoshuxiong.com/api/order/getPromotionNums'
        self.updateRemindMsg_url='http://www.xiaoshuxiong.com/api/order/updateRemindMsg'
        self.OrderByProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'
        self.updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
        self.RemindMsg_url='http://www.xiaoshuxiong.com/api/order/getRemindMsg'
        self.createOrderTour_url='http://www.xiaoshuxiong.com/api/order/createOrderTour'
        self.OutOrderSn_url='http://www.xiaoshuxiong.com/api/order/setOutOrderSn'
        self.ChildOrderTour_url='http://www.xiaoshuxiong.com/api/order/getChildOrderTour'
        self.shipWithoutCoupon_url='http://www.xiaoshuxiong.com/api/ocoupon/shipWithoutCoupon'
        self.query_url='http://www.xiaoshuxiong.com/api/delivery/query'
        self.ByCouponCode_url='http://www.xiaoshuxiong.com/api/ocoupon/getByCouponCode'












    def tearDown(self):
       # pass

        print(self.code,self.msgs)

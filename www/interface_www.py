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
        self.UserOrderNums_url='http://www.xiaoshuxiong.com/api/order/getUserOrderNums'
        self.de_AllStatus_url='http://www.xiaoshuxiong.com/api/delivery/getAllStatus'
        self.AllStatus_url='http://www.xiaoshuxiong.com/api/order/getAllStatus'
        self.OrderPromotionList_url='http://order.api.xiaoshuxiong.com/order/getOrderPromotionList'
        self.G_dingdan_url='http://www.xiaoshuxiong.com/api/source/get'
        self.ProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'
        self.add_XUJ_url='http://www.xiaoshuxiong.com/api/ocoupon/add'
        self.verify_url='http://www.xiaoshuxiong.com/api/ocoupon/verify'
        self.ship_url='http://www.xiaoshuxiong.com/api/ocoupon/ship'












    def tearDown(self):
       # pass

        print(self.code,self.msgs)

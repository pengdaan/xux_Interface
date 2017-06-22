# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''点评相关接口'''

        self.orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
        self.DPverify ='http://www.xiaoshuxiong.com/api/ocoupon/verify'#点评验卷接口
        self.UserOrderListDP_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListDianping' #获取用户订单列表-点评项目
        self.cancelOrder_url='http://www.xiaoshuxiong.com/api/order/cancelOrder'
        self.applyRefund_url='http://order.api.xiaoshuxiong.com/order/applyRefund'
        self.OrderBySnDianping_url='http://www.xiaoshuxiong.com/api/order/getOrderBySnDianping'
        self.updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
        self.updateCommentStatusUrl='http://www.xiaoshuxiong.com/api/Reservation/updateCommentStatus'
        self.GoodsByIdsDpUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsByIdsDp'
        self.GoodsByIdsDpUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsByIdsDp'
        self.GoodsByIdsDetailDpUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsByIdsDetailDp'
        self.updateConsumeStatusUrl='http://www.xiaoshuxiong.com/api/Reservation/updateConsumeStatus'
        self.GoodsBySupplierIdDpUrl='http://www.xiaoshuxiong.com/api/goods/getGoodsBySupplierIdDp'



    def tearDown(self):

        print self.msgs

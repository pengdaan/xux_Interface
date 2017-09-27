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
import XSX_InTerFace.Dp.interface_dp
times= int(time.time())
Driver=XSX_Driver.XsxDriver()
class Test(XSX_InTerFace.Dp.interface_dp.MyTest):
    '''点评接口'''

    def test_Create_Order_sucess(self):
        '''创建点评订单'''
        api_secrets=All_secrets.dp_secrets
        Create_Orders= Driver.send_data(test_data.data_OrderDPSuce,self.orderDP_url,api_secret=api_secrets)
        Driver.parse_data(Create_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        self.msgs=Driver.parse_data(Create_Orders,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')


    def test_UserOrderListDP_sucess(self):
        '''获取用户订单列表-点评项目'''
        api_secrets= All_secrets.dp_secrets
        UserOrderListDP_data=Driver.send_data(test_data.data_UserOrderListDP,self.UserOrderListDP_url,api_secret=api_secrets)
        self.msgs=Driver.parse_data(UserOrderListDP_data,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')

    def test_cancelOrder_sucess(self):
        '''取消订单-点评'''
        api_secrets= All_secrets.dp_secrets
        CancelOrders=test_data.cancelOrder_data
        DP_Orders=Driver.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        DP_Order=Driver.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        CancelOrders.setdefault('order_sn',DP_Order)
        CancelOrder_data=Driver.send_data(CancelOrders,self.cancelOrder_url,api_secret=api_secrets)
        self.msgs=Driver.parse_data(CancelOrder_data,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')


    def test_applyRefund_sucess(self):
        '''取用户申请退款-点评项目'''
        api_secrets= All_secrets.dp_secrets
        UP_api_secrets= All_secrets.update_dpStatus
        Data_updatePayStatus=test_data.data_updatePayStatus
        Data_ApplyRefund=test_data.applyRefund_data
        DP_Orders=Driver.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        DP_Order=Driver.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=Driver.parse_data(DP_Orders,regular_data='.+order_amount:(.+?\d+),?.*')
        Data_updatePayStatus.setdefault('order_sn',DP_Order)
        Data_updatePayStatus.setdefault('order_amount',Order_amount)
        Data_ApplyRefund.setdefault('order_sn',DP_Order)
        Data_ApplyRefund.setdefault('order_amount',Order_amount)
        Driver.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secret=UP_api_secrets)
        ApplyRefundOrder_data=Driver.send_data(Data_ApplyRefund,self.applyRefund_url,api_secret=api_secrets)
        self.msgs=Driver.parse_data(ApplyRefundOrder_data,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')


    def test_OrderBySnDp_sucess(self):
        '''获取订单详情-点评项目'''
        api_secrets= All_secrets.dp_secrets
        Data_OrderBySnDp=test_data.OrderBySnDianping_data
        OrderBySnDp_data=Driver.send_data(Data_OrderBySnDp,self.OrderBySnDianping_url,api_secret=api_secrets)
        self.msgs=Driver.parse_data(OrderBySnDp_data,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')


    def test_updateCommentStatus_sucess(self):
        '''点评或旅游--更新评价状态'''
        api_secrets=All_secrets.dp_secrets
        DP_secrets=All_secrets.update_dpStatus
        Create_Orders= Driver.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        order_sn=Driver.parse_data(Create_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        data="SELECT * FROM mall_order_info where order_sn='%s'"%order_sn
        order_id=Driver.Limit_data(data,send_data='order_id')
        CommentStatus_data=test_data.updateCommentStatus(order_id)
        Driver.send_data(CommentStatus_data,self.updateCommentStatusUrl,api_secret=DP_secrets)
        print(CommentStatus_data)
        self.msgs=Driver.parse_data(Create_Orders,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'SUCCESS,code:0')

    def test_GoodsByIdsDp_sucess(self):
        '''点评--批量商品基本信息-列表页'''
        api_secrets= All_secrets.update_dpStatus
        GoodsByIdsDp=test_data.GoodsByIdsDp
        OrderBySnDp_data=Driver.send_data(GoodsByIdsDp,self.GoodsByIdsDpUrl,api_secret=api_secrets)
        self.msgs=Driver.parse_data(OrderBySnDp_data,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'OK,code:200')


    def test_GoodsByIdsDetailDp_sucess(self):
        '''点评--批量商品详细信息-详情页'''
        api_secrets= All_secrets.update_dpStatus
        GoodsByIdsDetailDp=test_data.GoodsByIdsDetailDp
        GoodsByIdsDetailDp=Driver.send_data(GoodsByIdsDetailDp,self.GoodsByIdsDetailDpUrl,api_secret=api_secrets)
        self.msgs=Driver.parse_data(GoodsByIdsDetailDp,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'OK,code:200')


    def test_ConsumeStatus_sucess(self):
        '''点评--更新到店状态'''
        api_secrets= All_secrets.update_dpStatus
        updateConsumeStatus=test_data.updateConsumeStatus
        updateConsumeStatus=Driver.send_data(updateConsumeStatus,self.updateConsumeStatusUrl,api_secret=api_secrets)
        self.msgs=Driver.parse_data(updateConsumeStatus,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'OK,code:200')


    def test_GoodsBySupplierIdDp_sucess(self):
        '''点评--根据供应商ID获取商品-商户页'''
        api_secrets= All_secrets.update_dpStatus
        GoodsBySupplierIdDp=test_data.GoodsBySupplierIdDp
        GoodsBySupplierIdDp=Driver.send_data(GoodsBySupplierIdDp,self.GoodsBySupplierIdDpUrl,api_secret=api_secrets)
        self.msgs=Driver.parse_data(GoodsBySupplierIdDp,regular_data='.+msg:(.+?\d+),?.*')
        self.assertEqual(self.msgs, 'OK,code:200')





if __name__=='__main__':
    unittest.main()





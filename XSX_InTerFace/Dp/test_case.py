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
import XSX_InTerFace.Common.All_secrets
import XSX_InTerFace.Dp.interface_dp
import XSX_InTerFace.Common.XSX_Driver
times= int(time.time())

class Test(XSX_InTerFace.Dp.interface_dp.MyTest):
    '''点评接口'''

    def test_Create_Order_sucess(self):
        '''创建点评订单'''
        api_secrets=XSX_InTerFace.Common.All_secrets.dp_secrets
        Create_Order=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Create_Orders= Create_Order.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        result=Create_Order.parse_data(Create_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        print result

    def test_UserOrderListDP_sucess(self):
        '''获取用户订单列表-点评项目'''
        api_secrets= XSX_InTerFace.Common.All_secrets.dp_secrets
        UserOrderListDP=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        UserOrderListDP.send_data(test_data.data_UserOrderListDP,self.UserOrderListDP_url,api_secret=api_secrets)

    def test_cancelOrder_sucess(self):
        '''取消订单-点评'''
        api_secrets= XSX_InTerFace.Common.All_secrets.dp_secrets
        CancelOrder=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        CancelOrders=test_data.cancelOrder_data
        DP_Orders=CancelOrder.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        DP_Order=CancelOrder.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        #print DP_Order
        CancelOrders.setdefault('order_sn',DP_Order)
        #print CancelOrders
        CancelOrder.send_data(CancelOrders,self.cancelOrder_url,api_secret=api_secrets)


    def test_applyRefund_sucess(self):
        '''取用户申请退款-点评项目'''
        api_secrets= XSX_InTerFace.Common.All_secrets.dp_secrets
        Data_updatePayStatus=test_data.data_updatePayStatus
        Data_ApplyRefund=test_data.applyRefund_data
        ApplyRefundOrder=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        DP_Orders=ApplyRefundOrder.send_data(test_data.data_OrderDPSuces,self.orderDP_url,api_secret=api_secrets)
        DP_Order=ApplyRefundOrder.parse_data(DP_Orders,regular_data='.+order_sn:(.+?\d+),?.*')
        Order_amount=ApplyRefundOrder.parse_data(DP_Orders,regular_data='.+order_amount:(.+?\d+),?.*')
        #print Order_amount
        Data_updatePayStatus.setdefault('order_sn',DP_Order)
        Data_updatePayStatus.setdefault('order_amount',Order_amount)
        Data_ApplyRefund.setdefault('order_sn',DP_Order)
        Data_ApplyRefund.setdefault('order_amount',Order_amount)
        #print Data_ApplyRefund
        ApplyRefundOrder.send_data(Data_updatePayStatus,self.updatePayStatus_url,api_secret=api_secrets)
        ApplyRefundOrder.send_data(Data_ApplyRefund,self.applyRefund_url,api_secret=api_secrets)


    def test_OrderBySnDp_sucess(self):
        '''获取订单详情-点评项目'''
        Data_OrderBySnDps=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets= XSX_InTerFace.Common.All_secrets.dp_secrets
        Data_OrderBySnDp=test_data.OrderBySnDianping_data
        Data_OrderBySnDps.send_data(Data_OrderBySnDp,self.OrderBySnDianping_url,api_secret=api_secrets)






if __name__=='__main__':
    unittest.main()





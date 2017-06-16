# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
import sys
import os
import Ly_Applet.Ly_Applet.Test_data
import Ly_Applet.Common.Common_Applet
import Ly_Applet.Ly_Applet.interface_Applet
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
class Test(Ly_Applet.Ly_Applet.interface_Applet.MyTest):

    '''小程序接口'''
    def test_search_Ly_sucess(self):
        '''商品标题搜索详情接口'''
        Order_Ly=Ly_Applet.Common.Common_Applet.Applet_Driver()
        Token=Order_Ly.WX_SESSION_KEY()
        Headers=Ly_Applet.Ly_Applet.Test_data.headers(Token)
        Order_Ly.Get_data(Ly_Applet.Ly_Applet.Test_data.search_data,self.searchUrl,headers=Headers)


    def test_goodsList_Ly_sucess(self):
        '''根据出行日期和父商品ID获取子商品列表'''
        Order_Ly=Ly_Applet.Common.Common_Applet.Applet_Driver()
        Token=Order_Ly.WX_SESSION_KEY()
        Headers=Ly_Applet.Ly_Applet.Test_data.headers(Token)
        Order_Ly.Get_data(Ly_Applet.Ly_Applet.Test_data.GoodsList_data,self.goodsListUrl,headers=Headers)




    def test_Order_Ly_sucess(self):
        '''旅游小程序下单'''
        Order_Ly=Ly_Applet.Common.Common_Applet.Applet_Driver()
        Token=Order_Ly.WX_SESSION_KEY()
        print Token
        Headers=Ly_Applet.Ly_Applet.Test_data.headers(Token)
        Order_Ly.Get_data(Ly_Applet.Ly_Applet.Test_data.Order_data,self.Order_Ly,headers=Headers)









if __name__=='__main__':
    unittest.main()
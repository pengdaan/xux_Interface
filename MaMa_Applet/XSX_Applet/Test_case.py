# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
import sys
import os
import MaMa_Applet.XSX_Applet.Test_data
import MaMa_Applet.Common.Common_Applet
import MaMa_Applet.XSX_Applet.interface_Applet
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
class Test(MaMa_Applet.XSX_Applet.interface_Applet.MyTest):

    '''小程序接口'''

    def test_GoodsDetail_sucess(self):
        '''获取商品基本信息'''
        GoodsDetail=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=GoodsDetail.Get_data(Uid,self.Token_url)
        Tokens=GoodsDetail.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        GoodsDetail.Get_data(MaMa_Applet.XSX_Applet.Test_data.goodsDetail,self.goodsDetail_url,headers=Headers)

    def test_Buy_sucess(self):
        '''商品接口获取sku弹窗信息'''
        Buy=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Buy.Get_data(Uid,self.Token_url)
        Tokens=Buy.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Buy.Get_data(MaMa_Applet.XSX_Applet.Test_data.Buy,self.Buy_url,headers=Headers)

    def test_RecommendGoods_sucess(self):
        '''商品接口获取sku弹窗信息'''
        RecommendGoods=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=RecommendGoods.Get_data(Uid,self.Token_url)
        Tokens=RecommendGoods.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        RecommendGoods.Get_data(MaMa_Applet.XSX_Applet.Test_data.RecommendGoods,self.RecommendGoods_url,headers=Headers)

    def test_TabQuery_sucess(self):
        '''良品首页数据展示'''
        TabQuery=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=TabQuery.Get_data(Uid,self.Token_url)
        Tokens=TabQuery.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        TabQuery.Get_data(MaMa_Applet.XSX_Applet.Test_data.TabQuery,self.tabQuery_url,headers=Headers)

    def test_Index_sucess(self):
        '''良品首页数据展示'''
        Index=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Index.Get_data(Uid,self.Token_url)
        Tokens=Index.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Index.Get_data(None,self.index_url,headers=Headers)

    def test_mmcCheckMobile_sucess(self):
        '''入会手机号校验接口'''
        Index=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Index.Get_data(Uid,self.Token_url)
        Tokens=Index.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Index.Get_data(MaMa_Applet.XSX_Applet.Test_data.mmcCheckMobile,self.mmcCheckMobile_url,headers=Headers)

    def test_add_Cart_sucess(self):
        '''加入购物车接口'''
        add_Cart=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=add_Cart.Get_data(Uid,self.Token_url)
        Tokens=add_Cart.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        add_Cart.Get_data(MaMa_Applet.XSX_Applet.Test_data.add_Cart,self.add_Cart,headers=Headers)


    def test_batchDelete_sucess(self):
        '''批量删除购物车接口'''
        batchDelete=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=batchDelete.Get_data(Uid,self.Token_url)
        Tokens=batchDelete.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        batchDelete.Get_data(MaMa_Applet.XSX_Applet.Test_data.batchDelete,self.batchDelete_url,headers=Headers)

    def test_deleteCart_sucess(self):
        '''删除购物车接口'''
        deleteCart=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=deleteCart.Get_data(Uid,self.Token_url)
        Tokens=deleteCart.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        deleteCart.Get_data(MaMa_Applet.XSX_Applet.Test_data.batchDelete,self.deleteCart_url,headers=Headers)


    def test_Update_sucess(self):
        '''更新购物车接口'''
        Update=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Update.Get_data(Uid,self.Token_url)
        Tokens=Update.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Update.Get_data(MaMa_Applet.XSX_Applet.Test_data.update,self.update_url,headers=Headers)

    def test_checkRepost_sucess(self):
        '''检查是否有待支付订单或重复提交'''
        checkRepost=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=checkRepost.Get_data(Uid,self.Token_url)
        Tokens=checkRepost.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        checkRepost.Get_data(MaMa_Applet.XSX_Applet.Test_data.checkRepost,self.checkRepost_url,headers=Headers)

if __name__=='__main__':
    unittest.main()
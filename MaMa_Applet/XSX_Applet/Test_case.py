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

    def test_submitOrder_sucess(self):
        '''立即购买提交订单并支付'''
        submitOrder=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=submitOrder.Get_data(Uid,self.Token_url)
        Tokens=submitOrder.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        submitOrder.Get_data(MaMa_Applet.XSX_Applet.Test_data.submitOrder,self.submitOrder_url,headers=Headers)


    def test_buynow_sucess(self):
        '''立即购买提交订单并支付'''
        buynow=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=buynow.Get_data(Uid,self.Token_url)
        Tokens=buynow.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        buynow.Get_data(MaMa_Applet.XSX_Applet.Test_data.buynow,self.buynow_url,headers=Headers)


    def test_checkout_sucess(self):
        '''购物车结算页接口'''
        checkout=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=checkout.Get_data(Uid,self.Token_url)
        Tokens=checkout.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        checkout.Get_data(None,self.checkout_url,headers=Headers)


    def test_buyShare_sucess(self):
        '''会省会赚-良品推荐分页'''
        buyShare=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=buyShare.Get_data(Uid,self.Token_url)
        Tokens=buyShare.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        buyShare.Get_data(None,self.buyShare_url,headers=Headers)


    def test_buyShareView_sucess(self):
        '''会省会赚-页面'''
        buyShareView=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=buyShareView.Get_data(Uid,self.Token_url)
        Tokens=buyShareView.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        buyShareView.Get_data(None,self.buyShareView_url,headers=Headers)


    def test_shareMoney_sucess(self):
        '''分享赚钱-良品推荐分页'''
        shareMoney=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=shareMoney.Get_data(Uid,self.Token_url)
        Tokens=shareMoney.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        shareMoney.Get_data(None,self.shareMoney_url,headers=Headers)


    def test_shareMoneyView_sucess(self):
        '''分享赚钱-页面'''
        shareMoneyView=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=shareMoneyView.Get_data(Uid,self.Token_url)
        Tokens=shareMoneyView.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        shareMoneyView.Get_data(None,self.shareMoneyView_url,headers=Headers)


    def test_address_delete_sucess(self):
        '''地址管理-删除地址'''
        address_delete=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=address_delete.Get_data(Uid,self.Token_url)
        Tokens=address_delete.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        address_delete.Get_data(MaMa_Applet.XSX_Applet.Test_data.Address_delete,self.address_deleteUrl,headers=Headers)


    def test_Address_delete_sucess(self):
        '''地址管理-地址列表'''
        Address_delete=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Address_delete.Get_data(Uid,self.Token_url)
        Tokens=Address_delete.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Address_delete.Get_data(None,self.address_viewUrl,headers=Headers)


    def test_Address_save_sucess(self):
        '''地址管理-新增或编辑地址'''
        Address_save=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=Address_save.Get_data(Uid,self.Token_url)
        Tokens=Address_save.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        Address_save.Get_data(MaMa_Applet.XSX_Applet.Test_data.Address_delete,self.address_saveUlrl,headers=Headers)


    def test_region_sucess(self):
        '''地址管理-省市区联动'''
        region=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=region.Get_data(Uid,self.Token_url)
        Tokens=region.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        region.Get_data(None,self.region_url,headers=Headers)


    def test_RowByID_sucess(self):
        '''地址管理-获取单个地址'''
        RowByID=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=RowByID.Get_data(Uid,self.Token_url)
        Tokens=RowByID.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        RowByID.Get_data(MaMa_Applet.XSX_Applet.Test_data.RowByID,self.RowByID_url,headers=Headers)


    def test_setDedault_sucess(self):
        '''地址管理-设默认地址'''
        setDedault=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=setDedault.Get_data(Uid,self.Token_url)
        Tokens=setDedault.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        setDedault.Get_data(MaMa_Applet.XSX_Applet.Test_data.setDedault,self.setDedault_url,headers=Headers)

    def test_coupon_Code_sucess(self):
        '''我的优惠券-优惠券兑换'''
        coupon_Code=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_Code.Get_data(Uid,self.Token_url)
        Tokens=coupon_Code.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_Code.Get_data(MaMa_Applet.XSX_Applet.Test_data.coupon_Code,self.coupon_CodeUrl,headers=Headers)

    def test_coupon_page_sucess(self):
        '''我的优惠券-优惠券分页'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.coupon_Code,self.coupon_pageUrl,headers=Headers)


    def test_LY_sucess(self):
        '''我的优惠券-优惠券分页'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Tokens='7bedb350c031ae40abab984c563d282d'
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.aaa,self.LY,headers=Headers)









if __name__=='__main__':
    unittest.main()
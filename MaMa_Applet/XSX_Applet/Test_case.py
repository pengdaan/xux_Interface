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


        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.goodsDetail,self.goodsDetail_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='ok'
        self.assertEqual(self.msgs, msgs, "获取商品基本信息失败")

    def test_Buy_sucess(self):
        '''商品接口获取sku弹窗信息'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.Buy,self.Buy_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='ok'
        self.assertEqual(self.msgs, msgs, "商品接口获取sku弹窗信息失败")

    def test_RecommendGoods_sucess(self):
        '''商品详情获取推荐商品____None'''

        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.RecommendGoods,self.RecommendGoods_url,headers=self.Headers)
        msgs='ok'
        self.assertEqual(self.msgs, msgs, "商品详情获取推荐商品获取失败")

    def test_TabQuery_sucess(self):
        '''良品Table数据展示'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.TabQuery,self.tabQuery_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='ok'
        self.assertEqual(self.msgs, msgs, "良品首页数据展示失败")

    def test_Index_sucess(self):
        '''良品首页数据展示'''

        result=self.MaMa_Applet.Get_data(None,self.index_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='成功'
        print msgs.decode('utf-8')
        self.assertEqual(self.msgs, msgs, "良品首页数据展示失败")

    def test_mmcCheckMobile_sucess(self):
        '''入会手机号校验接口  None'''

        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.mmcCheckMobile,self.mmcCheckMobile_url,headers=self.Headers)
        msgs='ok,code:0'
        self.assertEqual(self.msgs, msgs, "入会手机号校验接口调用失败")

    def test_add_Cart_sucess(self):
        '''加入购物车接口'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.add_Cart,self.add_Cart,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='OK'
        self.assertEqual(self.msgs, msgs, "加入购物车失败")


    def test_batchDelete_sucess(self):
        '''批量删除购物车接口'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.batchDelete,self.batchDelete_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='OK'
        self.assertEqual(self.msgs, msgs, "批量删除购物车失败")

    def test_deleteCart_sucess(self):
        '''删除购物车接口___None'''

        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.batchDelete,self.deleteCart_url,headers=self.Headers)
        msgs='OK'
        self.assertEqual(self.msgs, msgs, "删除购物车接口失败")


    def test_Update_sucess(self):
        '''更新购物车接口'''
        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.add_Cart,self.add_Cart,headers=self.Headers)
        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.update,self.update_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='OK'
        self.assertEqual(self.msgs, msgs, "更新购物车失败")

    def test_checkRepost_sucess(self):
        '''检查是否有待支付订单或重复提交____None'''

        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.checkRepost,self.checkRepost_url,headers=self.Headers)

    def test_submitOrder_sucess(self):
        '''立即购买提交订单并支付'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.submitOrder,self.submitOrder_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+loginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "立即购买提交订单并支付接口失败")


    def test_buynow_sucess(self):
        '''提交订单并支付'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.buynow,self.buynow_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "提交订单并支付失败")


    def test_checkout_sucess(self):
        '''购物车结算页接口'''

        result=self.MaMa_Applet.Get_data(None,self.checkout_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='OK'
        self.assertEqual(self.msgs, msgs, "购物车结算页失败")


    def test_buyShare_sucess(self):
        '''会省会赚-良品推荐分页'''

        result=self.MaMa_Applet.Get_data(None,self.buyShare_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "会省会赚-良品推荐分页获取失败")


    def test_buyShareView_sucess(self):
        '''会省会赚-页面'''

        result=self.MaMa_Applet.Get_data(None,self.buyShareView_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "会省会赚-页面获取失败")


    def test_shareMoney_sucess(self):
        '''分享赚钱-良品推荐分页'''

        result=self.MaMa_Applet.Get_data(None,self.shareMoney_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "分享赚钱-良品推荐分页获取失败")


    def test_shareMoneyView_sucess(self):
        '''分享赚钱-页面____None'''

        self.MaMa_Applet.Get_data(None,self.shareMoneyView_url,headers=self.Headers)



    def test_address_delete_sucess(self):
        '''地址管理-删除地址'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.Address_delete,self.address_deleteUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "地址管理-删除地址失败")

    def test_Address_delete_sucess(self):
        '''地址管理-地址列表'''

        result=self.MaMa_Applet.Get_data(None,self.address_viewUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "地址管理-地址列表失败")


    def test_Address_save_sucess(self):
        '''地址管理-新增或编辑地址'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.Address_save,self.address_saveUlrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "地址管理-新增或编辑地址失败")


    def test_region_sucess(self):
        '''地址管理-省市区联动'''

        result=self.MaMa_Applet.Get_data(None,self.region_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "地址管理-省市区联动失败")


    def test_RowByID_sucess(self):
        '''地址管理-获取单个地址'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.RowByID,self.RowByID_url,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "地址管理-获取单个地址失败")


    def test_setDedault_sucess(self):
        '''地址管理-设默认地址____None'''

        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.setDedault,self.setDedault_url,headers=self.Headers)

    def test_coupon_Code_sucess(self):
        '''我的优惠券-优惠券兑换'''
        MaMa_Applets=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        data="SELECT * FROM mall_redemption_code WHERE promotion_id='805'AND user_id='0'  ORDER BY CODE DESC LIMIT 1"
        data=MaMa_Applets.Limit_data(data,send_data='code')
        Test_data=MaMa_Applet.XSX_Applet.Test_data.coupon_Code(data)
        result=self.MaMa_Applet.Get_data(Test_data,self.coupon_CodeUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "我的优惠券-优惠券兑换失败")

    def test_coupon_page_sucess(self):
        '''我的优惠券-优惠券分页'''

        result=self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.oupon_page,self.coupon_pageUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "我的优惠券-优惠券兑换失败")

    def test_distribution_view_sucess(self):
        '''我的返现-页面'''
        MaMa_Applets=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid(uid='43507844')
        Token=MaMa_Applets.Get_data(Uid,self.Token_url)
        Tokens=MaMa_Applets.parse_data(Token,regular_data='.token:(.+?\d+,?.*)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        result=MaMa_Applets.Get_data(MaMa_Applet.XSX_Applet.Test_data.istribution_view,self.distribution_viewUrl,headers=Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "我的返现-页面获取失败")

    def test_couponview_sucess(self):
        '''我的优惠券-页面'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.couponviewUrl,headers=Headers)

<<<<<<< HEAD
    def test_getMycode_sucess(self):
        '''我的邀请码___None'''

        self.MaMa_Applet.Get_data(None,self.MycodeUrl,headers=self.Headers)



    def test_centerView_sucess(self):
        '''用户中心'''

        result=self.MaMa_Applet.Post_data(None,self.centerViewUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "用户中心获取失败")

    def test_user_info_sucess(self):
        '''用户信息'''

        result=self.MaMa_Applet.Post_data(None,self.user_infoUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "用户信息获取失败")

    def test_sendBindPhoneCode_sucess(self):
        '''用户操作 - 发送手机绑定验证码'''

        result=self.MaMa_Applet.Post_data(MaMa_Applet.XSX_Applet.Test_data.sendBindPhoneCode,self.sendBindPhoneCodeUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "用户操作 - 发送手机绑定验证码获取失败")

    def test_checkBindPhone_sucess(self):
        '''用户操作 - 检查手机绑定'''

        result=self.MaMa_Applet.Post_data(MaMa_Applet.XSX_Applet.Test_data.checkBindPhone,self.checkBindPhoneUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+lginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "用户操作 - 检查手机绑定接口调用失败")


    def test_doBindPhone_sucess(self):
        '''用户操作 - 绑定手机'''

        result=self.MaMa_Applet.Post_data(MaMa_Applet.XSX_Applet.Test_data.doBindPhone,self.doBindPhoneUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+ginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "绑定手机接口调用失败")

    def test_joinView_sucess(self):
        '''良粉页 - 良粉省钱计划【入会页】'''

        result=self.MaMa_Applet.Post_data(None,self.joinViewUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+msg:(.*?\,)')
        msgs='SUCCESS'
        self.assertEqual(self.msgs, msgs, "入会页调用失败")


    def test_getOrderPayInfo_sucess(self):
        '''获取订单去支付信息'''

        result=self.MaMa_Applet.Post_data(MaMa_Applet.XSX_Applet.Test_data.getOrderPayInfo,self.getOrderPayInfoUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+ginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "获取订单去支付信息失败")


    def test_getOrderList_sucess(self):
        '''订单列表'''

        result=self.MaMa_Applet.Post_data(None,self.getOrderListUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+ginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "订单列表获取失败")


    def test_cancel_sucess(self):
        '''订单操作 - 取消'''
=======
    def test_distribution_sucess(self):
        '''我的返现-返现分页'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid(uid='43507844')
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.distribution,self.distributionUrl,headers=Headers)


    def test_distribution_view_sucess(self):
        '''我的返现-页面'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid(uid='43507844')
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.distribution_view,self.distributionViewUrl,headers=Headers)


    def test_Mycode_sucess(self):
        '''我的邀请码'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.MycodeUrl,headers=Headers)

    def test_centerView_sucess(self):
        '''用户中心 - 页面'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.centerViewUrl,headers=Headers)

    def test_userinfo_sucess(self):
        '''用户信息'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.userinfoUrl,headers=Headers)

    def test_BindPhoneCode_sucess(self):
        '''用户操作 - 发送手机绑定验证码'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.BindPhoneCode,self.sendBindPhoneCodeUrl,headers=Headers)

    def test_auth_sucess(self):
        '''用户操作 - 检查手机绑定'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.checkBindPhone,self.authUrl,headers=Headers)

    def test_doBindPhone_sucess(self):
        '''用户操作 - 绑定手机'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        verify_code=coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.BindPhoneCode,self.sendBindPhoneCodeUrl,headers=Headers)
        verify_codes=coupon_page.parse_data(verify_code,regular_data='.+verify_code:(.+?\d+),?.*')
        Test_data=MaMa_Applet.XSX_Applet.Test_data.checkBindPhone(verify_codes)
        coupon_page.Get_data(Test_data,self.doBindPhoneUrl,headers=Headers)

    def test_joinView_sucess(self):
        '''良粉省钱计划 - 页面 【多余待删除】'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.joinViewUrl,headers=Headers)


    def test_JoinView_sucess(self):
        '''良粉页 - 良粉省钱计划【入会页】'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.JoinViewUrl,headers=Headers)


    def test_OrderPayInfo_sucess(self):
        '''获取订单去支付信息'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.OrderPayInfo,self.OrderPayInfoUrl,headers=Headers)

    def test_OrderList_sucess(self):
        '''订单列表'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(None,self.OrderListUrl,headers=Headers)


    def test_Ordercancel_sucess(self):
        '''取消订单'''
        coupon_page=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token=coupon_page.Get_data(Uid,self.Token_url)
        Tokens=coupon_page.parse_data(Token,regular_data='.token:(.+?\d+,?.*\d)')
        Headers=MaMa_Applet.XSX_Applet.Test_data.headers(Tokens)
        coupon_page.Get_data(MaMa_Applet.XSX_Applet.Test_data.Ordercancel,self.OrdercancelUrl,headers=Headers)



>>>>>>> d9b1926d63bdfe279356feaa6bfa926bd4ddf105

        MaMa_Applets=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        data="SELECT * FROM mall_order_info WHERE uid='76383768' ORDER BY order_sn DESC LIMIT 1"
        self.MaMa_Applet.Get_data(MaMa_Applet.XSX_Applet.Test_data.submitOrder,self.submitOrder_url,headers=self.Headers)
        data=MaMa_Applets.Limit_data(data,send_data='order_sn')
        order_cancel=MaMa_Applet.XSX_Applet.Test_data.order_cancel(data)
        result=self.MaMa_Applet.Post_data(order_cancel,self.cancelUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+ginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "取消订单失败")


    def test_receiveConfirm_sucess(self):
        '''订单操作-确认收货___需要调整'''

        result=self.MaMa_Applet.Post_data(MaMa_Applet.XSX_Applet.Test_data.receiveConfirm,self.receiveConfirmUrl,headers=self.Headers)
        self.msgs=self.MaMa_Applet.parse_data(result,regular_data='.+ginCode:(.*?\d+),?.*')
        msgs='1'
        self.assertEqual(self.msgs, msgs, "登录失败")





if __name__=='__main__':
    unittest.main()
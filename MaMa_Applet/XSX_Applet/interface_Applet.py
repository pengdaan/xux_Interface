# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
import MaMa_Applet.Common.Common_Applet
import MaMa_Applet.XSX_Applet.Test_data
class MyTest(unittest.TestCase):
    def setUp(self):
        '''Token创建'''
        self.Token_url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
        self.MaMa_Applet=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        self.Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        self.Token=self.MaMa_Applet.Get_data(self.Uid,self.Token_url)
        self.Tokens=self.MaMa_Applet.parse_data(self.Token,regular_data='.token:(.+?\d+,?.*)')
        self.Headers=MaMa_Applet.XSX_Applet.Test_data.headers(self.Tokens)




        '''专场商品列表分页 None'''
        self.getMmcInfo_url='http://www.xiaoshuixong.com/mapi/mmc/getMmcInfo'
        '''专场商品列表基础信息 None'''
        self.MmcInfo_url='http://www.xiaoshuixong.com/mapi/mmc/getMmcInfo'
        '''商品基本信息'''
        self.goodsDetail_url='http://www.xiaoshuxiong.com/mapi/goods/MaMaIndex/goodsDetail'
        '''商品接口获取sku弹窗信息'''
        self.Buy_url='http://www.xiaoshuxiong.com/mapi/goods/MaMaIndex/toBuy'
        '''商品详情获取推荐商品 None'''
        self.RecommendGoods_url='http://www.xiaoshuxiong.com/mapi/goods/goods/getRecommendGoods'
        '''良品tab'''
        self.tabQuery_url='http://www.xiaoshuxiong.com/mapi/goods/MaMaIndex/tabQuery'
        '''良品首页数据展示'''
        self.index_url='http://www.xiaoshuxiong.com/mapi/goods/MaMaIndex/index'
        '''入会手机号校验接口 None'''
        self.mmcCheckMobile_url='http://www.xiaoshuixong.com/mapi/checkoutBuynow/mmcCheckMobile'
        '''加入购物车接口'''
        self.add_Cart='http://www.xiaoshuxiong.com/mapi/checkout/cart/add'
        '''批量删除购物车接口'''
        self.batchDelete_url='http://www.xiaoshuxiong.com/mapi/checkout/cart/batchDelete'
        '''删除购物车接口'''
        self.deleteCart_url='http://www.xiaoshuixong.com/mapi/cart/deleteCart'
        '''更新购物车接口'''
        self.update_url='http://www.xiaoshuxiong.com/mapi/checkout/cart/update'
        '''检查是否有待支付订单或重复提交'''
        self.checkRepost_url='http://www.xiaoshuxiong.com/mapi/checkout/Buynow/checkRepost'
        '''立即购买提交订单并支付'''
        self.submitOrder_url='http://www.xiaoshuxiong.com/mapi/checkout/buynow/submitOrder'
        '''立即购买结算页接口'''
        self.buynow_url='http://www.xiaoshuxiong.com/mapi/checkout/buynow/index'
        '''良粉入会结算数据获取接口'''
        self.mmcBuy_url='http://www.xiaoshuixong.com/mapi/checkoutBuynow/mmcBuy'
        '''良粉入会订单提交'''
        self.mmcBuyAdd_url='.http://www.xiaoshuixong.com/mapi/checkoutBuynow/mmcBuyAdd'
        '''获取购物车商品运费详情'''
        self.shipinfo='http://www.xiaoshuxiong.com/mapi/checkout/Checkout/shipinfo'
        '''购物车结算页接口'''
        self.checkout_url='http://www.xiaoshuxiong.com/mapi/checkout/cart/index'
        '''购物车订单提交'''
        self.Checkout_addurl='http://www.xiaoshuixong.com/mapi/checkout/Checkout/add'
        '''购物车选中接口'''
        self.selected_url='http://www.xiaoshuixong.com/mapi/cart/selected'
        '''购物车页面数据获取接口'''
        self.cart_url='http://www.xiaoshuixong.com/mapi/checkout/cart/index'
        '''会省会赚-良品推荐分页'''
        self.buyShare_url='http://www.xiaoshuxiong.com/mapi/user/buyShare/page'
        '''会省会赚-页面'''
        self.buyShareView_url='http://www.xiaoshuxiong.com/mapi/user/buyShare/view'
        '''分享赚钱-良品推荐分页'''
        self.shareMoney_url='http://www.xiaoshuxiong.com/mapi/user/shareMoney/page'
        '''分享赚钱-页面'''
        self.shareMoneyView_url='http://www.xiaoshuxiong.com/mapi/user/shareMoney/view'
        '''地址管理-删除地址'''
        self.address_deleteUrl='http://www.xiaoshuxiong.com/mapi/user/address/delete'
        '''地址管理-地址列表'''
        self.address_viewUrl='http://www.xiaoshuxiong.com/mapi/user/address/view'
        '''地址管理-新增或编辑地址'''
        self.address_saveUlrl='http://www.xiaoshuxiong.com/mapi/user/address/save'
        '''地址管理-省市区联动'''
        self.region_url='http://www.xiaoshuxiong.com/mapi/user/region/data'
        '''地址管理-获取单个地址'''
        self.RowByID_url='http://www.xiaoshuxiong.com/mapi/user/address/getRowByID'
        '''地址管理-设默认地址'''
        self.setDedault_url='http://www.xiaoshuxiong.com/mapi/user/address/setDedault'
        '''我的优惠券-优惠券兑换'''
        self.coupon_CodeUrl='http://www.xiaoshuxiong.com/mapi/user/coupon/getByCode'
        '''我的优惠券-优惠券分页'''
        self.coupon_pageUrl='http://www.xiaoshuxiong.com/mapi/user/coupon/page'
<<<<<<< HEAD
        '''我的返现-页面'''
        self.distribution_viewUrl='http://www.xiaoshuxiong.com/mapi/user/distribution/view'
        '''我的邀请码'''
        self.MycodeUrl='http://www.xiaoshuxiong.com/mapi/user/inviteCode/getMycode'
        '''用户信息'''
        self.centerViewUrl='http://www.xiaoshuxiong.com/mapi/user/user/centerView'
        '''用户信息'''
        self.user_infoUrl='http://www.xiaoshuxiong.com/mapi/user/user/info'
        '''用户操作 - 发送手机绑定验证码'''
        self.sendBindPhoneCodeUrl='http://www.xiaoshuxiong.com/mapi/user/user/sendBindPhoneCode'
        '''用户操作 - 检查手机绑定'''
        self.checkBindPhoneUrl='http://www.xiaoshuxiong.com/mapi/user/user/checkBindPhone'
        '''用户操作 - 绑定手机'''
        self.doBindPhoneUrl='http://www.xiaoshuxiong.com/mapi/user/user/doBindPhone'
        '''良粉页 - 良粉省钱计划【入会页】'''
        self.joinViewUrl='http://www.xiaoshuxiong.com/mapi/user/mmcvip/joinView'
        '''获取订单去支付信息'''
        self.getOrderPayInfoUrl='http://www.xiaoshuxiong.com/mapi/user/order/getOrderPayInfo'
        '''订单列表'''
        self.getOrderListUrl='http://www.xiaoshuxiong.com/mapi/user/order/getOrderList'
        '''订单操作 - 取消'''
        self.cancelUrl='http://www.xiaoshuxiong.com/mapi/user/order/cancel'
        '''订单操作 - 确认收货'''
        self.receiveConfirmUrl='http://www.xiaoshuxiong.com/mapi/user/order/receiveConfirm'
        '''旅游下单'''
        self.LY='http://m-ly.mama.cn/main/wxapp/order/submit'
=======
        '''我的优惠券-页面'''
        self.couponviewUrl='http://www.xiaoshuxiong.com/mapi/user/coupon/view'
        '''我的返现-返现分页'''
        self.distributionUrl='http://www.xiaoshuxiong.com/mapi/user/distribution/page'
        '''我的返现-页面'''
        self.distributionViewUrl='http://www.xiaoshuxiong.com/mapi/user/distribution/view'
        '''我的邀请码'''
        self.MycodeUrl='http://www.xiaoshuxiong.com/mapi/user/inviteCode/getMycode'
        '''用户中心 - 页面'''
        self.centerViewUrl='http://www.xiaoshuxiong.com/mapi/user/user/centerView'
        '''用户信息'''
        self.userinfoUrl='http://www.xiaoshuxiong.com/mapi/user/user/info'
        '''用户操作 - 发送手机绑定验证码'''
        self.sendBindPhoneCodeUrl='http://www.xiaoshuxiong.com/mapi/user/user/sendBindPhoneCode'
        '''用户操作 - 检查手机绑定'''
        self.authUrl='http://www.xiaoshuxiong.com/mapi/user/user/checkBindPhone'
        '''用户操作 - 绑定手机'''
        self.doBindPhoneUrl='http://www.xiaoshuxiong.com/mapi/user/user/doBindPhone'
        '''良粉省钱计划 - 页面 【多余待删除】'''
        self.joinViewUrl='http://www.xiaoshuxiong.com/mapi/user/mmcvip/joinView'
        '''良粉页 - 良粉省钱计划【入会页】'''
        self.JoinViewUrl='http://www.xiaoshuxiong.com/mapi/user/mmcvip/joinView'
        '''获取发货单物流详情'''
        self.deliveryHistory='http://www.xiaoshuxiong.com/mapi/user/order/deliveryHistory'
        '''获取订单去支付信息'''
        self.OrderPayInfoUrl='http://www.xiaoshuxiong.com/mapi/user/order/getOrderPayInfo'
        '''订单列表'''
        self.OrderListUrl='http://www.xiaoshuxiong.com/mapi/user/order/getOrderList'
        '''订单操作 - 取消'''
        self.OrdercancelUrl='http://www.xiaoshuxiong.com/mapi/user/order/cancel'
        '''订单操作 - 确认收货'''
        self.receiveConfirmUrl='http://www.xiaoshuxiong.com/mapi/user/order/receiveConfirm'
        '''订单详情'''
        self.OrderdetailUrl='http://www.xiaoshuxiong.com/mapi/user/order/detail'





















>>>>>>> d9b1926d63bdfe279356feaa6bfa926bd4ddf105

    def tearDown(self):

        self.msgs

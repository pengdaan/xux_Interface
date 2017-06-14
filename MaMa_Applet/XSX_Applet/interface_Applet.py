# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''Token创建'''
        self.Token_url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
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
























    def tearDown(self):
        pass
        #print(self.code,self.msgs)

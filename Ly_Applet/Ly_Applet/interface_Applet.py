# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''Token创建'''
        self.Token_url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
        '''登录信息插入redis'''
        self.getMmcInfo_url='http://www.xiaoshuxiong.com/test.php?act=setForRedis'
        '''商品标题搜索详情接口'''
        self.searchUrl='http://m-ly.mama.cn/main/wxapp/search/goodsInfo'
        '''根据出行日期和父商品ID获取子商品列表'''
        self.goodsListUrl='http://m-ly.mama.cn/main/wxapp/goods/list'
        '''登录接口'''
        self.loginUrl='http://m-ly.mama.cn/main/wxapp/login'



        '''旅游下单'''
        self.Order_Ly='http://m-ly.mama.cn/main/wxapp/order/submit'
























    def tearDown(self):
        pass
        #print(self.code,self.msgs)

# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''专场商品列表分页'''
        self.Token_url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
        '''专场商品列表分页'''
        self.getMmcInfo_url='http://www.xiaoshuixong.com/mapi/mmc/getMmcInfo'
        '''专场商品列表基础信息'''
        self.MmcInfo_url='http://www.xiaoshuixong.com/mapi/mmc/getMmcInfo'






















    def tearDown(self):
        pass
        #print(self.code,self.msgs)

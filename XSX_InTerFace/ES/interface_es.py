# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''二手交易市场接口'''
        self.insertSecondHangGoodsUrl='http://es.xiaoshuxiong.com/api/es/sellers/SecondHand/insertSecondHangGoods'



    def tearDown(self):
        pass
        #print(self.code,self.msgs)

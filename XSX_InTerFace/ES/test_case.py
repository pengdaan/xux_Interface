# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import interface_es

import requests, time
from XSX_InTerFace.ES import test_data
from XSX_InTerFace.Common import All_secrets
from XSX_InTerFace.Common import XSX_Driver

times= int(time.time())

class Test(interface_es.MyTest):

    '''2手商品相关接口'''
    def test_PromotionNums_sucess(self):
        '''创建2手商品'''
        SecondHangGoods= XSX_Driver.XsxDriver()
        Headers=test_data.headers
        Test_data=test_data.HangGoods_data()
        SecondHangGoods.Post_data(Test_data,self.insertSecondHangGoodsUrl,Headers)









if __name__=='__main__':
    unittest.main()





# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''商家中心接口'''
        self.registerUrl='http://supplier.api.xiaoshuxiong.com/supplierapi/user/register'
        self.updatUrl='http://supplier.api.xiaoshuxiong.com/supplierapi/user/update'


    def tearDown(self):

        print self.msgs
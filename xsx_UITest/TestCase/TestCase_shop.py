# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
from time import sleep
from XSX_UITest.common.Common_Driver import AutomateDriver
from XSX_UITest.keyword.XUX_ShoppPage import XUXShopPage

"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""


class XUXShopTests(unittest.TestCase):
    def setUp(self):
        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = AutomateDriver()
        self.baseUrl = "http://www.xiaoshuxiong.com"

    def tearDown(self):
        """
        结束每个测试后的清理工作
        :return:
        """
        #self.autoDriver.quitBrowser()

    def test_xux_buy_now(self):
        """
        测试用例：小树熊立即购买
        """
        BayNowPage = XUXShopPage(self.autoDriver, self.baseUrl)
        BayNowPage.Buy_now()
        BayNowPage.passport_Login(img_out="id,img_out_3530904427",q_user="u,3530904427",q_pass="p，qq111111")
        BayNowPage.pay_Sub()






if __name__ == "__main__":
    unittest.main()

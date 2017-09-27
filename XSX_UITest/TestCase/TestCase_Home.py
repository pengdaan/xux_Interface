# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

from XSX_UITest.Common.Common_Driver import AutomateDriver
from XSX_UITest.Page.HomePage import Home


"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""


class XUXTests(unittest.TestCase):
    def setUp(self):
        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = AutomateDriver()
        self.baseUrl = "http://www.xiaoshuxiong.com"


    def test_xux_Spike(self):
        """
        测试用例：打开秒杀页面
        :return:
        """
        # 新建小树熊的页面对象
        Homes = Home(self.autoDriver, self.baseUrl)
        Homes.Spike()


    def test_xux_menu(self):
        """
        测试用例：未登录情况下，检验前端菜单栏链接是否正常
        :return:
        """
        # 新建小树熊的页面对象
        Homes = Home(self.autoDriver, self.baseUrl)
        # 打开妈妈良品
        Homes.MMLP()
        #打开非买不可
        Homes.FMBK()
        #打开小树熊主页
        Homes.SmallBear()
        #打开购物车
        Homes.Shopping_cart()
        #打开个人中心
        Homes.Personal_center()








if __name__ == "__main__":
    unittest.main()

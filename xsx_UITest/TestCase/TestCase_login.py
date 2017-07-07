# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
from time import sleep

from XSX_UITest.Common.Common_Driver import AutomateDriver
from XSX_UITest.keyword.XUX_LoginPage import XUXSubLoginPage


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

    def tearDown(self):
        """
        结束每个测试后的清理工作
        :return:
        """
        self.autoDriver.quitBrowser()

    def test_xux_login(self):
        """
        测试用例：测试小树熊账号密码登录
        :return:
        """
        # 新建小树熊的页面对象
        loginPage = XUXSubLoginPage(self.autoDriver, self.baseUrl)

        # 利用小树熊的页面对象进行登录
        loginPage.login(u"么么22", u"qq111111")
        sleep(2)
        # 断言 是否登录成功
        self.assertEqual(loginPage.getUserPage(), self.autoDriver.getUrl(), "登录失败")


    def test_xux_QQlogin(self):
        """
        测试用例：测试小树熊QQ授权登录
        :return:
        """
        # 新建小树熊的页面对象
        loginPage = XUXSubLoginPage(self.autoDriver, self.baseUrl)
        # 利用小树熊的页面对象进行登录
        loginPage.QQlogin()
        sleep(15)
        # 断言 是否登录成功
        self.assertEqual(loginPage.getUserPage(), self.autoDriver.getUrl(), "登录失败,查看QQ是否登录错误或没有登录QQ")


if __name__ == "__main__":
    unittest.main()

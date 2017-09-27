# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
from XSX_UITest.Common.Common_Driver import AutomateDriver
from XSX_UITest.Page.Back_Page import Back

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

    def test_Back_login(self):
        """
        测试用例：测试小树熊后台账号密码登录
        """
        # 新建小树熊的页面对象，后台登录
        Back_Homes = Back(self.autoDriver, self.baseUrl)
        Result=Back_Homes.Back_Login()
        self.assertEqual(Result,'个人设置',msg="元素不存在")

    def test_Goods_search(self):
        """
        测试用例：小树熊后台商品列表查询
        """
        # 新建小树熊的页面对象，后台登录
        Back_Homes = Back(self.autoDriver, self.baseUrl)
        login=Back_Homes.Back_Login()
        self.assertEqual(login,'个人设置',msg="元素不存在")
        #商品列表页使用分类查询
        Search=Back_Homes.Goods_search()
        print Search
        self.assertEqual(Search,'128：Capricorn',msg="元素不存在")









if __name__ == "__main__":
    unittest.main()

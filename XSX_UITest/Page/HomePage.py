# -*- coding: utf-8 -*-
__author__ = 'leo'
import time
from XSX_UITest.Common.XUX_BasePage import BasePage
from XSX_UITest.keyword.FrontDesk_Home import *

class Home(BasePage):
    def __init__(self, driver, baseUrl):
        """
        调用其 基类 BasePage的 构造函数
        实现 基类 的构造函数的功能
        下面两句都是继承基类的写法，①比②句好用
        :param driver:
        :param baseUrl:
        """
        BasePage.__init__(self,driver,baseUrl)
        self.mainPageUrl = "/mobile"
        self.driver.clearCookies()


    def Spike(self):
        """
        打开秒杀页面
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(Spike)

    def MMLP(self):
        """
        打开妈妈良品页面
        :return:
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(SmallBear_menu)
        self.driver.click(MMLP)

    def FMBK(self):
        """
        打开非买不可页面
        :return:
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(SmallBear_menu)
        self.driver.click(FMBK)


    def Shopping_cart(self):
        """
        打开购物车页面
        :return:
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(SmallBear_menu)
        self.driver.click(Shopping_cart)

    def SmallBear(self):
        """
        打开小树熊页面
        :return:
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(SmallBear_menu)
        self.driver.click(SmallBear)

    def Personal_center(self):
        """
        打开个人中心
        :return:
        """
        self.openPage(self.mainPageUrl)
        self.driver.implicitlyWait(10)
        self.driver.click(SmallBear_menu)
        self.driver.click(Personal_center)

# -*- coding: utf-8 -*-
__author__ = 'leo'
from XSX_UITest.Common.XUX_BasePage import BasePage
from XSX_UITest.keyword.Back_Element import *

class Back(BasePage):

    def __init__(self, driver, baseUrl):
        """
        调用其 基类 BasePage的 构造函数
        实现 基类 的构造函数的功能
        """
        BasePage.__init__(self,driver,baseUrl)
        self.mainPageUrl = "/admin"
        self.driver.clearCookies()#清除浏览器Cookies

    def Back_Login(self):
        self.openPage(self.mainPageUrl)
        self.driver.maximizeWindow()
        self.driver.implicitlyWait(10)
        self.driver.type(adminName[0],adminName[1])
        self.driver.type(adminPwd[0],adminPwd[1])
        self.driver.click(login_submit)
        self.driver.switchFrame(headerframe)
        return self.driver.getText(Personal_center)

    def Goods_search(self):
        self.driver.implicitlyWait(10)
        self.driver.switchDefaultFrame()
        self.driver.switchFrame(menu_frame)
        self.driver.click(List_goods)
        self.driver.switchDefaultFrame()
        self.driver.switchFrame(main_frame)
        self.driver.click(classification)
        self.driver.click(Gcontent)
        self.driver.click(Buttion)
        return self.driver.getText(Good_Title)









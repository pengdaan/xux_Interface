# -*- coding: utf-8 -*-
__author__ = 'leo'
import time

from XSX_UITest.Common.XUX_BasePage import BasePage
class XUXShopPage(BasePage):
    def __init__(self, driver, baseUrl):
        """
        调用其 基类 BasePage的 构造函数
        实现 基类 的构造函数的功能
        """
        BasePage.__init__(self,driver,baseUrl)
        self.shopPageUrl = "/mobile/product.php?id=21386"
        self.driver.clearCookies()


    def passport_Login(self,img_out,q_user,q_pass):
        """
        跳转到大UC页面，登录
        """
        self.driver.click("c,login_others_li")
        try:
            self.driver.switchFrame("id,ptlogin_iframe")
            self.driver.click(img_out)
        except Exception:
            self.driver.type(q_user)
            self.driver.type(q_pass)
            self.driver.click("id,go")
            self.driver.implicitlyWait(5)



    def Buy_now(self):
        """
        小树熊立即购买
        """
        self.openPage(self.shopPageUrl)
        self.driver.clearCookies()
        time.sleep(1)
        self.driver.click("J_btnGroup")
        time.sleep(1)
        self.driver.click("J_skuBtns")



    def pay_Sub(self):
        """
        小树熊提交订单
        """
        self.driver.implicitlyWait(5)
        self.driver.click("J_paySub")
        time.sleep(1)



    def getMainPage(self):
        """
        打开小树熊主页
        """
        return self.baseUrl + self.mainPageUrl

    def getUserPage(self):
        """
        打开小树熊个人中心
        """
        return self.baseUrl + self.loginPageUrl


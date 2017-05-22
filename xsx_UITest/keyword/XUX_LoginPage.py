# -*- coding: utf-8 -*-
__author__ = 'leo'
import time

from XSX_UITest.common.XUX_BasePage import BasePage


class XUXSubLoginPage(BasePage):
    def __init__(self, driver, baseUrl):
        """
        调用其 基类 BasePage的 构造函数
        实现 基类 的构造函数的功能
        下面两句都是继承基类的写法，①比②句好用
        :param driver:
        :param baseUrl:
        """
        BasePage.__init__(self,driver,baseUrl)
        #super(BasePage,self).__init__(self,driver, baseUrl)
        self.loginPageUrl = "/mobile/user.php"
        self.mainPageUrl = "/mobile"
        self.driver.clearCookies()

    def login(self, userName, password):
        """
        登陆小树熊，测试环境（100）
        :param userName: 么么22
        :param password: qq111111
        :return:
        """
        self.openPage(self.loginPageUrl)
        self.driver.clearCookies()
        self.driver.implicitlyWait(5)
        self.driver.click("J_loginBtn")
        self.driver.implicitlyWait(5)
        self.driver.type("cn_account", userName)
        self.driver.type("cn_password", password)
        #这里的处理机制有问题，需要手动输入验证码，正确的处理方式 1)屏蔽验证码 2)设置万能验证码
        self.driver.click("c,login_btn_signin")
        time.sleep(10)
        self.driver.click("id,login_btn_signin")

    def QQlogin(self):
        """
        登陆小树熊，正式环境
        使用QQ授权，登录的QQ账号为3530904427
        """
        self.openPage(self.loginPageUrl)
        self.driver.clearCookies()
        self.driver.implicitlyWait(5)
        self.driver.click("J_loginBtn")
        self.driver.click("c,login_others_li")
        #判断是否使用了模拟iphone6的方式打开浏览器，不同模式登录流程不同,注：登录需要输入QQ密码
        try:
            self.driver.switchFrame("id,ptlogin_iframe")
            self.driver.click("id,img_out_3530904427")
        except Exception:
            self.driver.type("u", '3530904427')
            self.driver.type("p", 'qq111111')
            self.driver.click("id,go")





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
# -*- coding: utf-8 -*-
__author__ = 'leo'
import random
Picture='/xux_project/xux_UITest/Picture'
class BasePage():
    def __init__(self, driver, baseUrl):
        """
        构造方法
        :param driver: 封装好的webdriver
        :param baseUrl: 小树熊的基本url http://www.xioahsuxiong.com/
        :param baseUrl: 小树熊mobile版的基本url http://www.xioahsuxiong.com/mobile
        """

        self.baseUrl = baseUrl
        self.driver = driver

    def openPage(self, url):
        """
        打开浏览器
        :param url: /mobile
        :return:
        """
        self.driver.navigate(self.baseUrl + url)

    def tearDown(self):
        """
        退出浏览器
        """
        self.driver.quitBrowser()

    def screenshot(self):
        """
        屏幕截屏
        """
        Nu=random.randint(20000, 30000)
        #生成5位数的随机数
        bug_Picture=Picture+Nu+'.jpg'
        self.driver.get_screenshot_as_file(bug_Picture)



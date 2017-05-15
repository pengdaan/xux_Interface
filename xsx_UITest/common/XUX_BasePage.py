# -*- coding: utf-8 -*-
__author__ = 'leo'
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
        打开小树熊主页，通过拼接URL的方式
        :param url: /mobile
        :return:
        """
        self.driver.navigate(self.baseUrl + url)



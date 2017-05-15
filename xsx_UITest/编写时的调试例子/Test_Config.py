# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def startChrome():
    """启动Chrome浏览器，并自动转到 百度 首页
    启动Chrome浏览器需要指定驱动的位置
    """
    chrome_driver = os.path.abspath("..\Path\chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chrome_driver
    driver = webdriver.Chrome(chrome_driver)
    driver.get("http://www.baidu.com")
    assert(u"百度" in driver.title)
    elem = driver.find_element_by_name("wd")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    assert u"百度" in driver.title
    driver.close()
    driver.quit()
    driver = None



if __name__ == "__main__":
    # 2.启动浏览器时自动加载插件， 如Firefox -> Firebug ; Chrome -> Chrome to Mobile
    # start_firefox_with_firebug_plug()
    # start_chrome_with_chrometomobile_plug()
    # start_firefox_with_default_settings()
    #start_chrome_with_default_settings()
    # 1.启动各种浏览器
    #startFirefox()
    #startFirefoxWithSpecificLocation()
    startChrome()
    #startIE()
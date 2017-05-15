# -*- coding: utf-8 -*-
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# options = webdriver.ChromeOptions()
# #options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument("user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
# browser = webdriver.Chrome(chrome_options=options)
# sys.s()
# #browser=webdriver.Chrome(chrome_options=options,executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
# #browser = webdriver.Chrome()
# time.sleep(10)
# browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# browser.quit()
# sys.getprofile()
def startChrome():
    """启动Chrome浏览器，并自动转到 百度 首页
    启动Chrome浏览器需要指定驱动的位置
    """
    chrome_driver = os.path.abspath(r"D:\xux_Interface\xsx_UITest\Path\chromedriver.exe")
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
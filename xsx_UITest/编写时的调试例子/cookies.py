# coding=utf-8
from selenium import webdriver
import os
import time
chrome_driver = os.path.abspath("..\Path\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chrome_driver
profile_dir = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--user-data-dir=" + os.path.abspath(profile_dir))
chrome_options.add_argument("--no-startup-window")
chrome_options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://www.66luntan.com")
cookie= driver.get_cookies()

print(cookie)
print(driver.title)


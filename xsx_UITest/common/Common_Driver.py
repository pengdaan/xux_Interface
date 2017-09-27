# coding=utf-8
import os
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append('..')#.. 代表当前路径的上一级路径
from selenium.webdriver.support import expected_conditions as EC

class AutomateDriver(object):
    """
    selenium的框架封装，封装后续测试过程中需要用到基础方法和代码
    """

    def __init__(self):
        """
        把驱动放在项目中，便于代码迁移以及维护
        """
        chrome_driver = os.path.abspath("..\Path\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver
        #设置下载目录，添加配置下载
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "/path/download"}
        chromeOptions.add_experimental_option("prefs", prefs)
        #模拟iPhone6打开，一般情况下少用
        # chromeOptions.add_argument('user-agent="Mozilla/5.0 '
        #                            '(iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46'
        #                            ' (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
        driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chromeOptions)

        try:
            self.driver = driver
        except Exception:
            raise NameError("Chrome Not Found!")


    def clearCookies(self):
        """
        清除驱动程序初始化后的所有Cookie
        """
        self.driver.delete_all_cookies()

    def refreshBrowser(self):
        """
        刷新浏览器
        """
        self.driver.refresh()

    def setwindows_size(self,x,y):
        """
        设置窗口大小
        """
        self.driver.set_window_size(x,y)


    def maximizeWindow(self):
        """
        最大化窗口
        """
        self.driver.maximize_window()


    def navigate(self, url):
        """
        驱动浏览器打开url
        """
        self.driver.get(url)

    def quitBrowser(self):
        """
        浏览器停止
        """
        self.driver.quit()

    def closeBrowser(self):
        """
        关闭浏览器
        """
        self.driver.close()

    def getElement(self, selector):
        """
        通过选择器定位元素
        :arg
        选择器应该以“i，xxx”的例子传递
        "x,//*[@id='langs']/button"
        :返回
        DOM元素
        """
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]   #通过分割函数获取选择元素的方式
        selector_value = selector.split(',')[1]#通过分割函数获取选择元素的元素值

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            #raise NameError("请输入有效类型的定位元素.")
            raise NameError("Please enter a valid type of targeting elements.")
        print element
        return element

    def type(self, selector, text):
        """
        操作输入框.

        用法:
        driver.type("i,el","selenium")
        """
        el = self.getElement(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self.getElement(selector)
        el.click()

    def selectByIndex(self, selector, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.getElement(selector)
        Select(el).select_by_index(index)

    def clickByText(self, text):
        """
        通过链接文本单击元素

        Usage:
        driver.click_text("新闻")
        """
        self.getElement('p,' + text).click()

    def submit(self, selector):
        """
        提交指定的表单.

        Usage:
        driver.submit("i,el")
        """
        el = self.getElement(selector)
        el.submit()

    def executeJs(self, script):
        """
        执行JavaScript脚本.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def getAttribute(self, selector, attribute):
        """
        获取元素属性的值.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self.getElement(selector)
        return el.getAttribute(attribute)

    def getText(self, selector):
        """
        获取元素文本信息.

        Usage:
        driver.get_text("i,el")
        """
        el = self.getElement(selector)
        return el.text

    def getDisplay(self, selector):
        """
        获取要显示的元素，返回结果为true或false.

        Usage:
        driver.get_display("i,el")
        """
        el = self.getElement(selector)
        return el.is_displayed()

    def getTitle(self):
        '''
        获取窗口标题

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def getUrl(self):
        """
        获取当前页面的URL地址.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def acceptAlert(self):
        '''
            接受警告框.
            Usage:
            driver.accept_alert()
            '''
        self.driver.switch_to.alert.accept()

    def dismissAlert(self):
        '''
        关闭警报可用.

        Usage:
        driver.dismissAlert()
        '''
        self.driver.switch_to.alert.dismiss()

    def implicitlyWait(self, secs):
        """
        隐式等待页面上的所有元素.

        Usage:
        driver.implicitly_wait(10)
        """
        self.driver.implicitly_wait(secs)

    def switchFrame(self, selector):
        """
        切换到指定的 frame.

        Usage:
        driver.switch_to_frame("i,el")
        """
        el = self.getElement(selector)
        self.driver.switch_to.frame(el)

    def switchDefaultFrame(self):
        """
        返回下一个更高级别的当前表单机器表单。
        与switch_to_frame（）方法的对应关系。.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def openNewWindow(self, selector):
        '''
        打开新窗口并将手柄切换到新打开的窗口。.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.getElement(selector)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)


    def sendkey(self, selector):
        """
        找到按钮模拟使用回车键进行确认

        Usage:
        driver.sendkey("i,el","selenium")
        """
        el = self.getElement(selector)
        el.clear()
        el.send_keys(Keys.RETURN)

    def screenshot(self):
        """
        屏幕截屏
        """
        Nu=random.randint(20000, 30000) #生成5位数的随机数
        Picture='/xux_project/xux_UITest/Picture'
        bug_Picture=Picture+Nu+'.jpg'
        self.driver.get_screenshot_as_file(bug_Picture)






    # def Title(self,title):
    #    title=EC.title_is(title)
    #    print title(driver)
    #    if title!= True:
    #        print('没有跳转到目标页')
    #        exit(0)
    #    else:
    #        print title



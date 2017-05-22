# -*- coding: utf-8 -*-
__author__ = 'leo'
import time
import sys
sys.path.append('..')#.. 代表当前路径的上一级路径
import unittest
from xux_Interface.setting.HTMLTestRunner import HTMLTestRunner
test_dir='/xux_project/xux_Interface/www'
test_filename='/xux_project/xux_Interface/report/'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ =="__main__":
    now=time.strftime("%y-%m-%d %H_%M_%S", time.localtime())
    filename ='/xux_project/report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner =HTMLTestRunner(stream=fp,
                           title='dp_Interface Test Test_Report',
                           description='Implementation Example whith:'
                           )
    runner.run(discover)
    fp.close()



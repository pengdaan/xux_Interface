# -*- coding: utf-8 -*-
__author__ = 'leo'
import time
import sys
sys.path.append('..')#.. 代表当前路径的上一级路径
#sys.path.append('D:\\xux_project')
import unittest
from XSX_InTerFace.Setting.HTMLTestRunner import HTMLTestRunner
test_dir='/xux_project/XSX_InTerFace/'
test_filename='/xux_project/XSX_InTerFace/report/'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ =="__main__":
    now=time.strftime("%y-%m-%d %H_%M_%S", time.localtime())
    filename =test_filename+now+'_result.html'
    fp=open(filename,'wb')
    runner =HTMLTestRunner(stream=fp,
                           title='xux_project Test Test_Report',
                           description='Implementation Example whith:'
                           )
    runner.run(discover)
    fp.close()


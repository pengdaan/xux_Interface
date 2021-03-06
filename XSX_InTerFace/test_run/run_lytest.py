# -*- coding: utf-8 -*-
__author__ = 'leo'
import time
import sys

sys.path.append('..')#.. 代表当前路径的上一级路径
import unittest
from XSX_InTerFace.Setting.HTMLTestRunnerCN import HTMLTestRunner
test_dir='/xux_project/XSX_InTerFace/Ly'
test_filename='/xux_project/XSX_InTerFace/report/'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ =="__main__":
    now=time.strftime("%y-%m-%d %H_%M_%S", time.localtime())
    filename ='/xux_project/report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner =HTMLTestRunner(stream=fp,
                           title='ly_Interface Test report',
                           description='Implementation Example whith:'
                           )
    runner.run(discover)
    fp.close()

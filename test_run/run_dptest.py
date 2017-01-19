__author__ = 'leo'
import time,sys
sys.path.append('./xux_project')
#sys.path.append('./setting')
import unittest
from setting.HTMLTestRunner import HTMLTestRunner
test_dir='/xux_Interface/dp'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ =="__main__":
    now=time.strftime("%y-%m-%d %H_%M_%S", time.localtime())
    filename ='/xux_Interface/report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner =HTMLTestRunner(stream=fp,
                           title='dp_Interface Test Report',
                           description='Implementation Example whith:'
                           )
    runner.run(discover)
    fp.close()



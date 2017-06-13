# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest
import sys
import os
import MaMa_Applet.XSX_Applet.Test_data
import MaMa_Applet.Common.Common_Applet
import MaMa_Applet.XSX_Applet.interface_Applet
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
class Test(MaMa_Applet.XSX_Applet.interface_Applet.MyTest):

    '''小程序接口'''

    def test_Create_Order_sucess(self):
        '''创建token'''

        Create_Token=MaMa_Applet.Common.Common_Applet.Applet_Driver()
        Uid=MaMa_Applet.XSX_Applet.Test_data.uid()
        Token= Create_Token.Get_data(Uid,self.Token_url)
        print Token



if __name__=='__main__':
    unittest.main()
# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):

        #pms接口
        self.PMSadd_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add'
        self.PMSoperate_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/operate'
        self.CreateDepositMission_url ='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/createDepositMission'
        self.updateDepositMission_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/updateDepositMission'
        self.PmsUpdatestatus_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/updateStatus'
        self.NameRepeat_url= 'http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/checkNameRepeat'
        self.BatchSend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/batchSend'
        self.Pmssend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/send'
        self. createPromotion_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/common/createPromotion'





    def tearDown(self):
       # pass

        print(self.code,self.msgs)

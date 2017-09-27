# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        '''pms接口'''
        self.PMSadd_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add'
        self.PMSoperate_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/operate'
        self.CreateDepositMission_url ='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/createDepositMission'
        self.updateDepositMission_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/updateDepositMission'
        self.PmsUpdatestatus_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/updateStatus'
        self.NameRepeat_url= 'http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/checkNameRepeat'
        self.BatchSend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/batchSend'
        self.Pmssend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/send'
        self. createPromotion_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/Common/createPromotion'
        self.Pmsinfo_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/info'
        self.Pms_pcodeList_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/user/pcodeList'
        self.Pms_listGoodsPromotion_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/user/listGoodsPromotion'
        self.Pms_redemptionUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/redemption/create'
        self.createWithGoodsUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/createWithGoods'
        self.createActivityAll_Url='http://pms.api.xiaoshuxiong.com/pmsapi/action/exclusivePromotion/createActivity'
        self.fullcutPromotionUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/fullcutPromotion/add'
        self.confictUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/common/goods/promotion/confict'
        self.MSUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/ms/save'
        self.MS_GoodsUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/ms/goods/add'
        '''创建抽奖活动'''
        self.PromotionUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/createPromotion'
        '''判断用户是否具有抽奖资格'''
        self.uerQualifiedUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/isUserQualified'
        '''后台获取活动列表信息'''
        self.listPromotionUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/listPromotion'
        '''抽奖活动用户数-前台'''
        self.userCountUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/userCount'
        '''抽奖记录列表接口-前台'''
        self.recordListUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/recordList'
        '''抽奖记录列表接口-前台'''
        self.AdminrecordListUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/admin/recordList'
        '''用户抽奖'''
        self.lotteryUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/lottery'
        '''获取单个抽奖活动信息'''
        self.getPromotionInfoUrl='http://pms.api.xiaoshuxiong.com/pmsapi/action/lottery/getPromotionInfo'





    def tearDown(self):
        pass

#        print(self.code,self.msgs)

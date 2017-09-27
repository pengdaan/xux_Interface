# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
import datetime
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import XSX_InTerFace.XUX_Pms.interface_pms
import time
from XSX_InTerFace.XUX_Pms import test_data
from XSX_InTerFace.Common import All_secrets
from XSX_InTerFace.Common import XSX_Driver
import yaml
times= int(time.time())
Driver= XSX_Driver.XsxDriver()
class Test(XSX_InTerFace.XUX_Pms.interface_pms.MyTest):

    '''PMS接口'''
    def test_Pmsadd_sucess(self):
        '''Pms添加优惠劵'''
        api_secrets=All_secrets.pms_secrets
        Test_data=test_data.test_Addpms
        f = open('D:/xux_project/XSX_InTerFace/Dp/test.yaml')
        data=yaml.load(f)
        data.setdefault('timestamp',times)
        print(data)
        print Test_data
        Driver.send_data(data,self.PMSadd_url,api_secret=api_secrets)



    def test_Pmsoperate_sucess(self):
        '''Pms操作优惠活动（开启、关闭）接口'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.test_Pmsoperate
        Driver.send_data(Test_data,self.PMSoperate_url,api_secrets)


    def test_createDepositMission_sucess(self):
        '''添加定金团活动'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.CreateDepositMission_data
        Driver.send_data(Test_data,self.CreateDepositMission_url ,api_secrets)



    def test_updateDepositMission_sucess(self):
        '''修改定金团活动'''
        api_secrets= All_secrets.pms_secrets
        data="SELECT * FROM mall_promotion_info ORDER BY id DESC LIMIT 1"
        startAt=Driver.Limit_data(data,send_data='start_at')
        endAt=Driver.Limit_data(data,send_data='end_at')
        fromAt=Driver.Limit_data(data,send_data='from_at')
        toAt=Driver.Limit_data(data,send_data='to_at')
        id=Driver.Limit_data(data,send_data='id')
        Title=Driver.Limit_data(data,send_data='title')
        Test_data=test_data.updateDepositMission_data(id,Title,startAt,endAt,fromAt,toAt)
        Driver.send_data(Test_data,self.updateDepositMission_url,api_secrets)


    def test_createWithGoods_sucess(self):
        '''添加拼货团'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createWithGoods_data
        Driver.send_data(Test_data,self.createWithGoodsUrl ,api_secrets)


    def test_createActivityAll_sucess(self):
        '''添加专享活动_all'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createActivityAll_data
        Driver.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_createActivityLF_sucess(self):
        '''添加专享活动_良粉'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createActivityLF_data
        Driver.send_data(Test_data,self.createActivityAll_Url ,api_secrets)


    def test_createActivity3month_sucess(self):
        '''添加专享活动_3个月没购买行为'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createActivity3month_data
        Driver.send_data(Test_data,self.createActivityAll_Url ,api_secrets)


    def test_createActivityNew_sucess(self):
        '''添加限时专享_妈妈良品新客'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createActivityNew_data
        Driver.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_createActivityNews_sucess(self):
        '''添加限时专享_妈妈良品新会员'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.createActivityNews_data
        Driver.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_fullcutPromotion_sucess(self):
        '''添满减满赠活动_满减'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.fullcutPromotion_data
        Driver.send_data(Test_data, self.fullcutPromotionUrl ,api_secrets)


    def test_fullcutPromotionZ_sucess(self):
        '''添满减满赠活动_满赠'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.fullcutPromotionZ_data
        Driver.send_data(Test_data, self.fullcutPromotionUrl ,api_secrets)


    def test_confict_sucess(self):
        '''添加预售商品活动'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.confict_data
        Driver.send_data(Test_data, self.confictUrl ,api_secrets)

    def test_MS_save_sucess(self):
        '''添加秒杀活动'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.MS_save_data
        Driver.send_data(Test_data, self.MSUrl ,api_secrets)


    def test_MS_Goods_sucess(self):
        '''添加秒杀商品到活动中'''
        api_secrets= All_secrets.pms_secrets
        data="SELECT * FROM mall_ms_info WHERE ms_title='Test_MS'ORDER BY ms_id DESC LIMIT 1"
        MSId=Driver.Limit_data(data,send_data='ms_id')
        MS_Goods_data=test_data.MSgoods_data(MSId)
        Driver.send_data(MS_Goods_data,self.MS_GoodsUrl,api_secrets)



    def test_NameRepeat_sucess(self):
        '''检查活动名称是否重复接口'''
        Test_data=test_data.NameRepeat_data
        api_secrets= All_secrets.pms_secrets
        Driver.send_data(Test_data,self.NameRepeat_url,api_secrets)

    def test_Pmssend_sucess(self):
        '''发放优惠卷接口'''
        a=1
        runtime=[]
        while a<=1:
            api_secrets= All_secrets.pms_secrets
            AddPms_data=test_data.test_Addpms
            print AddPms_data
            promotionNames=Driver.parse_data(AddPms_data,regular_data='.+promotionName:(.+?\d+)')+'Test_AddPms'
            Driver.send_data(AddPms_data,self.PMSadd_url,api_secret=api_secrets)
            data="SELECT * FROM mall_promotion where promotion_name='%s'"%promotionNames
            PmsId=Driver.Limit_data(data,send_data='id')
            Test_data=test_data.Pmssend_data(PmsId)
            start = time.clock()
            Driver.send_data(Test_data,self.Pmssend_url,api_secrets)
            end = time.clock()
            print "read: %f s" % (end - start)
            ti=(end - start)
            a=a+1
            print a
            runtime.append(ti)
            print runtime
            print(sum(runtime)/a)





    def test_batchSend_sucess(self):
        '''批量发放优惠卷接口'''
        api_secrets= All_secrets.pms_secrets
        AddPms_data=test_data.test_Addpms
        promotionNames=Driver.parse_data(AddPms_data,regular_data='.+promotionName:(.+?\d+)')+'Test_AddPms'
        Driver.send_data(AddPms_data,self.PMSadd_url,api_secret=api_secrets)
        data="SELECT * FROM mall_promotion where promotion_name='%s'"%promotionNames
        PmsId=Driver.Limit_data(data,send_data='id')
        Test_data=test_data.BatchSend_data(PmsId)
        Driver.send_data(Test_data,self.BatchSend_url,api_secrets)



    def test_Pmsinfo_sucess(self):
        '''获取指定优惠活动信息接口'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.Pmsinfo_data
        Driver.send_data(Test_data,self.Pmsinfo_url,api_secrets)


    def test_PcodeList_sucess(self):
        '''获取用户的优惠券列表接口'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.pcodeList_data
        Driver.send_data(Test_data,self.Pms_pcodeList_url,api_secrets)


    def test_listGoodsPromotion_sucess(self):
        '''获取用户有效的优惠券列表接口'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.listGoodsPromotion_data
        Driver.send_data(Test_data,self.Pms_listGoodsPromotion_url,api_secrets)



    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        api_secrets= All_secrets.pms_secrets
        data="SELECT promotion_code FROM mall_promotion_code WHERE use_time='0' AND order_id='0' ORDER BY code_id DESC LIMIT 1"
        promotion_code=Driver.Limit_data(data,send_data='promotion_code')
        Test_data=test_data.Pms_updateStatus(promotion_code)
        Driver.send_data(Test_data,self.PmsUpdatestatus_url,api_secrets)

    def test_redemption_sucess(self):
        '''创建兑换码'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.redemption_data
        Driver.send_data(Test_data,self.Pms_redemptionUrl,api_secrets)

    def test_Promotion_sucess(self):
        '''创建抽奖活动'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.PromotionData()
        Driver.send_data(Test_data,self.PromotionUrl,api_secrets)


    def test_PUserQualified_sucess(self):
        '''判断用户是否具有抽奖资格'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.UserQualifiedData
        Driver.send_data(Test_data,self.uerQualifiedUrl,api_secrets)

    def test_listPromotion_sucess(self):
        '''后台获取活动列表信息[type:9为抽奖活动]'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.listPromotionData
        Driver.send_data(Test_data,self.listPromotionUrl,api_secrets)

    def test_userCount_sucess(self):
        '''抽奖活动用户数-前台'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.userCountData
        Driver.send_data(Test_data,self.userCountUrl,api_secrets)

    def test_recordList_sucess(self):
        ''''抽奖记录列表-前台'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.recordListData
        Driver.send_data(Test_data,self.recordListUrl,api_secrets)

    def test_AdminrecordList_sucess(self):
        ''''抽奖记录列表-后台'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.AdminrecordListData
        Driver.send_data(Test_data,self.AdminrecordListUrl,api_secrets)

    def test_Lottery_sucess(self):
        ''''抽奖'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.lotteryData
        Driver.send_data(Test_data,self.lotteryUrl,api_secrets)

    def test_PromotionInfo_sucess(self):
        ''''获取单个抽奖活动信息'''
        api_secrets= All_secrets.pms_secrets
        Test_data=test_data.PromotionInfoData
        Driver.send_data(Test_data,self.getPromotionInfoUrl,api_secrets)


if __name__=='__main__':
    unittest.main()





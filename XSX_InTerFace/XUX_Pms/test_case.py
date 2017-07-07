# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import XSX_InTerFace.Setting.api_signs
import XSX_InTerFace.Setting.result_jsons
import XSX_InTerFace.Setting.DBConns
import interface_pms
import time
import test_data
import XSX_InTerFace.Common.All_secrets
import XSX_InTerFace.Common.XSX_Driver
times= int(time.time())

class Test(interface_pms.MyTest):

    '''PMS接口'''
    def test_Pmsadd_sucess(self):
        '''Pms添加优惠劵'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        AddPms=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.test_Addpms
        AddPms.send_data(Test_data,self.PMSadd_url,api_secret=api_secrets)



    def test_Pmsoperate_sucess(self):
        '''Pms操作优惠活动（开启、关闭）接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.test_Pmsoperate
        Pmsoperate=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Pmsoperate.send_data(Test_data,self.PMSoperate_url,api_secrets)


    def test_createDepositMission_sucess(self):
        '''添加定金团活动'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.CreateDepositMission_data
        CreateDepositMission=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        CreateDepositMission.send_data(Test_data,self.CreateDepositMission_url ,api_secrets)



    def test_updateDepositMission_sucess(self):
        '''修改定金团活动'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        UpdateDepositMission=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        data="SELECT * FROM mall_promotion_info ORDER BY id DESC LIMIT 1"
        startAt=UpdateDepositMission.Limit_data(data,send_data='start_at')
        endAt=UpdateDepositMission.Limit_data(data,send_data='end_at')
        fromAt=UpdateDepositMission.Limit_data(data,send_data='from_at')
        toAt=UpdateDepositMission.Limit_data(data,send_data='to_at')
        id=UpdateDepositMission.Limit_data(data,send_data='id')
        Title=UpdateDepositMission.Limit_data(data,send_data='title')
        Test_data=test_data.updateDepositMission_data(id,Title,startAt,endAt,fromAt,toAt)
        UpdateDepositMission.send_data(Test_data,self.updateDepositMission_url,api_secrets)


    def test_createWithGoods_sucess(self):
        '''添加拼货团'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createWithGoods_data
        CreateDepositMission=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        CreateDepositMission.send_data(Test_data,self.createWithGoodsUrl ,api_secrets)


    def test_createActivityAll_sucess(self):
        '''添加专享活动_all'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createActivityAll_data
        CreateDepositMission=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        CreateDepositMission.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_createActivityLF_sucess(self):
        '''添加专享活动_良粉'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createActivityLF_data
        createActivityLF=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        data=createActivityLF.send_data(Test_data,self.createActivityAll_Url ,api_secrets)


    def test_createActivity3month_sucess(self):
        '''添加专享活动_3个月没购买行为'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createActivity3month_data
        createActivityLF=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        createActivityLF.send_data(Test_data,self.createActivityAll_Url ,api_secrets)


    def test_createActivityNew_sucess(self):
        '''添加限时专享_妈妈良品新客'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createActivityNew_data
        createActivityLF=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        createActivityLF.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_createActivityNews_sucess(self):
        '''添加限时专享_妈妈良品新会员'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.createActivityNews_data
        createActivityLF=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        createActivityLF.send_data(Test_data,self.createActivityAll_Url ,api_secrets)

    def test_fullcutPromotion_sucess(self):
        '''添满减满赠活动_满减'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.fullcutPromotion_data
        fullcutPromotion=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        fullcutPromotion.send_data(Test_data, self.fullcutPromotionUrl ,api_secrets)


    def test_fullcutPromotionZ_sucess(self):
        '''添满减满赠活动_满赠'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.fullcutPromotionZ_data
        fullcutPromotion=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        fullcutPromotion.send_data(Test_data, self.fullcutPromotionUrl ,api_secrets)


    def test_confict_sucess(self):
        '''添加预售商品活动'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.confict_data
        confict=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        confict.send_data(Test_data, self.confictUrl ,api_secrets)

    def test_MS_save_sucess(self):
        '''添加秒杀活动'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.MS_save_data
        confict=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        confict.send_data(Test_data, self.MSUrl ,api_secrets)


    def test_MS_Goods_sucess(self):
        '''添加秒杀商品到活动中'''
        MSsend=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        data="SELECT * FROM mall_ms_info WHERE ms_title='Test_MS'ORDER BY ms_id DESC LIMIT 1"
        MSId=MSsend.Limit_data(data,send_data='ms_id')
        MS_Goods_data=test_data.MSgoods_data(MSId)
        MSsend.send_data(MS_Goods_data,self.MS_GoodsUrl,api_secrets)



    def test_NameRepeat_sucess(self):
        '''检查活动名称是否重复接口'''
        NameRepeat=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.NameRepeat_data
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        NameRepeat.send_data(Test_data,self.NameRepeat_url,api_secrets)

    def test_Pmssend_sucess(self):
        '''发放优惠卷接口'''
        Pmssend=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        AddPms_data=test_data.test_Addpms
        print AddPms_data
        promotionNames=Pmssend.parse_data(AddPms_data,regular_data='.+promotionName:(.+?\d+)')+'Test_AddPms'
        #print promotionNames
        Pmssend.send_data(AddPms_data,self.PMSadd_url,api_secret=api_secrets)
        data="SELECT * FROM mall_promotion where promotion_name='%s'"%promotionNames
        #print data
        PmsId=Pmssend.Limit_data(data,send_data='id')
        #print PmsId
        Test_data=test_data.Pmssend_data(PmsId)
        #print Test_data
        Pmssend.send_data(Test_data,self.Pmssend_url,api_secrets)


    def test_batchSend_sucess(self):
        '''批量发放优惠卷接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        BatchSend=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        AddPms_data=test_data.test_Addpms
        promotionNames=BatchSend.parse_data(AddPms_data,regular_data='.+promotionName:(.+?\d+)')+'Test_AddPms'
        #print promotionNames
        BatchSend.send_data(AddPms_data,self.PMSadd_url,api_secret=api_secrets)
        data="SELECT * FROM mall_promotion where promotion_name='%s'"%promotionNames
        #print data
        PmsId=BatchSend.Limit_data(data,send_data='id')
        Test_data=test_data.BatchSend_data(PmsId)
        BatchSend.send_data(Test_data,self.BatchSend_url,api_secrets)



    def test_Pmsinfo_sucess(self):
        '''获取指定优惠活动信息接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Pmsinfo=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.Pmsinfo_data
        Pmsinfo.send_data(Test_data,self.Pmsinfo_url,api_secrets)


    def test_PcodeList_sucess(self):
        '''获取用户的优惠券列表接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        PcodeList=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.pcodeList_data
        PcodeList.send_data(Test_data,self.Pms_pcodeList_url,api_secrets)


    def test_listGoodsPromotion_sucess(self):
        '''获取用户有效的优惠券列表接口'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        listGoodsPromotion=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.listGoodsPromotion_data
        listGoodsPromotion.send_data(Test_data,self.Pms_listGoodsPromotion_url,api_secrets)



    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        Pmsupdate=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        data="SELECT promotion_code FROM mall_promotion_code WHERE use_time='0' AND order_id='0' ORDER BY code_id DESC LIMIT 1"
        promotion_code=Pmsupdate.Limit_data(data,send_data='promotion_code')
        Test_data=test_data.Pms_updateStatus(promotion_code)
        Pmsupdate.send_data(Test_data,self.PmsUpdatestatus_url,api_secrets)

    def test_redemption_sucess(self):
        '''创建兑换码'''
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        redemption=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        Test_data=test_data.redemption_data
        redemption.send_data(Test_data,self.Pms_redemptionUrl,api_secrets)


if __name__=='__main__':
    unittest.main()





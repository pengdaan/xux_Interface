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
import xux_Interface.common.common_Order
import xux_Interface.common.common_data
import requests, time
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
        promotionNames=Pmssend.parse_data(AddPms_data,regular_data='.+promotionName:(.+?\d+)Test_AddPms')+'Test_AddPms'
        print promotionNames
        Pmssend.send_data(AddPms_data,self.PMSadd_url,api_secret=api_secrets)
        data="SELECT * FROM mall_promotion where promotion_name='%s'"%promotionNames
        PmsId=Pmssend.Limit_data(data,send_data='id')
        #print PmsId
        Test_data=test_data.Pmssend_data(PmsId)
        Pmssend.send_data(Test_data,self.Pmssend_url,api_secrets)















    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        Pmsupdate=XSX_InTerFace.Common.XSX_Driver.XsxDriver()
        api_secrets=XSX_InTerFace.Common.All_secrets.pms_secrets
        Test_data=test_data.Pms_updateStatus
        Pmsupdate.send_data(Test_data,self.PmsUpdatestatus_url,api_secrets)




    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.Pms_updateStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.Pms_updateStatus
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PmsUpdatestatus_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")




    def test_batchSend_sucess(self):
        '''批量发放优惠卷接口'''
        order= XSX_InTerFace.Common.common_Order.order()
        pmsNames=order.Pmsadd()
        pms_id=order.Pmsname_all(pmsNames)
        #pms_id=create_data.Pmsname_all(pmsNames)
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.batchSend_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload=pms_id
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.BatchSend_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmssend1_sucess(self):
        '''发放优惠卷接口'''
        order= XSX_InTerFace.Common.common_Order.order()
        pmsNames=order.Pmsadd()
        pms_id=order.Pmsname_one(pmsNames)
        #print pms_id,'pms_id'
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.Pmssend_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=pms_id
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pmssend_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")




    def test_Pmsinfo_sucess(self):
        '''获取指定优惠活动信息接口'''
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.Pmsinfo_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload= test_data.Pmsinfo_data
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pmsinfo_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_PcodeList_sucess(self):
        '''获取用户的优惠券列表接口'''
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.pcodeList_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.pcodeList_data
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pms_pcodeList_url , params=payload)
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_listGoodsPromotion_sucess(self):
        '''获取用户有效的优惠券列表接口'''
        api_key= XSX_InTerFace.Setting.DBConns.Api_secret(**test_data.listGoodsPromotion_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= XSX_InTerFace.Setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.listGoodsPromotion_data
                api_sign= XSX_InTerFace.Setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pms_listGoodsPromotion_url , params=payload)
                self.code=r.status_code
                self.result=r.text
                js= XSX_InTerFace.Setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


if __name__=='__main__':
    unittest.main()





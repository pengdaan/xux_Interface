# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,time
import test_data
import xux_Interface.setting.api_signs
import xux_Interface.setting.result_jsons
import xux_Interface.setting.DBConns
import interface_pms
import xux_Interface.common.common_Order
import xux_Interface.common.common_data
times= int(time.time())

class Test(interface_pms.MyTest):

    '''PMS接口'''
    def test_Pmsadd_sucess(self):
        '''Pms添加优惠劵'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.test_Addpms)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.test_Addpms
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PMSadd_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmsoperate_sucess(self):
        '''Pms操作优惠活动（开启、关闭）接口'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.test_Pmsoperate)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.test_Pmsoperate
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PMSoperate_url, params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_createDepositMission_sucess(self):
        '''添加定金团活动'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.CreateDepositMission_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.CreateDepositMission_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.CreateDepositMission_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

    def test_updateDepositMission_sucess(self):
        '''修改定金团活动'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.updateDepositMission_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload= test_data.updateDepositMission_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.updateDepositMission_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmsupdate_sucess(self):
        '''修改优惠劵状态'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.Pms_updateStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.Pms_updateStatus
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.PmsUpdatestatus_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_NameRepeat_sucess(self):
        '''检查活动名称是否重复接口'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.NameRepeat_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.NameRepeat_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.NameRepeat_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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
        order= xux_Interface.common.common_Order.order()
        pmsNames=order.Pmsadd()
        pms_id=order.Pmsname_all(pmsNames)
        #pms_id=create_data.Pmsname_all(pmsNames)
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.batchSend_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload=pms_id
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.BatchSend_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_Pmssend_sucess(self):
        '''发放优惠卷接口'''
        order= xux_Interface.common.common_Order.order()
        pmsNames=order.Pmsadd()
        pms_id=order.Pmsname_one(pmsNames)
        #print pms_id,'pms_id'
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.Pmssend_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=pms_id
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pmssend_url , params=payload)
                #print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, 'ok')
                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")



    def test_createPromotion_sucess(self):
        '''添加砍价活动'''
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.createPromotion_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload= test_data.createPromotion_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.createPromotion_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.Pmsinfo_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload= test_data.Pmsinfo_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pmsinfo_url , params=payload)
              #  print payload
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.pcodeList_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.pcodeList_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pms_pcodeList_url , params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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
        api_key= xux_Interface.setting.DBConns.Api_secret(**test_data.listGoodsPromotion_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets= xux_Interface.setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload= test_data.listGoodsPromotion_data
                api_sign= xux_Interface.setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.Pms_listGoodsPromotion_url , params=payload)
                self.code=r.status_code
                self.result=r.text
                js= xux_Interface.setting.result_jsons.result_json(self.result)
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




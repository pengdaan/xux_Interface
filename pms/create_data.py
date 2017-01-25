# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import requests,json
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import time
times= int(time.time())
PMSadd_url="http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add"
BatchSend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/batchSend'
def Pmsadd():
        '''Pms添加优惠劵'''
        api_key=setting.DBConns.Api_secret(**test_data.test_Addpms)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.test_Addpms
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                requests.post(PMSadd_url, params=payload)
                print test_data.promotionNames
                return str(test_data.promotionNames)
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")

def Pmsname_one(pmsName):
    #获取Pms活动的活动id
    PmsId="SELECT * FROM mall_promotion where promotion_name='%s'"%pmsName
    mysql = setting.DBConns.Mysql()
    datas=mysql.get_one(PmsId)
    if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
        pms_id=datas['id']
        Pmssend_data={
            'api_key':'647b00ec1fe6990b1b97263b05341b6b',
            'timestamp':times,
            'data':'{"promotionId":"' + str(pms_id) + '","num":10,"mark":"","type":1,"userId":1160,"adminId":1}'
        }
       # print Pmssend_data
        return Pmssend_data
    else:
        print 'pms_id 不存在'

def Pmsname_all(pmsName):
    #获取Pms活动的活动id
    PmsId="SELECT * FROM mall_promotion where promotion_name='%s'"%pmsName
    mysql = setting.DBConns.Mysql()
    datas=mysql.get_one(PmsId)
    if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
        pms_id=datas['id']
        batchSend_data={
            'api_key':'647b00ec1fe6990b1b97263b05341b6b',
            'timestamp':times,
            'data':'{"promotionId":"' + str(pms_id) + '","num":1,"mark":"","type":0,"userIds":[1160],"adminId":1}'
        }
       # print Pmssend_data
        return batchSend_data
    else:
        print 'pms_id 不存在'

def batchSend():
        '''批量发放优惠卷接口'''
        api_key=setting.DBConns.Api_secret(**test_data.batchSend_data)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.pmssecret(api_key)#返回api_secret
            #print api_secrets
            if api_secrets !=0:
                payload=test_data.batchSend_data
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(BatchSend_url , params=payload)
                return r.text
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


def Pms_code():
    try:
        # 将json对象转换成python对象
        result=batchSend()
        json_to_python = json.loads(result)
        data_1 = json_to_python['data']
        data_2=data_1['results']
        data_3=data_2[0]
        data_4=data_3['codeList']
        print data_4
        return data_4
    except:
        print (result)



Pms_code()
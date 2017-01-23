# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import requests,json
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import time
times= int(time.time())


orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'


def DP_order(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        order = json_to_python['data']
        #print type(dp_order)
        dp_order=order['order_sn']
        return dp_order
    except:
        print (result)

def test_post_orderDP():
        '''创建点评订单测试数据'''
        api_key=setting.DBConns.Api_secret(**test_data.data_OrderDPSuces)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.data_OrderDPSuces
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(orderDP_url, params=payload)
                results= r.text
                return DP_order(results)


def updatePayStatus():
        '''更新订单支付状态'''
        payloads=test_data.data_updatePayStatus
        order_sns=test_post_orderDP()#生成订单号
        payloads.setdefault('order_sn',order_sns) #插入订单号
        api_key=setting.DBConns.Api_secret(**test_data.data_updatePayStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(updatePayStatus_url, params=payload)
                print r.text
                return order_sns


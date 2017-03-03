# -*- coding: utf-8 -*-
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,json,time
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import all_secrets
times= int(time.time())

createOrderTour_url='http://www.xiaoshuxiong.com/api/order/createOrderTour'
updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'11',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}

'''获取旅游order_id'''
def ly_order(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        order = json_to_python['data']
        #print type(dp_order)
        dp_order=order['order_id']
       # print result
        return dp_order
    except:
        print (result)

'''获取旅游订单号'''
def ly_ordersn(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        order = json_to_python['data']
        #print type(dp_order)
        ly_order=order['order_sn']
       # print result
        return ly_order
    except:
        print (result)

def reateOrderTour(status=1):
        '''旅游创建订单'''
        api_secrets=all_secrets.ly_secrets
        payload=test_data.createOrderTour_data
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(createOrderTour_url, params=payload)
        results= r.text
        if status==1:
            return ly_ordersn(results)
        elif status==2:
            return ly_order(results)

def updatePayDPStatu(order_sn):
        '''更新订单支付状态'''
        api_secrets=all_secrets.update_dpStatus
        payloads=data_updatePayStatus
        payloads.setdefault('order_sn',order_sn) #插入订单号
        payload=payloads
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(updatePayStatus_url, params=payload)
        results= r.text
        print results
        print order_sn


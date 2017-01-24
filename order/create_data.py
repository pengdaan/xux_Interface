# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import requests,json
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import time
times= int(time.time())


orderXUX_url="http://order.api.xiaoshuxiong.com/Order/createOrderXsx"
updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'


def xux_order(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        data_1 = json_to_python['data']
        data_2=data_1['2']
        XUXorder=data_2['order_sn']
        return XUXorder
    except:

        print (result)

def createOrderXsx():
        '''小树熊下单接口'''
        payload= test_data.data_createOrderXsx
        r=requests.post(orderXUX_url,params=payload)
        #print payload
        result=r.text
        print xux_order(result)
        return  xux_order(result)



def updatePayStatus():
        '''更新订单支付状态'''
        payloads=test_data.data_updatePayStatus
        order_sns=createOrderXsx()#生成订单号
        payloads.setdefault('order_sn',order_sns) #插入订单号
        api_key=setting.DBConns.Api_secret(**test_data.data_updatePayStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
               # print payload
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                requests.post(updatePayStatus_url, params=payload)
                #r=requests.post(updatePayStatus_url, params=payload)
                # print r.text
                print order_sns
                return order_sns


def Updatexux_Order(XUXorder): #通过修改数据库更改订单状态为已审核状态，只能改普通的直邮订单

    XUXorders = "UPDATE mall_order_info SET order_status='1',order_amount='0',confirm_time='%s' WHERE order_sn='%s'"%times%XUXorder
    mysql = setting.DBConns.Mysql()
    mysql.get_one(XUXorders)


order11=updatePayStatus()
aa=setting.DBConns.Updatexux_Order(order11)
print aa

# def Updatexux_Order():
#     Orders=updatePayStatus()


















#createOrderXsx()

updatePayStatus()
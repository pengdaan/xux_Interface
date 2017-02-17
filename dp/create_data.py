# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import requests,json
import test_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import time
import all_secrets
times= int(time.time())
orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'

#成功创建订单，不发卷
data_OrderDPSuces={
         'uid':'43507844',
        'timestamp':times,
        'consignee':'么么22',
        'shop_id':'38021',
        'pay_expire':'7200',
        'mobile':'13728142737',
        'source':'wap',
        'shop_city':'289',
        'version':'2.0',
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'products':'[{"product_id":"10852",'
                   '"goods_id":"846",'
                   '"product_sn":"product2016101010852",'
                   '"goods_name":"扣点商品001（xsx勿动）",'
                   '"shop_price":"10.00",'
                   '"goods_thumb":"//cdn-dianping.mama.cn/upload/201610/20161010/b02077e9907e75c58d15b8c6245bb175.jpg",'
                   '"supplier_id":"121",'
                   '"without_return":"0",'
                   '"goods_number":"1",'
                   '"use_coupon":"3",'
                   '"end_return_time":"0",'
                   '"return_anytime":"1",'
                   '"goods_attr_id":"3030",'
                   '"goods_attr":"默认属性:均码"}]'
}


#成功创建订单,发卷
data_OrderDPSuce={
    "timestamp":times,
    "uid": "43507844",
    "consignee": "么么22",
    "mobile": "13728142737",
    "shop_id": "1",
    "products": "[{\"product_id\":\"10860\",\"goods_id\":\"870\",\"product_sn\":\"product2017021610860\",\"goods_name\":\"\\u6d4b\\u8bd5\\u5546\\u54c1_02(\\u53d1\\u5377)\",\"cat_id\":\"483\",\"shop_price\":\"10.00\",\"goods_thumb\":\"\\/\\/cdn-dianping.mama.cn\\/upload\\/http:\\/\\/cdn-dianping.mama.cn\\/upload\\/201702\\/20170206\\/2a572c38539179823fc795d455e9b526.jpg\",\"supplier_id\":\"1\",\"without_return\":\"0\",\"goods_number\":\"1\",\"use_coupon\":\"3\",\"end_return_time\":\"0\",\"return_anytime\":\"0\",\"goods_attr_id\":\"3080|3081\",\"goods_attr\":\"\\u989c\\u8272:\\u7ea2\\u8272|\\u7801\\u6570:38\"}]",
    "source": "wap",
    "shop_city": "1",
    "pay_expire": "7200",
    "version": "2.1",
    "api_key": "8d46b75a4a0456a35302d2893ed072a3",

}


'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}

def DP_order(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        order = json_to_python['data']
        #print type(dp_order)
        dp_order=order['order_sn']
       # print result
        return dp_order
    except:
        print (result)

def orderDP(order_data=data_OrderDPSuces):
    '''新的点评下单方法，弃用旧的方法，secrets写死的方式，不走查库的方法'''
    api_secrets=all_secrets.dp_secrets
    payload=order_data
    api_sign=setting.api_signs.api_signs(payload,api_secrets)
    payload.setdefault('api_sign',api_sign)
    r=requests.post(orderDP_url, params=payload)
    results= r.text
    return DP_order(results)

def updatePayDPStatu(status=1):
        '''更新订单支付状态'''
        api_secrets=all_secrets.update_dpStatus
        payloads=data_updatePayStatus
        #不发卷订单
        if status==1:
            order_sns=orderDP()#生成订单号
            payloads.setdefault('order_sn',order_sns) #插入订单号
            payload=payloads
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
            requests.post(updatePayStatus_url, params=payload)
            return order_sns
        #发卷订单
        elif status==2:
            order_sns=orderDP(data_OrderDPSuce)#生成订单号
            payloads.setdefault('order_sn',order_sns) #插入订单号
            payload=payloads
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
             #r=requests.post(updatePayStatus_url, params=payload)
             # #print r.text
             # #print order_sns
            requests.post(updatePayStatus_url, params=payload)
            return order_sns



'''旧的累赘方法'''

def post_orderDP():
        '''创建点评订单测试数据,【创建订单为不发卷订单】'''
        api_key=setting.DBConns.Api_secret(**test_data.data_OrderDPSuces)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            print api_secrets
            if api_secrets !=0:
                payload=test_data.data_OrderDPSuces
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(orderDP_url, params=payload)
                results= r.text
                return DP_order(results)



def post_CorderDP():
        '''创建点评订单测试数据,【创建订单为发卷订单】'''
        api_key=setting.DBConns.Api_secret(**test_data.data_OrderDPSuce)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=test_data.data_OrderDPSuce
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(orderDP_url, params=payload)
                results= r.text
                return DP_order(results)


def updatePayStatus():
        '''更新订单支付状态'''
        payloads=test_data.data_updatePayStatus
        order_sns=post_orderDP()#生成订单号
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
                #  print order_sns
                return order_sns


def updatePayStatu():
        '''更新订单支付状态(点评发卷)'''
        payloads=test_data.data_updatePayStatus
        order_sns=post_CorderDP()#生成订单号
        payloads.setdefault('order_sn',order_sns) #插入订单号
        api_key=setting.DBConns.Api_secret(**test_data.data_updatePayStatus)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=payloads
                #print payload
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                requests.post(updatePayStatus_url, params=payload)
                #r=requests.post(updatePayStatus_url, params=payload)
                #print r.text
                #print order_sns
                return order_sns
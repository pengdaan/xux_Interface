__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import requests
import time
import json
import api_sign


def xux_prot():

    #url='http://www.xiaoshuxiong.com/api/delivery/shipByOrder'
    url='http://order.api.xiaoshuxiong.com/Order/createOrderXsx ' #小树熊下单
    #url='http://order.api.xiaoshuxiong.com/order/receiveOrderReturn'
    #url='http://order.api.xiaoshuxiong.com/order/applyRefund'
    payloads=api_sign.payload

    api_signs =api_sign.api_sign()
    print api_signs
    payloads.setdefault('api_sign',api_signs)
    r=requests.post(url,params=payloads)
    print payloads
    result=r.text
    try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
    except:
            print (result)

xux_prot()


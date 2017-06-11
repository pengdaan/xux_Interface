__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import json

import requests

import api_sign


def xux_prot():

    #url='http://XUX_www.xiaoshuxiong.com/api/delivery/shipByOrder'
    url='http://XUX_OrderApi.api.xiaoshuxiong.com/Order/createOrderXsx ' #小树熊下单
    #url='http://XUX_OrderApi.api.xiaoshuxiong.com/XUX_OrderApi/receiveOrderReturn'
    #url='http://XUX_OrderApi.api.xiaoshuxiong.com/XUX_OrderApi/applyRefund'
    payloads= api_sign.payload

    api_signs = api_sign.api_sign()
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


# -*- coding: utf-8 -*-
__author__ = 'leo'


def headers(token):
    """
    模拟手机访浏览器访问小程序时的头文件
    """
    headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN',
    'WX-SESSION-KEY':''+token+'',
    }
    return headers

'''商品标题搜索详情接口'''
search_data={
    'data':'{"kw":"测试","page":1,"rows":10}'
}
'''根据出行日期和父商品ID获取子商品列表'''
GoodsList_data={
    'data':{"pid":'690',"date":"2017-07-01至 2017-09-03"}
}
'''旅游下单'''
Order_data={
    'data':'{"travellers":[{"travellerType":3,"travellerName":"彭子曦","mobile":"13728142737","email":"","idCard":""}],'
           '"source":"wxapp","postscript":"",'
           '"goods":[{"skuId":106306,"number":1}]}'
}


# -*- coding: utf-8 -*-
__author__ = 'leo'

import hashlib
import requests
import redis
import json

url='http://www.xiaoshuxiong.com/test.php?act=setForRedis'
LY='http://m-ly.mama.cn/main/wxapp/order/submit'
signs='wx_app_session_76383768'
import json
md5jm= hashlib.new("md5", signs).hexdigest()


print md5jm

Headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN',
    'WX-SESSION-KEY':''+md5jm+'',
    }


test_data={
    'host':'10.0.0.150',
    'port':'6379',
    'key':''+md5jm+'',
    'val':'{"unionId":"sb","userId":76383768,"userName":"3546650393"}'
}


Order_data={
    'data':'{"travellers":[{"travellerType":3,"travellerName":"彭子曦","mobile":"13728142737","email":"","idCard":""}],"source":"wxapp","postscript":"","goods":[{"skuId":106306,"number":1}]}'
}
#r = redis.Redis(host='10.0.0.150',port=6379,db=0)
#r.set(''+md5jm+'','{"unionId":"sb","userId":76383768,"userName":"3546650393"}')

r=requests.get(url,params=test_data)
print r.text
order=requests.post(url=LY,params=Order_data,headers=Headers)
#print r
result=order.text

try:
    js = json.loads(result)
    print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
except:
    print (result)


  #  小树熊:http://wiki.corp.mama.cn/pages/viewpage.action?pageId=77435197
    #旅  游:http://jira.corp.mama.cn/browse/LY-1055
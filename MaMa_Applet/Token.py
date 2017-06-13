__author__ = 'leo'
import requests
import json
url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
url2='http://www.xiaoshuxiong.com/test.php?act=setForRedis'
url3='http://www.xiaoshuxiong.com/mapi/user/user/info'
url4='http://www.xiaoshuxiong.com/mapi/checkout/buynow/submitOrder'
url5='http://www.xiaoshuxiong.com/mapi/goods/MaMaIndex/goodsDetail'
url6='http://www.xiaoshuxiong.com/mapi/checkout/buynow/submitOrder'
url7='http://www.xiaoshuxiong.com/mapi/checkout/buynow/index'
uid={
    'uid':43507844,

}


Test_data2={
    'host':'10.0.0.100 ',
    'port':'6379',
    'key': '291a6843387cabdaa388144c516aa7ac',
    'val':'???'

}


Test_data4={
    'goods_id':'839',
    'goods_numbe':'1',
    'attr_id':'305',
    'pid':'undefined',
    'address_id':'1724'



}
Test_data5={
    'goods_id':'801'
}

Test_data6={
    'goods_id':'810',
    'attr_id':'2926,2930',
    'goods_number':'1',
    'address_id':'1760'

}

Test_data7={
    'goods_id':'810',
    'attr_id':'2927,2930',
    'goods_number':'1',
    'promotion_type':'-1',
    'promotion_id':'-1'


}


headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN',
    'token':'90ee1a3e38ff94e4a7998ac829b7434d'

}
#r=requests.post(url,params=uid)
r=requests.post(url7,params=Test_data7,headers=headers)
result=r.text

try:
    js = json.loads(result)
    print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
except:
    print (result)
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import time
import datetime
import random
times= int(time.time())
dtime=datetime.datetime.now()
def addHTime():#当前时间戳增加1小时
    dtime=datetime.datetime.now()
    dtime2= dtime + datetime.timedelta(hours=1)
    timestamp=int(time.mktime(dtime2.timetuple()))
    return timestamp
def addTime():#当前时间戳增加15分钟
    dtime=datetime.datetime.now()
    dtime2= dtime + datetime.timedelta(hours=0.25)
    timestamp=int(time.mktime(dtime2.timetuple()))
    return timestamp


#2手市场接口

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN',
    #'Cookie':'cookie_map=fc90d80fce543fac8743e1bd600bc179; ZwbC_8757_lastvisit=1502182356; ZwbC_8757_visitedfid=178; ZwbC_8757_auth=ccf658S1gsiIuuAwWZCXNGYTwsIOnUilHWmRGDC6adDdcn%2FKzI6XdSpDIATJTnk9t8KOXc2sZKVPJmpOLusOFTEx9utL2w; mamaun=%E4%B9%88%E4%B9%8822; mamaid=43507844; _ga=GA1.2.1067284069.1502676400; PPSID=5utftefovab7kci2um80f4ch23; passport_login=5utftefovab7kci2um80f4ch23; user_id=74264782; xkey=fb79ce91af082487bd27fa53d01ba1cb; xloginmama_service=http%3A%2F%2Fes.xiaoshuxiong.com%2F%23%2Fdetail%2Fsale%2F33753; mmt_step=true; step=1; MAMADATA60=mama_rp=3&si=45589faa033a08827cd5913b1e4b323e&ltime=1503047894442&rtime=2&sinfid=0&sinpage=__&location=http%3A%2F%2Fpassport.mama.cn%2Fappwap%2FbindPhone2; Hm_lvt_f2babe867b10ece0ff53079ad6c04981=1502178477,1503043606,1503047887; Hm_lpvt_f2babe867b10ece0ff53079ad6c04981=1503047895; PHPSESSID=5utftefovab7kci2um80f4ch23'
    'Cookie':'user_resource=7; mama_username=%E4%B9%88%E4%B9%8822; mama_sess=b6eff682ce0ba27591a6dd9386aafc19e7b801bb'
}

'''创建商品'''
def HangGoods_data():
    coupon=random.randint(1000000, 10000000)
    goods_name='es_commodity_'+str(coupon)
    HangGoods_data={
        'cat_id':'396',
        'new_degree':'2',
        'goods_name':''+str(goods_name)+'',
        'shop_price':'10',
        'postage':'2',
        'goods_desc':'get me es_commodity',
        'goods_img':'[{"newImg":true,'
                '"img_original":"seller_goods_img/original_da69bb3c1fa0f0319801f3e842849b44.jpg",'
                '"newImg":true,'
                '"img_max":"seller_goods_img/max_fe31b083734733dbfc5855d2ba19582a.jpg",'
                '"img_thumb":"seller_goods_img/thumb_fdca1195c7d94f0303662205b1bc3868.jpg"'
                '}]'
    }
    return HangGoods_data












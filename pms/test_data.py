# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import time
import datetime
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



add_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))# 获取当前时间。
promotionNames=str(add_time) + 'Test_AddPms'

Title=str(add_time)+'Test_AddPms'
dingjintuanTitle = str(add_time)+'Test_DJTuan'


#PMS相关接口

'''增加优惠劵 '''
test_Addpms={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{'
           '"promotionName":"' + str(promotionNames) + '",'
           '"sendNumLimit":2,'
           '"sendNum":0,"startDateLimit":2,'
           '"dateExpireNum":1,'
           '"getNumLimit":0,'
           '"adminId":1,"suppliersId":0,'
           '"promotionTitle":"' + str(Title) + '",'
           '"promotionDetail":"",'
           '"receiveLimit":1,'
           '"type":0,'
           '"rangeType":0,'
           '"chargePer":0.9,'
           '"supplierChargePer":0.1,'
           '"promotionRange":[],'
           '"supportMsGoods":1,'
           '"linkUrl":"",'
           '"selfType":"1",'
           '"supportDistributeGoods":1,'
           '"promotionType":1,'
           '"discountMoney":10,'
           '"useMinMoney":20,'
           '"goodsNumber":0'
           '}'

}
'''操作优惠活动（开启、关闭）接口 '''
test_Pmsoperate = {
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,

    'data':'{'
           '"promotionId": 454,'
           '"adminId": 1,'
           '"status": 2'
           ' }'
}


'''定金团4个时间处理机制：'''

'''1：定金支付时间直接使用当前时间戳'''
startAt=times

'''2.定金结束时间等于开始时间+15分钟'''
endAt=addTime()

'''3.尾款开始时间为定金结束时间+15分钟'''
fromAt=str(int(endAt)+600)

'''4.尾款结束时间为定金结束时间+15分钟'''
toAt=str(int(fromAt)+600)

'''新增定金团接口'''
CreateDepositMission_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{'
            '"photo":"images\/ms\/1484566379924518021.jpg",'
            '"goodsId":777,'
             '"title":"' + str(dingjintuanTitle) + '",'
             '"startAt":"'+ str(startAt) +'",'
             '"endAt":"'+ str(endAt) + '",'
             '"fromAt":"'+ str(fromAt) + '",'
             '"toAt":"'+ str(toAt) + '",'
             '"virtualHit":0,'
             '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0}'



}
'''修改定金团接口'''
updateDepositMission_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
    'data':'{'
        '"photo":"images\/ms\/1484566379924518021.jpg",'
        '"goodsId":777,"title":"2017-01-17 17:54:59Test_DJTuan",'
        '"startAt":1484646899,'
        '"endAt":1484647799,'
        '"fromAt":1484648399,'
        '"toAt":1484648999,'
        '"virtualHit":0,'
        '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0,"id":327}'
}
'''更新优惠劵状态'''
Pms_updateStatus={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionCode":"79241216","status":2,"orderId":"24594"}'


}

'''检查活动名称是否重复接口'''
NameRepeat_data={

    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"2017-01-19 18:25:49Test_DJTuan"}'

}
















































'''小树熊下单'''
data_createOrderXsx1 ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{"
                  "order:{serial_no:14841953352617914717,"
                         "user_id:1160,"
                         "uid:43507844,"
                         "source:wap,"
                         "referer:windows|wap|192.168.14.61,"
                         "source_type:1,"
                        "pid:c73400f06fe6f3c9796003c08a0f5a6d,"
                        "trade_pwd:\"\","
                        "surplus:40.00},"
                  "address:{address_id:1724,"
                            "\"customs_id\":\"3474\","
                            "\"address_type\":\"0\","
                            "\"consignee\":\"\\u674e\\u56db\","
                            "\"mobile\":\"13728142737\","
                            "\"province\":\"1\","
                            "\"city\":\"37\","
                            "\"district\":\"0\","
                            "\"country\":\"0\","
                            "\"address\":\"\\u81ea\\u8d2d\\u8fd4\\u73b0\","
                            "\"is_default\":\"0\"},"
              "\"customs\":{\"is_customs\":\"2\",\"customs_info\":{\"card_id\":\"440921199201184218\",\"customs_id\":\"3474\"},"
              "\"customs_pic\":{\"id\":\"3474\",\"identit_card\":\"440921199201184218\",\"img_front_original\":\"identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg\",\"img_front_max\":\"identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg\",\"img_front_thumb\":\"identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg\",\"img_back_original\":\"identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg\",\"img_back_max\":\"identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg\",\"img_back_thumb\":\"identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg\"}}}",
"goods_list": "{\"10750\":{\"goods_id\":\"777\",\"product_id\":\"10750\",\"product_sn\":\"cp0000001234\",\"goods_name\":\"\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539\",\"goods_sn\":\"XSX000777\",\"goods_own_type\":\"1\",\"shop_price\":40,\"market_price\":\"52.00\",\"is_on_sale\":\"1\",\"is_delete\":\"0\",\"is_customs\":\"2\",\"product_number\":\"129\",\"ext_price\":\"0.00\",\"delivery_method\":\"19\",\"goods_weight\":\"1.000\",\"cdn_status\":\"1\",\"goods_thumb\":\"https:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg\",\"order_quota\":\"100\",\"is_real\":\"1\",\"supplier_id\":\"128\",\"without_return\":\"0\",\"erp_goods_id\":\"0\",\"app_id\":\"0\",\"cat_id\":\"25\",\"shelf_life\":\"0\",\"shelf_life_start\":\"0\",\"sms_delivery\":\"0\",\"coupons\":\"0\",\"coupons_verificat\":\"0\",\"return_anytime\":\"0\",\"brand_id\":\"3\",\"goods_attr\":[\"\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801\",\" \\n\"],\"goods_attr_id\":\"2777\",\"isDistribution\":0,\"order_type\":2,\"goods_number\":1,\"is_gift\":0,\"gift_code\":\"\",\"code\":\"\",\"code_id\":0,\"code_name\":\"\",\"reduce_price\":0,\"is_seckill\":0,\"is_pinhuo\":0,\"is_zhuanxiang\":0,\"promotion_dimension_id\":0,\"pinhuo_code\":\"\",\"is_groupon\":0,\"promotion_id\":null}}",
"shipping_rules": "{\"shipFeeList\":[{\"id\":105,\"gapToFree\":0,\"amountToFree\":0,\"shipFee\":0,\"products\":[{\"isGift\":0,\"cartId\":0,\"productId\":10750}],\"isFree\":1,\"ruleName\":\"\\u6ee188\\u5305\\u90ae\"}],\"totalFee\":0}",
"tracking_data": "{\"26\":\"c73400f06fe6f3c9796003c08a0f5a6d\"}",
"timestamp": "1484195335",
"api_key": "xsx",
"api_sign": "27DBBE360E67E638B6836B7FFBCBE061"
}




data_createOrderXsx ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{\"order\":"
                  "{\"serial_no\":\"14841953352617914717\","
                  "\"user_id\":1160,\"uid\":43507844,"
                  "\"source\":\"wap\","
                  "\"referer\":\"windows|wap|192.168.14.61\","
                  "\"source_type\":1,"
                  "\"pid\":\"c73400f06fe6f3c9796003c08a0f5a6d\","
                  "\"trade_pwd\":\"\","
                  "\"surplus\":\"40.00\"},"
                  "\"address\":{\"address_id\":\"1724\","
                  "\"customs_id\":\"3474\","
                  "\"address_type\":\"0\","
                  "\"consignee\":\"\\u674e\\u56db\","
                  "\"mobile\":\"13728142737\","
                  "\"province\":\"1\",\"city\":\"37\",\"district\":\"0\",\"country\":\"0\","
                  "\"address\":\"\\u81ea\\u8d2d\\u8fd4\\u73b0\",\"is_default\":\"0\"},"
                  "\"customs\":{\"is_customs\":\"2\","
                  "\"customs_info\":{\"card_id\":\"440921199201184218\",\"customs_id\":\"3474\"},"
                  "\"customs_pic\":{\"id\":\"3474\",\"identit_card\":\"440921199201184218\","
                  "\"img_front_original\":\"identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg\","
                  "\"img_front_max\":\"identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg\","
                  "\"img_front_thumb\":\"identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg\","
                  "\"img_back_original\":\"identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg\","
                  "\"img_back_max\":\"identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg\","
                  "\"img_back_thumb\":\"identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg\"}}}",
    "goods_list": "{\"10750\":{\"goods_id\":\"777\","
                  "\"product_id\":\"10750\",\"product_sn\":\"cp0000001234\","
                  "\"goods_name\":\"\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539\","
                  "\"goods_sn\":\"XSX000777\",\"goods_own_type\":\"1\",\"shop_price\":40,\"market_price\":\"52.00\","
                  "\"is_on_sale\":\"1\",\"is_delete\":\"0\",\"is_customs\":\"2\",\"product_number\":\"129\","
                  "\"ext_price\":\"0.00\",\"delivery_method\":\"19\",\"goods_weight\":\"1.000\","
                  "\"cdn_status\":\"1\","
                  "\"goods_thumb\":\"https:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg\",\"order_quota\":\"100\",\"is_real\":\"1\","
                  "\"supplier_id\":\"128\",\"without_return\":\"0\",\"erp_goods_id\":\"0\",\"app_id\":\"0\","
                  "\"cat_id\":\"25\",\"shelf_life\":\"0\",\"shelf_life_start\":\"0\",\"sms_delivery\":\"0\","
                  "\"coupons\":\"0\",\"coupons_verificat\":\"0\",\"return_anytime\":\"0\",\"brand_id\":\"3\","
                  "\"goods_attr\":[\"\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801\",\" \\n\"],"
                  "\"goods_attr_id\":\"2777\",\"isDistribution\":0,\"order_type\":2,\"goods_number\":1,\"is_gift\":0,\"gift_code\":\"\",\"code\":\"\","
                  "\"code_id\":0,\"code_name\":\"\",\"reduce_price\":0,\"is_seckill\":0,\"is_pinhuo\":0,\"is_zhuanxiang\":0,"
                  "\"promotion_dimension_id\":0,\"pinhuo_code\":\"\",\"is_groupon\":0,\"promotion_id\":null}}",
    "shipping_rules": "{\"shipFeeList\":[{\"id\":105,\"gapToFree\":0,\"amountToFree\":0,\"shipFee\":0,"
                      "\"products\":[{\"isGift\":0,\"cartId\":0,\"productId\":10750}],"
                      "\"isFree\":1,\"ruleName\":\"\\u6ee188\\u5305\\u90ae\"}],\"totalFee\":0}",
    "tracking_data": "{\"26\":\"c73400f06fe6f3c9796003c08a0f5a6d\"}",
    "timestamp": times,
    "api_key": "xsx",
    "api_sign": "27DBBE360E67E638B6836B7FFBCBE061"
}























































































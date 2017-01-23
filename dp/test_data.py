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


#点评相关接口

#成功创建订单
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


'''点评验卷接口'''
data_DPverif={
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'data':'{"supplierId":1,"couponIds":[2447]}'
}
'''获取用户订单列表-点评项目'''
data_UserOrderListDP={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'uid':'43507844',
     'order_cate_id':'[2001,2006]'
}
'''点评取消订单'''

cancelOrder_data={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'timestamp':times,
     'uid':'43507844',

}
'''用户申请退款-点评项目'''
applyRefund_data={
    'timestamp':times,
    'uid':'43507844',
    'suggest_reason':'122',
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',

}
'''订单详情-点评项目'''
OrderBySnDianping_data={
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',
    'order_sn':'DP48414731026869',
}



'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_sn':'DP08414562386338',
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

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























































































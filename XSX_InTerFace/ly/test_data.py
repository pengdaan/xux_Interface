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



#旅游相关接口

'''test:获取用户所有的订单列表'''
test_UserOrderListTour={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':'43507844',
        'page_num':'1',
        'page_size':'20',
        'status':'100',
        'order_cate_id':'[2001,2002,2003,2004]'
    }
'''test:根据订单分类获取分类订单总数'''
test_UserOrderNums={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':43507844,
        'order_cate_id':'[2001,2002,2003,2004,2006]'
    }
'''旅游通过出行日期查询已支付的订单'''
test_OrderByGoTime={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'time':time,
     'go_time':'2016-10-26',
     'extra_fields':'["refund","delivery"]'

}
'''旅游根据订单编号获取订单信息'''
test_OrderBySnTour={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':time,
    'order_sn':'LY67414946235558'

}















































'''小树熊下单'''
data_createOrderXsx1 ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{"
                  "XUX_OrderApi:{serial_no:14841953352617914717,"
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
    "order_info": "{\"XUX_OrderApi\":"
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























































































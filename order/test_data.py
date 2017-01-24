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

'''用户申请退款-点评项目'''
applyRefund_data={
    'timestamp':times,
    'uid':'43507844',
    'order_sn':'DP48414731026869',
    'suggest_reason':'122',
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',

}

'''获取用户商品下单商品数量'''
UserLimitedSpecialOrderNum_data={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'timestamp':times,
     'uid':'43507844',
     'promotion_id':'158',
     'goods_id':'714',
     'order_cate':'1101'

}

'''接收open域回推要出发订单信息'''
receiveOrderReturn_data={
    'order_sn':'LY48414722526789',
    't':'1484722585',
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'type':'0',
    'status':'1'
}

'''根据订单号获取订单列表'''
ChildOrderTour_data={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'order_sn':'LY48414726526809 '
}

'''获取用户购买的商品数量'''
OrderGoodsNumTour_data={
    'api_key':'8d46b75a4a0456a35302d2893ed072a3',
    'timestamp':times,
    'goods_id':743,
    'uid':43507844,
    'passenger':'[{"phone":"13728142737","type":1}]'

}

'''小树熊下单'''
data_createOrderXsx ={
    "_url": "/Order/createOrderXsx",
    "order_info": "{\"order\":{\"serial_no\":\"14848002314991236655\",\"user_id\":1160,\"uid\":43507844,\"source\":\"wap\",\"referer\":\"windows|wap|192.168.14.61\",\"source_type\":1,\"pid\":0},\"address\":{\"address_id\":\"1724\",\"customs_id\":\"3474\",\"address_type\":\"0\",\"consignee\":\"\\u63a5\\u53e3\\u6d4b\\u8bd5\",\"mobile\":\"13728142737\",\"province\":\"1\",\"city\":\"37\",\"district\":\"0\",\"country\":\"0\",\"address\":\"\\u81ea\\u8d2d\\u8fd4\\u73b0\",\"is_default\":\"1\"},\"customs\":{\"is_customs\":\"2\",\"customs_info\":{\"card_id\":\"440921199201184218\",\"customs_id\":\"3474\"},\"customs_pic\":{\"id\":\"3474\",\"identit_card\":\"440921199201184218\",\"img_front_original\":\"identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg\",\"img_front_max\":\"identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg\",\"img_front_thumb\":\"identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg\",\"img_back_original\":\"identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg\",\"img_back_max\":\"identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg\",\"img_back_thumb\":\"identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg\"}}}",
    "goods_list": "{\"10750\":{\"goods_id\":\"777\",\"product_id\":\"10750\",\"product_sn\":\"cp0000001234\",\"goods_name\":\"\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539\",\"goods_sn\":\"XSX000777\",\"goods_own_type\":\"1\",\"shop_price\":40,\"market_price\":\"52.00\",\"is_on_sale\":\"1\",\"is_delete\":\"0\",\"is_customs\":\"2\",\"product_number\":\"9991\",\"ext_price\":\"0.00\",\"delivery_method\":\"19\",\"goods_weight\":\"1.000\",\"cdn_status\":\"1\",\"goods_thumb\":\"http:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg\",\"order_quota\":\"100\",\"is_real\":\"1\",\"supplier_id\":\"128\",\"without_return\":\"0\",\"erp_goods_id\":\"0\",\"app_id\":\"0\",\"cat_id\":\"25\",\"shelf_life\":\"0\",\"shelf_life_start\":\"0\",\"sms_delivery\":\"0\",\"coupons\":\"0\",\"coupons_verificat\":\"0\",\"return_anytime\":\"0\",\"brand_id\":\"3\",\"goods_attr\":[\"\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801\",\" \\n\"],\"goods_attr_id\":\"2777\",\"isDistribution\":0,\"order_type\":2,\"goods_number\":1,\"is_gift\":0,\"gift_code\":\"\",\"code\":\"\",\"code_id\":0,\"code_name\":\"\",\"reduce_price\":0,\"is_seckill\":0,\"is_pinhuo\":0,\"is_zhuanxiang\":0,\"promotion_dimension_id\":0,\"pinhuo_code\":\"\",\"is_groupon\":0,\"promotion_id\":null}}",
    "shipping_rules": "{\"shipFeeList\":[{\"id\":105,\"gapToFree\":0,\"amountToFree\":0,\"shipFee\":0,\"products\":[{\"isGift\":0,\"cartId\":0,\"productId\":10750}],\"isFree\":1,\"ruleName\":\"\\u6ee188\\u5305\\u90ae\"}],\"totalFee\":0}",
    "tracking_data": "[]",
    "timestamp": "1484800231",
    "api_key": "xsx",
    "api_sign": "B73BD177D4C17426ACD08C0C9E2E29E4"

}

'''根据订单号获取订单详情接口'''
OrderBySn_data={

      'api_key':'b47d4503ce201db6df525911812dd089',
      'order_sn':'XS58414070929679 ',

}

'''订单直接分单发货'''
normalShip_data={
        'api_key':'b47d4503ce201db6df525911812dd089',
        'timestamp':times,
        'order_sn':'LY58414141329699',
        'wms_info':'[{"shipping_id": "12","invoice_no": "EMS12345678","type": 1},{"shipping_id": "13","invoice_no": "EMS654321","type": 2}]'



}



'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'40',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}


























































































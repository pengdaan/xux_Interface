# -*- coding: utf-8 -*-
import time
import datetime
times= int(time.time())
createOrderTour_url='http://www.xiaoshuxiong.com/api/order/createOrderTour'
updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
orderXUX_url="http://order.api.xiaoshuxiong.com/Order/createOrderXsx"
PMSadd_url="http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add"
BatchSend_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/code/batchSend'




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

'''旅游创建订单'''
createOrderTour_data={
    "uid": "43507844",
    "consignee": "刘德华",
    "postscript": "",
    "source_type": "1",
    "version": "2.0",
    "passenger": "[{\"contact_type\":2,\"email\":\"\",\"identit_card\":\"\",\"passenger_name\":\"刘德华\",\"passenger_type\":1,\"phone\":\"13728142737\"}]",
    "timestamp": times,
    "track_param": "{}",
    "source": "pc",
    "products": "[{\"base_day\":1,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"主套餐1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1798,\"item_name\":\"主套餐1\",\"item_num\":1,\"item_timestamp\":1484553897,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131608,\"product_sn\":\"tour_131608\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":10.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"N选1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1799,\"item_name\":\"N选1\",\"item_num\":1,\"item_timestamp\":1484553924,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131624,\"product_sn\":\"tour_131624\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":1.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"包含 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1800,\"item_name\":\"包含\",\"item_num\":1,\"item_timestamp\":1484553929,\"item_type\":0,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131628,\"product_sn\":\"tour_131628\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":0.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1}]",
    "sms_param": "{\"delivery\":{\"1251\":{\"enabled\":0,\"supplier_phone\":\"111111\",\"destination\":\"深圳市南山区深南大道华侨城欢乐谷\"}}}",
    "mobile": "13728142737",
    "api_key": "9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o",

}


'''成功创建订单，不发卷'''
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


'''成功创建订单,发卷'''
data_OrderDPSuce={
    "timestamp":times,
    "uid": "43507844",
    "consignee": "么么22",
    "mobile": "13728142737",
    "shop_id": "1",
    "products": "[{\"product_id\":\"10860\",\"goods_id\":\"870\",\"product_sn\":\"product2017021610860\",\"goods_name\":\"\\u6d4b\\u8bd5\\u5546\\u54c1_02(\\u53d1\\u5377)\",\"cat_id\":\"483\",\"shop_price\":\"10.00\",\"goods_thumb\":\"\\/\\/cdn-dianping.mama.cn\\/upload\\/http:\\/\\/cdn-dianping.mama.cn\\/upload\\/201702\\/20170206\\/2a572c38539179823fc795d455e9b526.jpg\",\"supplier_id\":\"1\",\"without_return\":\"0\",\"goods_number\":\"1\",\"use_coupon\":\"3\",\"end_return_time\":\"0\",\"return_anytime\":\"0\",\"goods_attr_id\":\"3080|3081\",\"goods_attr\":\"\\u989c\\u8272:\\u7ea2\\u8272|\\u7801\\u6570:38\"}]",
    "source": "wap",
    "shop_city": "1",
    "pay_expire": "7200",
    "version": "2.1",
    "api_key": "8d46b75a4a0456a35302d2893ed072a3",

}


'''更新订单支付状态'''
data_updatePayStatus_ly = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'11',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}


'''更新订单支付状态'''
data_updatePayStatus = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}
'''更新小树熊订单支付状态'''
data_updatePayStatus_xsx = {
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_amount':'40',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}


'''批量发放优惠卷接口'''
batchSend_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495,"num":1,"mark":"","type":0,"userIds":[1181],"adminId":1}'
}


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

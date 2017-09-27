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


add_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))# 获取当前时间。
promotionNames=str(add_time) + 'Test_AddPms'

Title=str(add_time)+'Test_AddPms'
dingjintuanTitle = str(add_time)+'Test_DJTuan'



#www域接口

'''更新订单支付状态'''
def data_updatePayStatus(order_sn,order_amount):
    data_updatePayStatus = {
        'api_key':'b47d4503ce201db6df525911812dd089',
        'timestamp':times,
        'order_sn':''+order_sn+'',
        'order_amount':''+order_amount+'',
        'trade_no':'2015122921001003610003783823',
        'pay_serial_no':'2015122964844',
        'pay_id':'1',
        'order_status':'1',
        }
    return data_updatePayStatus

'''通过商品id获取订单列表'''
data_OrderByProductId={
    'api_key':'d81b8598bc36a686cc8cbbd26599bd92',
    'uid':'43507844',
    'product_id':'10750',
    'goods_id':'777',
}

'''旅游创建订单，已弃用'''
createOrderTour_data1={
    "_url": "/order/createOrderTour",
    "uid": "43507844",
    "invoice_info": "{\"content\":\"\",\"type\":0}",
    "postscript": "",
    "consignee": "彭先生",
    "source_type": "5",
    "promotion_info": "[]",
    "version": "2.1",
    "passenger": "[{\"contact_type\":2,\"email\":\"\",\"identit_card\":\"\",\"passenger_name\":\"彭先生\",\"passenger_type\":1,\"phone\":\"13728142738\"}]",
    "timestamp": "1505383689",
    #"timestamp": times,
    "track_param": "{}",
    "source": "pc",
    "products": "[{\"base_day\":1,\"base_num\":1,\"cat_id\":5,\"city\":537,\"coupons_opportunity\":21,\"district\":0,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-09-17\",\"goods_attr\":\"主套餐 2017-09-17\",\"goods_id\":3786,\"goods_name\":\"出境游-西安曲江国际旅行社有限公司-支付测试子商品\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/349946df7486ebe68df41de9f8ccfd8f.jpg\",\"is_main\":1,\"item_id\":28818,\"item_name\":\"主套餐\",\"item_num\":1,\"item_timestamp\":1505184429,\"item_type\":1,\"parent_id\":1739,\"parent_name\":\"出境游支付测试商品（勿动）-目的地\",\"product_id\":168213,\"product_sn\":\"tour_168213\",\"province\":35,\"purchaser_id\":20,\"purchaser_name\":\"重庆站\",\"receive_opportunity\":31,\"resource_id\":\"0\",\"shop_price\":0.10,\"smsText\":\"\",\"smsType\":\"1,2\",\"supplier_id\":1495,\"supplier_name\":\"西安曲江国际旅行社有限公司\",\"ticket\":4,\"use_coupon\":4,\"useday\":\"\",\"without_return\":1}]",
    "sms_param": "{\"delivery\":{\"3786\":{\"enabled\":1,\"send_coupons\":4,\"supplier_phone\":\"8888888888\"}}}",
    "mobile": "13728142738",
    "appkey": "9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o",
    #"sign": "6A4F51590E1F3B0064C9C8C99F84D63B"
}

createOrderTour_data={
    "_url": "/order/createOrderTour",
    "uid": "43507844",
    "invoice_info": "{\"content\":\"\",\"type\":0}",
    "postscript": "",
    "consignee": "彭先生",
    "source_type": "5",
    "promotion_info": "[]",
    "version": "2.1",
    "passenger": "[{\"contact_type\":2,\"email\":\"\",\"identit_card\":\"\",\"passenger_name\":\"彭先生\",\"passenger_type\":1,\"phone\":\"13728142738\"}]",
    "timestamp": "1505372929",
    "track_param": "{}",
    "source": "pc",
    "products": "[{\"base_day\":1,\"base_num\":1,\"cat_id\":5,\"city\":537,\"coupons_opportunity\":21,\"district\":0,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-09-17\",\"goods_attr\":\"主套餐 2017-09-17\",\"goods_id\":3786,\"goods_name\":\"出境游-西安曲江国际旅行社有限公司-支付测试子商品\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-ly.mama.cn/349946df7486ebe68df41de9f8ccfd8f.jpg\",\"is_main\":1,\"item_id\":28818,\"item_name\":\"主套餐\",\"item_num\":1,\"item_timestamp\":1505184429,\"item_type\":1,\"parent_id\":1739,\"parent_name\":\"出境游支付测试商品（勿动）-目的地\",\"product_id\":168213,\"product_sn\":\"tour_168213\",\"province\":35,\"purchaser_id\":20,\"purchaser_name\":\"重庆站\",\"receive_opportunity\":31,\"resource_id\":\"0\",\"shop_price\":0.10,\"smsText\":\"\",\"smsType\":\"1,2\",\"supplier_id\":1495,\"supplier_name\":\"西安曲江国际旅行社有限公司\",\"ticket\":4,\"use_coupon\":4,\"useday\":\"\",\"without_return\":1}]",
    "sms_param": "{\"delivery\":{\"3786\":{\"enabled\":1,\"send_coupons\":4,\"supplier_phone\":\"8888888888\"}}}",
    "mobile": "13728142738",
    "appkey": "9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o",
    "sign": "EFC15AACA09B3D33EE40014E66A0FDA0"
}










'''获取秒杀订单实际秒杀购买数'''
PromotionNums_data={
      'api_key':'b47d4503ce201db6df525911812dd089',
      'timestamp':times,
      'data':'{"promotion_type":2,"promotion_id":62}'
}
'''更新订单客服留言接口'''
updateRemindMsg_data={
      'api_key':'b47d4503ce201db6df525911812dd089',
      'timestamp':times,
      'order_sn':'XS48414708726629 ',
      'msg_ids':'[1,2,3]'
}
'''获取订单客服留言'''
RemindMsg_data={
     'api_key':'b47d4503ce201db6df525911812dd089',
     'timestamp':times,
     'order_sn':'XS48414708726629'

}

'''对接要出发回调设置外部订单号'''
def OutOrderSn_data(Order_sn):
    OutOrderSn_data={
        'api_key': '9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        't':times,
        'out_order_sn':times,
        'order_sn':''+Order_sn+''
    }
    return OutOrderSn_data

'''根据订单号获取订单列表'''
ChildOrderTour_data={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'order_sn':'LY10514212034040'
}



'''根据订单分类获取分类订单总数'''
UserOrderNums_data={
      'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
      'uid':'43507844',
      'order_cate_id':'[2001,2002,2003,2004]'

}

'''获取用户购买的促销订单信息'''
OrderPromotionList_data={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':times,
    'uid':'43507844',
    'promotion_id':'33733',
    'promotion_type':'1'

}

'''获取订单来源参数列表'''
G_dingdan_data={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,

}


'''验证使用消费券'''
def couponId():
    coupon=random.randint(1000000, 10000000)
    return coupon


def verify_data(order_sn,couponId):
    verify_data={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'timestamp':times,
        'data':'{"supplierId":100,"orderId":"'+str(order_sn)+'","couponIds":["'+str(couponId)+'"]}'
    }
    return verify_data

getStock={
     'api_key':'402a61732af2bf0b8df1cb9a12ae2b29',
     'timestamp':times,
     'data':'{"productSn":"952841-00016-04","warehouseAreaCode":2}',
     'sys':'7'
}


'''不输入消费券直接发货'''
def ShipWithoutCoupon_data(order_sn,orderId):
    shipWithoutCoupon_data={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'timestamp':times,
        'order_sn':''+ str(order_sn) + ' ',
        'data':'{"supplierId":110,"orderId":'+ str(orderId) + '}'
    }
    return shipWithoutCoupon_data


'''发送消费券'''
def ship_data(orderId,coupon):
     coupons_ship=str(coupon)
     ship_data={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'timestamp':times,
        'data':'{"supplierId":110,"orderId":'+ str(orderId) + ',"coupons":["'+str(coupons_ship)+'"]}'
    }
     return ship_data

'''重复发放消费卷'''
def Add_XUJ_data(orderId):
    coupon=random.randint(100000, 1000000)
    Add_data={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'timestamp':times,
        'data':'{"supplierId":110,"orderId":"'+ str(orderId) + '","coupons":["'+str(coupon)+'"]}'
    }
    return Add_data

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
'''获取商品信息'''
InfoByGoodsId={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'goods_id':'777'
}


test_data='content=<Request>' \
                  '<MailTotalCount></MailTotalCount>' \
                  '<Sign_Code>M00136337385</Sign_Code>' \
                  '<OutInFlag>5</OutInFlag>' \
                  '<Cust_OrderCode>20170703151580697</Cust_OrderCode>' \
                  '<WMS_OrderID>3204180232</WMS_OrderID>' \
                  '<CustID>1300007873</CustID>' \
                  '<TmsCode></TmsCode>' \
                  '<TmsName></TmsName>' \
                  '<MailNo>3204180232</MailNo>' \
                  '<Weight>9.5900</Weight>' \
                  '<Volume>0.0000</Volume>' \
                  '<PlanID>00030010</PlanID>' \
                  '<StockID>B03L00</StockID>' \
                  '<InfoCode>0006</InfoCode>' \
                  '<InfoContent>已发货</InfoContent>' \
                  '<Reason></Reason>' \
                  '<Message></Message>' \
                  '<StatusTime>2017-07-01 16:03:39</StatusTime>' \
                  '<Invoice_No></Invoice_No>' \
                  '<InvoiceDate></InvoiceDate>' \
                  '<OrderItems></OrderItems>' \
                  '</Request>'



'''获取商品信息--批量'''
InfoByGoodsIds={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'goods_ids':'777,778'}

'''获取sku价格和库存（通过商品id）'''
GoodsSkuByGoodsId={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'goods_id':'777'


}

'''获取sku价格和库存（通过商品id）—批量'''
GoodsSkuByGoodsIds={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'goods_ids':'777,778'


}

'''获取sku价格和库存（通过货品id）'''
GoodsSkuByProductsId={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'product_id': '10750'

}

'''获取sku价格和库存（通过货品id）—批量）'''
GoodsSkuByProductsIds={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'product_ids': '10750,10751'

}
'''进货价批量查询'''
pageBatch={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'page_param':'[{"supplier_id":1343,"product_sn":"tour_162126"}]'

}

'''进货价新增-批量'''
batchInsert={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'purchase_price':'[{"purchase_price":25.00,"sku_name":"广仁寺门票（一证一票） 2017-11-7",'
                     '"supplier_id":1343,"product_sn":"tour_162127","effect_time":1498116035}]'}



'''进货价查询'''
PurchasePrice_page={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'page_num ':1,
    'page_size ':15,
    'supplier_id':1343,
    'product_sn':"tour_162126"

}
'''进货价编辑-批量'''
batchUpdate={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'purchase_price':'[{"purchase_price":25.00,"sku_name":"广仁寺门票（一证一票） 2017-11-7",'
                        '"supplier_id":1343,"product_sn":"tour_162127",'
                        '"effect_time":1498116035}]'
}

'''获取供应商下面的分类以及品牌信息'''
ReferInfo={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128
}

'''获取供应商所属品牌信息'''
BrandBySupplierId={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128

}

'''获取商品id列表'''
GoodsIdsbySnbc={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'goods_name':'接口测试'


}

'''获取商品品牌列表'''
BrandList={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times


}
'''获取商品所有分类(以树形展示返回)'''
getCatListTree={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times


}

'''获取商品的名称，品牌和分类名称 --批量'''
GoodsNbc={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'goods_ids':'777'

}

'''获取商品详情接口'''
GoodsBySupplierId={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128,
     'goods_id':777

}
'''获取商家下面的SKU列表'''
SkuListBySupplierId={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128,
     'page_num':1,
     'page_size':15

}
'''获取商家下面的商品列表'''
GoodsListBySupplierId={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128,
     'page_num':1,
     'page_size':15

}

'''获取商家所属栏目分类信息'''
CatBySupplierId={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'timestamp':times,
     'supplier_id':128
}

'''孕管首页获取清单商品信息'''
hygjList={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':times,
    'mode':1,
    'day':1

}

'''旅游--批量获取sku的信息'''
SkuByPidsTour={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'products_ids':'1343,1344'

}

'''旅游--批量获取子商品的信息'''
CommonGoodsByGidsTour={
    'api_key':'b47d4503ce201db6df525911812dd089',
     'goods_ids':'1343'

}

'''旅游--批量获取组合商品的详情'''
ByGidsTour={
    'api_key':'b47d4503ce201db6df525911812dd089',
     'goods_ids':'1343'

}
'''旅游--根据栏目ID获取筛选属性'''
CatAttrByCatIdTour={
    'api_key':'b47d4503ce201db6df525911812dd089',
     'cat_id':'40'

}

'''旅游--获取旅游栏目'''
CatTour={
     'api_key':'b47d4503ce201db6df525911812dd089',
}


AddCart={
    'timestamp':times,
    'data':'{"goods_id":777,'
           '"num":1,"session_id":"b318a3b72fe99fb9fccbe61bc0ae95ef",'
           '"goods_arr_ids":[2777],"user_id":0,'
           '"gift_code":"","product_id":"10750",'
           '"goods_arrs":"\u9ed8\u8ba4\u5c5e\u6027\uff1a\u5747\u7801|",'
           '"goods_price":40,"goods_sn":"XSX000777","goods_own_type":"1",'
           '"goods_name":"\u3010\u666e\u3011\u63a5\u53e3\u6d4b\u8bd5\u5546\u54c1_\u52ff\u52a8\u52ff\u6539",'
           '"market_price":"52.00","rec_type":"2","product_number":"7995","promotion_type":0,'
           '"promotion_id":0,"promotion_dimension_id":0}',
    'api_key':'b4c3ca6134255ce2e71586da794f4328'
}

'''对科捷回推回来的数据进行筛选，如果是系统内有记录的批次则同步'''
yncStock_Data={
    'timestamp':times,
    'sku_list':'[{ "stock_id":"0600",'
               '"sku_product_no":"233",'
               '"sku_batch_no":"CG-00001",'
               '"sku_inuse_inventory":"7.0000",'
               '"sku_qty":"600.0000","goods_own_type":"2"},'
               '{"stock_id":"0600",'
               '"sku_product_no":"233",'
               '"sku_batch_no":"CG-00001",'
               '"sku_inuse_inventory":"0.0000",'
               '"sku_qty":"200.0000",'
               '"goods_own_type":"1"},'
               '{"stock_id":"0600",'
               '"sku_product_no":"20170518",'
               '"sku_batch_no":"CG-00001",'
               '"sku_inuse_inventory":"0.0000",'
               '"sku_qty":"300.0000",'
               '"goods_own_type":"1"},'
               '{"stock_id":"0600",'
               '"sku_product_no":"20170518",'
               '"sku_batch_no":"CG-00001",'
               '"sku_inuse_inventory":"0.0000",'
               '"sku_qty":"40.0000",'
               '"goods_own_type":"1"}]'
}














































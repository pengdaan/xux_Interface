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
    "products": "[{\"base_day\":1,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"主套餐1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-Ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1798,\"item_name\":\"主套餐1\",\"item_num\":1,\"item_timestamp\":1484553897,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131608,\"product_sn\":\"tour_131608\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":10.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"N选1 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-Ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1799,\"item_name\":\"N选1\",\"item_num\":1,\"item_timestamp\":1484553924,\"item_type\":1,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131624,\"product_sn\":\"tour_131624\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":1.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1},{\"base_day\":0,\"base_num\":1,\"extend_id\":\"\",\"extend_link\":\"\",\"go_time\":\"2017-01-19\",\"goods_attr\":\"包含 2017-01-19\",\"goods_id\":1251,\"goods_name\":\"【东北 | 雪国列车】-出行1\",\"goods_number\":1,\"goods_thumb\":\"http://cdn-Ly.mama.cn/59bc4788c02a51deb4e93362e7350a54.gif\",\"item_id\":1800,\"item_name\":\"包含\",\"item_num\":1,\"item_timestamp\":1484553929,\"item_type\":0,\"parent_id\":743,\"parent_name\":\"常用旅客---测试\",\"product_id\":131628,\"product_sn\":\"tour_131628\",\"purchaser_id\":5,\"purchaser_name\":\"总部—宋龙辉\",\"shop_price\":0.00,\"smsText\":\"\",\"smsType\":\"2\",\"supplier_id\":110,\"supplier_name\":\"旅游供应商(成本结算)\",\"ticket\":1,\"use_coupon\":1,\"without_return\":1}]",
    "sms_param": "{\"delivery\":{\"1251\":{\"enabled\":0,\"supplier_phone\":\"111111\",\"destination\":\"深圳市南山区深南大道华侨城欢乐谷\"}}}",
    "mobile": "13728142737",
    "api_key": "9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o",

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
     'order_sn':'LY48414726526809 '
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

<<<<<<< HEAD
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
=======
}

'''获取商品信息--批量'''
InfoByGoodsIds={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'goods_ids':'777,778'
>>>>>>> d9b1926d63bdfe279356feaa6bfa926bd4ddf105

}

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
















































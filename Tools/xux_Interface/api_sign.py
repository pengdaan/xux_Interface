# -*- coding: utf-8 -*-
import hashlib
import time
times= int(time.time())
username='么么22'
uids='43507844'

'''国际发货'''
payloads ={
        'api_key':'d81b8598bc36a686cc8cbbd26599bd92',
        'timestamp':times,
        'data':'{'
        '"actionUser": "15915968257@qq.com",'
        '"orderId": 10711,'
        '"supplierId": 24,'
        '"wmsInfo": [{'
        '"invoiceNo": "GT3123123",'
        '"orderId": 0,'
        '"shippingId": 13,'
        ' "type": 2},'
        '{'
        '"invoiceNo": "GR3123123",'
        ' "orderId": 0,'
        ' "shippingId": 8,'
        '"type": 1}],'
        '"wmsInfoStr": [{'
        '"invoiceNo":"GT3123123",'
        '"shippingId":"13","type":"2"},'
        '{"invoiceNo":"GR3123123",'
        '"shippingId":"8","type":"1"'
        ' }]'
        '}'
}


payload14 ={
    'order_sn': 'LY48414722526789',
    't':times,
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'type':'1',
    'status':'1'
}

payload={
    'timestamp':times,
    'uid':'43507844',
    'order_sn':'DP48414731026869',
    'suggest_reason':'122',
    'appkey':'8d46b75a4a0456a35302d2893ed072a3'

}


payload ={
    "order_info": "{'order':{'serial_no':'14848002314991236655','user_id':1160,'uid':43507844,'source':'wap','referer':'windows|wap|192.168.14.61','source_type':1,'pid':0},'address':{'address_id':'1724','customs_id':'3474','address_type':'0','consignee':'\\u63a5\\u53e3\\u6d4b\\u8bd5','mobile':'13728142737','province':'1','city':'37','district':'0','country':'0','address':'\\u81ea\\u8d2d\\u8fd4\\u73b0','is_default':'1'},'customs':{'is_customs':'2','customs_info':{'card_id':'440921199201184218','customs_id':'3474'},'customs_pic':{'id':'3474','identit_card':'440921199201184218','img_front_original':'identit_card\\/original_10dba1499d2e72e1c5e0c7345dcb7e3f.jpg','img_front_max':'identit_card\\/max_1bdaf04b61d9cdc5ecd4deb1ba1e28ac.jpg','img_front_thumb':'identit_card\\/thumb_abf6163039e3f3b035546f81c565f0fb.jpg','img_back_original':'identit_card\\/original_945a264a54944207f124ee62a20fbaf2.jpg','img_back_max':'identit_card\\/max_0ef88ad15a28f791e632c04925258a9d.jpg','img_back_thumb':'identit_card\\/thumb_7cd66cb9b1033ba540ef72c3d72fc6b7.jpg'}}}",
    "goods_list": "{'10750':{'goods_id':'777','product_id':'10750','product_sn':'cp0000001234','goods_name':'\\u3010\\u666e\\u3011\\u63a5\\u53e3\\u6d4b\\u8bd5\\u5546\\u54c1_\\u52ff\\u52a8\\u52ff\\u6539','goods_sn':'XSX000777','goods_own_type':'1','shop_price':40,'market_price':'52.00','is_on_sale':'1','is_delete':'0','is_customs':'2','product_number':'9991','ext_price':'0.00','delivery_method':'19','goods_weight':'1.000','cdn_status':'1','goods_thumb':'http:\\/\\/cdn.xiaoshuxiong.com\\/images\\/201604\\/thumb_img\\/777_thumb_P_1461658613884.jpg','order_quota':'100','is_real':'1','supplier_id':'128','without_return':'0','erp_goods_id':'0','app_id':'0','cat_id':'25','shelf_life':'0','shelf_life_start':'0','sms_delivery':'0','coupons':'0','coupons_verificat':'0','return_anytime':'0','brand_id':'3','goods_attr':['\\u9ed8\\u8ba4\\u5c5e\\u6027\\uff1a\\u5747\\u7801',' \\n'],'goods_attr_id':'2777','isDistribution':0,'order_type':2,'goods_number':1,'is_gift':0,'gift_code':'','code':'','code_id':0,'code_name':'','reduce_price':0,'is_seckill':0,'is_pinhuo':0,'is_zhuanxiang':0,'promotion_dimension_id':0,'pinhuo_code':'','is_groupon':0,'promotion_id':null}}",
    "shipping_rules": "{'shipFeeList':[{'id':105,'gapToFree':0,'amountToFree':0,'shipFee':0,'products':[{'isGift':0,'cartId':0,'productId':10750}],'isFree':1,'ruleName':'\\u6ee188\\u5305\\u90ae'}],'totalFee':0}",
    "tracking_data": "[]",
    "timestamp": times,
    "api_key": "xsx",


}
def api_sign():
    api_sign=[]
    for (key,value) in payload.items():
        api_sign.append( key +str(value))
    #print api_sign
    api_sign.sort()#获取所有键值对，并升序排列
    #print  api_sign
    api_signs = "".join(api_sign)
    #print '获取HTTP请求的所有键值对，并升序排列 :'  + api_signs #获取HTTP请求的所有键值对，并升序排列
    api_secret='9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o'#这个参数在mall_app
    pj=api_secret+api_signs+api_secret
    #print '字符串拼接：       '+ pj
    # #拼接后字符串反转义
    pj = pj.replace("\\n", "\n")
    pj = pj.replace("\\r", "\n")
    pj = pj.replace("\\", "")
    #print'拼接后字符串反转 :'+ pj
    md5jm= hashlib.new("md5", pj).hexdigest()
    #print md5jm
    #print md5jm.upper()#然后把加密内容转换为大写
    return md5jm.upper()




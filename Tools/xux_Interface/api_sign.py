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



def api_sign():
    api_sign=[]
    for (key,value) in payload.items():
        api_sign.append( key +str(value))
    #print api_sign
    api_sign.sort()#获取所有键值对，并升序排列
    #print  api_sign
    api_signs = "".join(api_sign)
    #print '获取HTTP请求的所有键值对，并升序排列 :'  + api_signs #获取HTTP请求的所有键值对，并升序排列
    api_secret='8f720e0f093400e2cfc355dc130a2d87'#这个参数在mall_app
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




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
#    'order_sn':'DP08414562386338',
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}

























































































# -*- coding: utf-8 -*-
__author__ = 'leo'


def headers(token):
    """
    模拟手机访浏览器访问小程序时的头文件
    """
    headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.3 NetType/WIFI Language/zh_CN',
    'token':''+token+'',
    }
    return headers

def uid(uid=None):
    """
    uid=none时使用默认的测试账号
    """
    if uid==None:
        Uid={
            'uid':76383768,
            }
    else:
        Uid={
            'uid':''+uid+'',
            }
    return Uid

'''获取商品基本信息'''
goodsDetail={
    'goods_id':'777'
}

'''商品接口获取sku弹窗信息'''
Buy={
    'goods_id':'777'
}

'''商品详情获取推荐商品'''
RecommendGoods={
    'goods_ids':'[777]',
    'pageType':'1'

}
'''良品tab'''''
TabQuery={
    'cat_id':'2',
    'page_num':'1',
    'page_size':'20'

}
'''入会手机号校验接口'''
mmcCheckMobile={
    'mobile':'13728142737'

}
'''加入购物车接口'''
add_Cart={
    'goods_id':'777',
    'sku':'2777',
    'number':'1'

}

'''批量删除购物车商品'''
batchDelete={
    'del_list[0][product_id]':'10750',
    'del_list[0][cart_id]':'30716'
}

'''更新购物车接口'''
update={
    'goods_id':'777',
    'product_id':'10750',
    'number':'2',
    'promotion_type':'0',
    'promotion_id':'0',
    'cart_id':'30761'

}
'''检查是否有待支付订单或重复提交'''
checkRepost={
    'is_cart':'1'
}

'''立即购买提交订单并支付'''
submitOrder={
    'goods_id':'33768',
    'goods_number':'1',
    'attr_id':'120587',
    'pid':'undefined',
    'address_id':'1767'

}


'''立即购买结算页接口'''
buynow={
    'attr_id':'2777',
    'address_id':'1767',
    'promotion_type':'0'

}

buynow_Test={
    'goods_id':'777',
    'goods_number':'1',
    'attr_id':'2777',
    'pid':'undefined',
    'address_id':'1767'


}


'''地址管理-删除地址'''
Address_delete={
    'consignee':'子曦',
    'mobile':'13728142737',
    'province':'440000',
    'city':'440100',
    'district':'440106',
    'address':'万菱汇 43楼',
    'is_customs':'3',
    'address_type':'3',
    'address_id':1783

}

'''地址管理-新增地址'''
Address_save={
    'consignee':'子曦',
    'mobile':'13728142737',
    'province':'440000',
    'city':'440100',
    'district':'440106',
    'address':'万菱汇 43楼',
    'is_customs':'3',
    'address_type':'3',


}




'''地址管理-获取单个地址'''
RowByID={

    'address_id':'1767'

}
'''地址管理-设默认地址'''
setDedault={

     'address_id':'1767'
}
'''我的优惠券-优惠券兑换'''
def coupon_Code(data):
    coupon_Code={
        'code':''+data+''
    }
    return coupon_Code

'''我的优惠券-优惠券分页'''
oupon_page={
    'page_num':1
}



'''我的返现'''
istribution_view={
    'type':2,
}

'''用户操作 - 发送手机绑定验证码'''
sendBindPhoneCode={
    'phone':'13728142737'
}

'''用户操作 - 检查手机绑定'''
checkBindPhone={
    'phone':'13728142737'
}


'''用户操作 - 绑定手机'''
doBindPhone={
    'phone':'13728142737',
    'code':'1581'

}

'''获取订单去支付信息'''
getOrderPayInfo={
    'order_sn':'XS89414643318620'
}

'''取消订单'''
def order_cancel(order_sn):
    order_cancel={
        'order_sn':''+order_sn+''
    }
    return order_cancel


'''订单操作 - 确认收货'''
receiveConfirm={
    'order_sn':'XS89414876019480'
}


'''我的返现-返现分页'''
distribution={
    'type':1,
    'page_num':1,
    'page_size':1
}

'''我的返现-页面'''
distribution_view={
    'type':3,

}
'''用户操作 - 发送手机绑定验证码'''
BindPhoneCode={
    'phone':'13728142737'
}



'''获取订单去支付信息'''
OrderPayInfo={
    'order_sn':'XS79414955414080'
}


'''获取订单去支付信息'''
Ordercancel={
    'order_sn':'XS79414955414080'
}


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
'''操作优惠活动（开启、关闭）接口 '''
test_Pmsoperate = {
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,

    'data':'{'
           '"promotionId": 454,'
           '"adminId": 1,'
           '"status": 2'
           ' }'
}


'''定金团4个时间处理机制：'''

'''1：定金支付时间直接使用当前时间戳'''
startAt=times

'''2.定金结束时间等于开始时间+15分钟'''
endAt=addTime()

'''3.尾款开始时间为定金结束时间+15分钟'''
fromAt=str(int(endAt)+600)

'''4.尾款结束时间为定金结束时间+15分钟'''
toAt=str(int(fromAt)+600)

'''新增定金团接口'''
CreateDepositMission_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{'
            '"photo":"images\/ms\/1484566379924518021.jpg",'
            '"goodsId":777,'
             '"title":"' + str(dingjintuanTitle) + '",'
             '"startAt":"'+ str(startAt) +'",'
             '"endAt":"'+ str(endAt) + '",'
             '"fromAt":"'+ str(fromAt) + '",'
             '"toAt":"'+ str(toAt) + '",'
             '"virtualHit":0,'
             '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0}'



}
'''修改定金团接口'''
updateDepositMission_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
    'data':'{'
        '"photo":"images\/ms\/1484566379924518021.jpg",'
        '"goodsId":777,"title":"2017-01-17 17:54:59Test_DJTuan",'
        '"startAt":1484646899,'
        '"endAt":1484647799,'
        '"fromAt":1484648399,'
        '"toAt":1484648999,'
        '"virtualHit":0,'
        '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0,"id":327}'
}
'''更新优惠劵状态'''
Pms_updateStatus={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionCode":"37076723","status":2,"orderId":"24594"}'


}

'''检查活动名称是否重复接口'''
NameRepeat_data={

    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"2017-01-19 18:25:49Test_DJTuan"}'

}


#暂时不用了
'''批量发放优惠卷接口'''
batchSend_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495,"num":1,"mark":"","type":0,"userIds":[1160],"adminId":1}'
}

#暂时不用了
'''发放优惠卷接口'''
Pmssend_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495,"num":10,"mark":"","type":1,"userId":1160,"adminId":1}'
}


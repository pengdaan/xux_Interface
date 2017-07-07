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

def PmsCode():
    P_list=random.randint(20000, 30000)
    return P_list

add_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))# 获取当前时间。
promotionNames=str(PmsCode()) + 'Test_AddPms'

Title=str(add_time)+'Test_AddPms'
PHT_Title=str(add_time)+'PHT'
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


'''秒杀预告时间'''
MS_noticeTime=str(int(startAt)+60)
'''秒杀开始时间'''
MS_startAtime=str(int(MS_noticeTime)+60)
'''秒杀结束时间'''
MS_endAtime=str(int(MS_startAtime)+600)




'''新增定金团接口'''
CreateDepositMission_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{'
             '"photo":"images\/ms\/1499069899723595235.png",'
             '"goodsId":33777,'
             '"title":"' + str(dingjintuanTitle) + '",'
             '"startAt":"'+ str(startAt) +'",'
             '"endAt":"'+ str(endAt) + '",'
             '"fromAt":"'+ str(fromAt) + '",'
             '"toAt":"'+ str(toAt) + '",'
             '"virtualHit":0,'
             '"products":[{"endPrice":"0.1",'
             '"fixPrice":"0.1","goodsId":"33777",'
             '"groupPrice":"0.2",'
             '"ladder":[{"personNumber":"1","price":"0.2"},'
             '{"personNumber":"2","price":"0.2"}],"productId":0},'
             '{"endPrice":0.1,"fixPrice":0.1,"goodsId":"33777","groupPrice":0.2,'
             '"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10984"}],'
             '"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0}'


}


'''修改定金团接口'''
def updateDepositMission_data(update_code,Title,startAt,endAt,fromAt,toAt):
    updateDepositMission_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{'
             '"photo":"images\/ms\/1499069899723595235.png",'
             '"goodsId":33777,'
             '"title":"' + str(Title) + '",'
             '"startAt":"'+ str(startAt) +'",'
             '"endAt":"'+ str(endAt) + '",'
             '"fromAt":"'+ str(fromAt) + '",'
             '"toAt":"'+ str(toAt) + '",'
             '"virtualHit":0,'
             '"products":[{"endPrice":"0.1",'
             '"fixPrice":"0.1","goodsId":"33777",'
             '"groupPrice":"0.2",'
             '"ladder":[{"personNumber":"1","price":"0.2"},'
             '{"personNumber":"2","price":"0.2"}],"productId":0},'
             '{"endPrice":0.1,"fixPrice":0.1,"goodsId":"33777","groupPrice":0.2,'
             '"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10984"}],'
             '"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0,"id":"'+str(update_code)+'"}'
    }
    return updateDepositMission_data

'''添加拼货团'''
createWithGoods_data={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
     'data':'{"photo": "data/brandlogo/1499070837797883380.png",'
            '"goodsId": 33778,'
            '"title":"' + str(PHT_Title) + '",'
            '"startAt":"'+ str(startAt) +'",'
            '"endAt":"'+ str(endAt) + '",'
            '"actionCount": 2,'
            '"supportFreeShipping": 1,'
            '"supportPromotion": 0,'
            '"supportSpecial": 1,'
            '"virtualHit": 0,'
            '"products": [{"goodsId": "33778","productId": 0,"selfLimit": 0,"selfPrice": 0.1,"stock": 50},'
            '{"goodsId": "33778","productId": "10985","selfLimit": 0,"selfPrice": 0.1,"stock": 50}],'
            '"operator": 1,"detail": "","sortOrder": 0}'}

'''添加限时专享_全部用户'''
createActivityAll_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"goodsId": 33780,'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt) + '",'
           '"operator": 1,'
           '"supportFreeShipping": 0,'
           '"rules": [{"userScope": "1","selfPrice": "20","stock": "200","selfLimit": "10",'
           '"ruleDiscription": "ALL_User"}],"pregnantStock": 0}'
}

'''添加限时专享_良粉用户'''
createActivityLF_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"goodsId":33781,'
           '"noticeAt":0,'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"operator":1,'
           '"supportFreeShipping":0,'
           '"rules":[{"userScope":"4","selfPrice":"20","stock":"500","selfLimit":"10",'
           '"ruleDiscription":"LF_User"}],"pregnantStock":0}'

}

'''添加限时专享_妈妈良品新客'''
createActivityNew_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"goodsId":33783,'
           '"noticeAt":0,'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"operator":1,'
           '"supportFreeShipping":0,'
           '"rules":[{"userScope":"3","selfPrice":"0","stock":"500","selfLimit":"10",'
           '"ruleDiscription":"XINKE"}],"pregnantStock":0}'

}


'''添加限时专享_3个月没有购买行为'''
createActivity3month_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"goodsId":33782,'
           '"noticeAt":0,'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"operator":1,'
           '"supportFreeShipping":0,'
           '"rules":[{"userScope":"2","selfPrice":"0","stock":"500","selfLimit":"10",'
           '"ruleDiscription":"3month"}],"pregnantStock":0}'

}

'''添加限时专享_妈妈新会员'''
createActivityNews_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"goodsId":33784,'
           '"noticeAt":0,'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"operator":1,'
           '"supportFreeShipping":0,'
           '"rules":[{"userScope":"5","selfPrice":"0","stock":"500","selfLimit":"10",'
           '"ruleDiscription":"New_LF"}],"pregnantStock":0}'

}

'''满减满赠活动_满减'''
fullcutPromotion_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"New_TestMJ",'
           '"promotionTitle":"New_TestMJ",'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"goods":[{"type":"5","value":33785}],'
           '"suitType":2,'
           '"condition":[{"conditionType":1,"conditionValue":10,"benefitName":"","benefitType":3,"benefitValue":"10"}],'
           '"operator":1}'

}


'''满减满赠活动_满赠'''
fullcutPromotionZ_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"New_TestMZ",'
           '"promotionTitle":"New_TestMZ",'
           '"startAt":"'+ str(startAt) +'",'
           '"endAt":"'+ str(endAt)+ '",'
           '"goods":[{"type":"5","value":33786}],'
           '"suitType":2,'
           '"condition":[{"conditionType":2,"conditionValue":1,"benefitName":"zengpin","benefitType":1,"benefitValue":"10983"}],'
           '"operator":1}'

}
'''创建秒杀活动'''
MS_save_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"msId":0,'
           '"msTitle":"Test_MS",'
           '"msPic":"",'
           '"startTime":"' + str(MS_startAtime) + '",'
           '"endTime":"' + str(MS_endAtime) + '",'
           '"noticeTime":"' + str(MS_noticeTime) + '",'
           '}'
}

'''添加秒杀商品到活动'''
def MSgoods_data(msId):
    MSgoods_data={
        'api_key':'647b00ec1fe6990b1b97263b05341b6b',
        'timestamp':times,
        'data':'{"goodsId":33779,'
           '"sort":1,'
           '"activity":"1",'
           '"msId":"' + str(msId) + '",'
           '"selfTitle":"MS_Goods01",'
           '"goodsInfo":[{"msInventory":20,"msLimit":100,"msPrice":5,"msStock":20,"productId":0},'
           '{"msInventory":10,"msLimit":100,"msPrice":"5.0","msStock":5,"productId":"10986"},'
           '{"msInventory":10,"msLimit":100,"msPrice":"5.0","msStock":1,"productId":"10987"}]}'
    }
    return MSgoods_data


'''添加预售'''
confict_data={
        'api_key':'647b00ec1fe6990b1b97263b05341b6b',
        'timestamp':times,
        'data':'{"goodsId":33768,'
               '"type":8,'
               '"startAt":"'+ str(startAt) +'",'
               '"endAt":"'+ str(endAt)+ '"}'

}



'''修改优惠劵状态'''
def Pms_updateStatus(promotionCodes):
    Pms_updateStatus={
        'api_key':'647b00ec1fe6990b1b97263b05341b6b',
        'timestamp':times,
        'data':'{"promotionCode":"'+str(promotionCodes)+'","status":2,"orderId":"28701"}'
    }
    return Pms_updateStatus


'''检查活动名称是否重复接口'''
NameRepeat_data={

    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"2017-01-19 18:25:49Test_DJTuan"}'

}


'''批量发放优惠卷接口'''
def BatchSend_data(id):
    batchSend_data={
        'api_key':'647b00ec1fe6990b1b97263b05341b6b',
        'timestamp':times,
        'data':'{"promotionId":'+str(id)+',"num":1,"mark":"","type":0,"userIds":[1181],"adminId":1}'
    }
    return batchSend_data

'''发放优惠卷接口'''
def Pmssend_data(id):
    Pmssend_data={
        'api_key':'647b00ec1fe6990b1b97263b05341b6b',
        'timestamp':times,
        'data':'{"promotionId":'+str(id)+',"num":10,"mark":"","type":1,"userId":1181,"adminId":1}'
    }
    return Pmssend_data


'''获取指定优惠活动信息接口'''
Pmsinfo_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495}'
}
'''获取用户的优惠券列表接口'''
pcodeList_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"userId":1181,"useType":0,"page":{"size":10,"num":1}}'
}

'''获取用户有效的优惠券列表接口'''
listGoodsPromotion_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"uid":1181,'
           '"goodsInfos":[{"brandId":"3",'
           '"catId":"25","storeId":"19",'
           '"supplierId":"128",'
           '"goodsId":"777",'
           '"skuId":"10750",'
           '"skuNum":1,'
           '"skuPrice":40,'
           '"isDistribution":0,'
           '"promotionId":0,'
           '"promotionType":0'
           '}]}'
}

redemption_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":805,'
           '"sendNum":1,"mark":"\u6d4b\u8bd5\u6570\u636e",'
           '"type":1,"adminId":1,'
           '"generateWay":1,'
           '"code":""}'
}
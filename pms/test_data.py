# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import time
import datetime
import sys
sys.path.append('D:\\xux_Interface\\common')
import common.common_Order
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


order=common.common_Order.order()
update_code=order.DJT_code(dingjintuanTitle)
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
        '"products":[{"endPrice":"0.1","fixPrice":"0.1","goodsId":"777","groupPrice":"0.2","ladder":[{"personNumber":"1","price":"0.2"},{"personNumber":"2","price":"0.2"}],"productId":0},{"endPrice":0.1,"fixPrice":0.1,"goodsId":"777","groupPrice":0.2,"ladder":[{"personNumber":"1","price":0.2},{"personNumber":"2","price":0.2}],"productId":"10750"}],"supportPromotion":0,"operator":1,"supportSpecial":1,"detail":"","sortOrder":0,"id":"' + str(update_code) + '"}'
}




'''修改优惠劵状态'''

results=order.batchSend(status=2)
promotionCodes=order.Pms_code(results)
Pms_updateStatus={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionCode":"'+str(promotionCodes)+'","status":2,"orderId":"24594"}'


}


'''检查活动名称是否重复接口'''
NameRepeat_data={

    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionName":"2017-01-19 18:25:49Test_DJTuan"}'

}


'''批量发放优惠卷接口'''
batchSend_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495,"num":1,"mark":"","type":0,"userIds":[1181],"adminId":1}'
}

'''发放优惠卷接口'''
Pmssend_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"promotionId":495,"num":10,"mark":"","type":1,"userId":1181,"adminId":1}'
}

'''创建砍价团'''
createPromotion_data={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{"conditions":[{"benefitType":3,"benefitValue":1,"conditionType":3,"conditionValue":1},{"benefitType":3,"benefitValue":2,"conditionType":3,"conditionValue":2}],"detail":"1、活动有效期为：xxx至xxx，逾期无效；<br>2、砍价获得的优惠仅适用于当前商品，且仅能以优惠价购买1份商品，优惠金额将在提交订单时直接减去；<br>3、砍价优惠不可与其他优惠如优惠券同时使用；<br>4、砍价团商品付款成功后，您将在24小时内收到短信通知确认是否购买成功，请耐心等待，订单一经确认，不可取消变更；<br>5、砍价商品可进行砍价的同时，也支持正常购买行为（特惠价购买）；<br>6、如需查看订单可点击本公众号菜单栏中的“我的订单”；<br>7、活动商品数量有限，先到先得，售完即止；<br>8、有任何疑问，请咨询妈网旅游部客服：400-629-7599（节假日、周末休息）；<br>9、本活动最终解释权归妈网亲子游所有。","dimensions":[{"detail":"9.00","dimensionType":5,"parentScope":0,"scope":3024}],"endAt":1488279600,"linkUrl":"http://www.woniutrip.com","operator":12,"reason":"<p>来来来</p>","startAt":1487847600,"status":1,"title":"接口测试商品(勿动)","type":7,"virtualHit":20}'

}
createPromotion_data1={
     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
     'timestamp':times,
       'data':'{'
              '"conditions": ['
     '{'
              '"benefitType": 3,'
              '"benefitValue": 1,'
              '"conditionType": 3,'
              '"conditionValue": 1'
    '},'
     '{'
              '"benefitType": 3,'
              '"benefitValue": 3,'
              '"conditionType": 3,'
              '"conditionValue": 2'
    '}'
'],'
              '"detail": "1、活动有效期为：xxx至xxx，逾期无效；<br>2、砍价获得的优惠仅适用于当前商品，且仅能以优惠价购买1份商品，优惠金额将在提交订单时直接减去；<br>3、砍价优惠不可与其他优惠如优惠券同时使用；<br>4、砍价团商品付款成功后，您将在24小时内收到短信通知确认是否购买成功，请耐心等待，订单一经确认，不可取消变更；<br>5、砍价商品可进行砍价的同时，也支持正常购买行为（特惠价购买）；<br>6、如需查看订单可点击本公众号菜单栏中的“我的订单”；<br>7、活动商品数量有限，先到先得，售完即止；<br>8、有任何疑问，请咨询妈网旅游部客服：400-629-7599（节假日、周末休息）；<br>9、本活动最终解释权归妈网亲子游所有。",'
              '"dimensions": ['
     '{'
              '"detail": "10.00",'
              '"dimensionType": 5,'
              '"parentScope": 0,'
              '"scope": 2680'
              '}'
    '],'
              '"endAt": 1487844000,'
              '"linkUrl": "http://www.baidu.com",'
              '"operator": 1,'
              '"reason": "<p>★供奉唯一的释迦牟尼佛真身指骨舍利，引来大批海内外人士前来参拜、瞻仰； \n<br/> ★传承着释迦佛法，演绎慈悲佛陀的智慧妙法。净化繁劳迷惑尘心之旅； \n<br/> ★“佛光阁”佛文化体验宾馆房间装饰典雅、别致，设备齐全，设计独特，禅修间中设有专门为参禅者打坐的禅台。讲经堂、禅茶室、素食餐厅、书吧等具有佛文化特色的设施一应俱全； \n<br/> ★景区内万众瞩目的合十舍利塔塔高148米，庄严肃穆、气势恢宏，它供奉着世界唯一的释迦牟尼真身指骨舍利，它象征着和谐安康、国泰民安的旷古盛世。</p>",'
              '"startAt": 1487584800,'
              '"status": 1,'
              '"title": "法门寺文化景区",'
              '"type": 7,'
              '"virtualHit": 380'
              '}'
}






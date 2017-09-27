# -*- coding: utf-8 -*-
__author__ = 'leo'
import time
import random
times= int(time.time())


def register_data():
    nu=random.randint(20000, 30000)
    userName='Test_DP01_'+str(nu)
    register_data={
        'api_key':'091e63850fce13f7bee3774c92e0c9e5',
        'timestamp':times,
        'data':'{'
               '"catId":17,'
               '"groupId":9,'
               '"userName":"'+userName+'",'
               '"signatoryId":2,'
               '"merchantsOfficial":"test",'
               '"confirmStatus":1,"confirmReason":"","payMethodId":2,"depositStatus":3,"deposit":"0",'
               '"billingCycle":"","bank":"u62dbu5546u94f6u884c","bankAccount":"6222023602080752132",'
               '"bankUserName":"Test","returnContacts":"Tesst","returnMobile":"13800138000","callNo":"",'
               '"returnAddress":"Test_Adress","province":19,"city":307,"district":3146,"zipCode":"","contacts":"Test",'
               '"mobile":"13800138000","email":"","address":"","businesScope":"",'
               '"remark":"","ip":"192.168.14.37","operatorId":1,"taxpayerNo":"",'
               '"swiftCode":"","moneyTypeId":142,"alias":"","deliverTimeLimit":0,"delaySettle":0,'
               '"userType":0,"commissionList":[{"rate":"9","goodsCatId":"0","brandId":"0","catLevel":0}],'
               '"billingDays":"1"}'
    }
    return register_data

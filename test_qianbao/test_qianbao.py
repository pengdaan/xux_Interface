# -*- coding: utf-8 -*-
__author__ = 'leo'

import requests,json
def test_unbindPhone():
        '''钱包用户解绑手机号，本质是：大UC用户解绑手机号'''
        url='http://wallet.mama.cn/User/unbindPhone'
        test_unbindPhone={
            'API-KEY':'xux',
            #'uid':'44695795',
            'uid':'43507844',                            '''这个是么么22账号'''
            'phone':'13728142737',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)


def test_clearTradePwd():
        '''清除交易密码设置,相当于密码初始化（密码为空，未设置密码）'''
        url='http://wallet.mama.cn/user-test/clearTradePwd'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'43507844',
            'key':'ceshi001_clear',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)

def test_clearTradeErrorLock():
        '''当天错误交易码超过3次，锁定；此接口用于解锁！'''
        url='http://wallet.mama.cn/user-test/clearTradeErrorLock'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
         #   'uid':43507844,                            '''这个是么么22账号'''
            'key':'ceshi002_clear',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)

def test_setTradePwd():
        '''设置交易密码【测试专用】'''
        url='http://wallet.mama.cn/user-test/setTradePwd'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
            'trade_pwd':123456,
            'key':'ceshi001_test',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)


def test_bindPhone():
        '''钱包用户绑定手机号，本质是：大UC用户手机号绑定'''
        url='http://wallet.mama.cn/User/bindPhone'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
            'phone':13728142737,
            'sms_code':'9836',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)


def test_getSmsCode():
        '''获取手机验证码'''
        url='http://wallet.mama.cn/User/getSmsCode'
        test_unbindPhone={
            'API-KEY':'xux',
          #  'uid':'44695795',                         '''这个是微信的账号'''
            'uid':43507844,                            '''这个是么么22账号'''
            'phone':13728142737,
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)


def test_getDetail():
        '''获取用户钱包信息'''
        url='http://wallet.mama.cn/User/getDetail'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'43507844',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)

def test_setNeedTradePwd():
        '''设置交易需要支付密码（不免密，取消免密）'''
        url='http://wallet.mama.cn/User/setNeedTradePwd'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)

def test_verifyTradePwd():
        '''验证交易密码'''
        url='http://wallet.mama.cn/User/verifyTradePwd'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
            'trade_pwd':'123456',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)

def test_verifySmsCode():
        '''验证交易密码'''
        url='http://wallet.mama.cn/User/verifySmsCode'
        test_unbindPhone={
            'API-KEY':'xux',
            'uid':'44695795',
            'phone':'13728142737',
            'sms_code':'2899',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)


def test_getuserbalance():
        '''验证交易密码'''
        url='http://wallet.mama.cn/Fundsdetail/getuserbalance'
        test_unbindPhone={
            'from':'mmq',
            'API-KEY':'mmq_ios',
            'uid':'44695795',
            'debug':'6667b2371ce2d715c22077688dc4e411'
        }
        r=requests.get(url, params=test_unbindPhone)
        result=r.text
        try:
            js = json.loads(result)
            print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
            return js
        except:
            print (result)





'''钱包用户解绑手机号，本质是：大UC用户解绑手机号'''
#test_unbindPhone()

'''清除交易密码设置,相当于密码初始化（密码为空，未设置密码）'''
#test_clearTradePwd()

'''当天错误交易码超过3次，锁定；此接口用于解锁！'''
#test_clearTradeErrorLock()

'''设置交易密码【测试专用】'''
#test_setTradePwd()

'''钱包用户绑定手机号，本质是：大UC用户手机号绑定'''
#test_bindPhone()

'''获取手机验证码'''
#test_getSmsCode()

'''获取用户钱包信息'''
#test_getDetail()

'''设置交易需要支付密码（不免密，取消免密）'''
#test_setNeedTradePwd()

'''验证交易密码'''
#test_verifyTradePwd()

'''验证交易密码'''
#test_verifySmsCode()

'''验证交易密码'''
#test_getuserbalance()
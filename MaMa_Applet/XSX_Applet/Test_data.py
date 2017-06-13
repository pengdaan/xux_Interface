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
            'uid':43507844,
            }
    else:
        Uid={
            'uid':''+uid+'',
            }
    return Uid

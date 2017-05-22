# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import json
def result_json(result):
    try:
        js = json.loads(result)                                           #将json解析成python的数据类型
        print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10)) #转化为json，以特定的格式输出，且处理中文显示问题
        return js
    except:
        print (result)

def DP_order(result):
    try:
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        # print  type(json_to_python)
        order = json_to_python['data']
        #print type(dp_order)
        dp_order=order['order_sn']
        return dp_order
    except:
        print (result)

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
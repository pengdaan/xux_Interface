# -*- coding: utf-8 -*-
__author__ = 'leo'
#加载yaml
import yaml

#读取文件
f = open('D:/xux_project/XSX_InTerFace/Dp/test.yaml','r')
#f = open('F:/SmallBear_Interface/test_Data/DP/OrderDPSuces.yaml')
#导入
dict =  yaml.load(f)
print dict
#yaml.safe_dump(data)
# for data in yaml.load_all(f):
#     print data

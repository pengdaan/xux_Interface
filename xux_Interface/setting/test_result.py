# -*- coding: utf-8 -*-
__author__ = 'leo'
def test_result(data):

    if 'msg'in data:
        return data['code']

    else:
        return 'msg is not found'




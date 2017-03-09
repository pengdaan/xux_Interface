# -*- coding: utf-8 -*-
import requests,json,time
import setting.api_signs
import setting.result_jsons
import setting.DBConns
import all_secrets
import common_data
times= int(time.time())

class order:

    def xux_order(self,result):
        try:
            # 将json对象转换成python对象
            json_to_python = json.loads(result)
            # print  type(json_to_python)
            data_1 = json_to_python['data']
            data_2=data_1['2']
            XUXorder=data_2['order_sn']
            return XUXorder
        except:
            print (result)


    def order_id(self,result):
        try:
            # 将json对象转换成python对象
            json_to_python = json.loads(result)
            # print  type(json_to_python)
            order = json_to_python['data']
            #print type(dp_order)
            dp_order=order['order_id']
            # print result
            return dp_order
        except:
            print (result)

    def order_sn(self,result):
        try:
            # 将json对象转换成python对象
            json_to_python = json.loads(result)
            # print  type(json_to_python)
            order = json_to_python['data']
            #print type(dp_order)
            order=order['order_sn']
            # print result
            return order
        except:
            print (result)


    def Pms_code(self,result):
        # 将json对象转换成python对象
        json_to_python = json.loads(result)
        data_1 = json_to_python['data']
        data_2=data_1['results']
        data_3=data_2[0]
        data_4=data_3['codeList']
       # print data_4
        return data_4


    def Updatexux_Order(self,XUXorder):
         #通过修改数据库更改订单状态为已审核状态，只能改普通的直邮订单
         XUXorders = "UPDATE mall_order_info SET order_status='1',order_amount='0',confirm_time='%(time)s' WHERE order_sn='%(order)s'"%{'time':times,"order":XUXorder}
         mysql = setting.DBConns.Mysql()
         mysql.get_one(XUXorders)
         mysql.commit()

    def reateOrderTour(self):
        '''旅游创建订单'''
        api_secrets=all_secrets.ly_secrets
        payload=common_data.createOrderTour_data
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        r=requests.post(common_data.createOrderTour_url, params=payload)
        results= r.text
        return results


    def createOrderXsx(self):
        '''小树熊下单接口'''
        payload= common_data.data_createOrderXsx
        r=requests.post(common_data.orderXUX_url,params=payload)
        #print payload
        result=r.text
        print order.xux_order(self,result)
        return order.xux_order(self,result)

    def orderDP(self,order_data=None):
        '''新的点评下单方法，弃用旧的方法，secrets写死的方式，不走查库的方法'''
        api_secrets=all_secrets.dp_secrets
        payload=order_data
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        #print payload
        r=requests.post(common_data.orderDP_url, params=payload)
        results= r.text
        #print results
        return order.order_sn(self,results)

    def Pmsadd(self):
        '''Pms添加优惠劵'''
        api_secrets=all_secrets.pms_secrets
        payload=common_data.test_Addpms
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        requests.post(common_data.PMSadd_url, params=payload)
        #print common_data.promotionNames
        return str(common_data.promotionNames)


    def updatePayDPStatu(self,status=None,ly_order=None,DP_order=None):
        '''更新订单支付状态'''
        api_secrets=all_secrets.update_dpStatus
        payloads=common_data.data_updatePayStatus
        #不发卷订单
        if status==1:
            order_sns=order.orderDP(self)#生成订单号
            payloads.setdefault('order_sn',order_sns) #插入订单号
            payload=payloads
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
            requests.post(common_data.updatePayStatus_url, params=payload)
            return order_sns
        #发卷订单
        elif (status==2)and(DP_order!=None):
            order_sns=DP_order
            #print order_sns,order_sns
            payloads=common_data.data_updatePayStatus
            #order_sns=order.orderDP(self,common_data.data_OrderDPSuce)#生成订单号
            payloads.setdefault('order_sn',order_sns) #插入订单号
            payload=payloads
            #print payload,'payload'
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
            #r=requests.post(common_data.updatePayStatus_url, params=payload)
            #print r.text
            #print order_sns
            requests.post(common_data.updatePayStatus_url, params=payload)
            return order_sns
        #小树熊订单
        elif status==3:
            payloads=common_data.data_updatePayStatus_xsx
            order_sns=order.createOrderXsx(self)#生成订单号
            payloads.setdefault('order_sn',order_sns) #插入订单号
            api_secrets=all_secrets.update_dpStatus#返回api_secret
            payload=payloads
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
            requests.post(common_data.updatePayStatus_url, params=payload)
            #r=requests.post(updatePayStatus_url, params=payload)
            # print r.text
            #print order_sns
            return order_sns
        #旅游订单'
        elif (status==4)and(ly_order!=None):
            order_sn=ly_order
            api_secrets=all_secrets.update_dpStatus
            payloads=common_data.data_updatePayStatus_ly
            payloads.setdefault('order_sn',order_sn) #插入订单号
            payload=payloads
            #print payload
            api_sign=setting.api_signs.api_signs(payload,api_secrets)
            payload.setdefault('api_sign',api_sign)
            r=requests.post(common_data.updatePayStatus_url, params=payload)
            results= r.text
            #print results
            return order_sn

    def batchSend(self,status=1):
        '''批量发放优惠卷接口'''
        api_secrets=all_secrets.pms_secrets
        payload=common_data.batchSend_data
        api_sign=setting.api_signs.api_signs(payload,api_secrets)
        payload.setdefault('api_sign',api_sign)
        if status==1:
            requests.post(common_data.BatchSend_url , params=payload)
        elif status==2:
            r=requests.post(common_data.BatchSend_url , params=payload)
            results=r.text
            return results




    def Pmsname_one(self,pmsName):
        #获取Pms活动的活动id
        PmsId="SELECT * FROM mall_promotion where promotion_name='%s'"%pmsName
        mysql = setting.DBConns.Mysql()
        datas=mysql.get_one(PmsId)
        if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
            pms_id=datas['id']
            Pmssend_data={
                'api_key':'647b00ec1fe6990b1b97263b05341b6b',
                'timestamp':times,
                'data':'{"promotionId":"' + str(pms_id) + '","num":10,"mark":"","type":1,"userId":1181,"adminId":1}'
            }
            # print Pmssend_data
            return Pmssend_data
        else:
            print 'pms_id 不存在'

    def Pmsname_all(self,pmsName):
        #获取Pms优惠卷的所有优惠卷id
        PmsId="SELECT * FROM mall_promotion where promotion_name='%s'"%pmsName
        mysql = setting.DBConns.Mysql()
        datas=mysql.get_one(PmsId)
        if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
            pms_id=datas['id']
            batchSend_data={
                'api_key':'647b00ec1fe6990b1b97263b05341b6b',
                'timestamp':times,
                'data':'{"promotionId":"' + str(pms_id) + '","num":1,"mark":"","type":0,"userIds":[1181],"adminId":1}'
            }
            # print Pmssend_data
            return batchSend_data
        else:
            print 'pms_id 不存在'

    def DJT_code(self,title):
        #获取定金团活动的活动id
        #DJT_ids="SELECT * FROM mall_promotion_info WHERE title='%(title)s'"%{'title':title}
        DJT_ids="SELECT * FROM mall_promotion_info ORDER BY id DESC LIMIT 1"
        mysql = setting.DBConns.Mysql()
        datas=mysql.get_one(DJT_ids)
        DJT_id=datas['id']
        return DJT_id
        # if (datas!= None):#判断该定金团是否存在，存在为1 不存在为0
        #    DJT_id=datas['id']
        #    #print DJT_id
        #    return DJT_id
        # else:
        #     DJT_ids="SELECT * FROM mall_promotion_info ORDER BY id DESC LIMIT 1"
        #     datas=mysql.get_one(DJT_ids)
        #     DJT_id=datas['id']
        #     return DJT_id





# '''修改优惠劵状态'''
# promotionCodes=Pms_code()
# Pms_updateStatus={
#     'api_key':'647b00ec1fe6990b1b97263b05341b6b',
#     'timestamp':times,
#     'data':'{"promotionCode":"'+str(promotionCodes)+'","status":2,"orderId":"24594"}'
#
#
# }


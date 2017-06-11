# -*- coding: utf-8 -*-
__author__ = 'leo'
from Tools.Order_Tools import ToolsDB

'''该脚本用于修改普通订单的审核状态，（主要针对供应商发货，以及直邮商品，其他不可以用）
   把未审核的的订单变更为已审核审核
    1、更新order_info的 status状态
    2、更新confirm_time=当前的时间
''',



def Updete_LF(DB):

        print ("请输入订单号，输入666可切换数据库：")
       # print (unicode("请输入订单号，输入666可切换数据库：",'utf-8').encode('gbk'))
        Worder=raw_input()
        b=Worder.strip()
        if Worder=='666':
            print "正在重新选择测试环境，=。=！"
          #  print (unicode("正在重新选择测试环境，=。=！",'utf-8').encode('gbk'))
            OrderDB()
        elif Worder=='':
            print "输入内容为空，请重新输入，=。=！"
           # print (unicode("输入内容为空，请重新输入，=。=！",'utf-8').encode('gbk'))
            OrderDB()
        else:
              buyer_user_ids=("SELECT buyer_user_id FROM mall_order_rebates WHERE order_sn='%s'"%b)    #执行sql，查询入会订单是否存在
              sn_datas =DB.get_one(buyer_user_ids)
              if (sn_datas!=None):#判断该订单是否存在，存在为1 不存在为0
                print('入会订单确认存在，正在获取user_id')
                sn_data= sn_datas[0] #获取入会订单的user_id
                user_ids=("SELECT * FROM mall_users WHERE user_id='%s'"%sn_data) #在良粉会员表查询一次，确认会员存在
                #print(unicode("'入会订单确认存在。",'utf-8').encode('gbk'))
                us_data=DB.ch_data(user_ids)
                if (us_data !=None):
                    delete_order_sn = ("delete from mall_order_rebates where order_sn='%s'"%b)    #删掉入会订单
                    delete_user_id =("delete  from mall_users where user_id='%s'"%sn_data)          #删掉会员表
                    print delete_order_sn
                    print delete_user_id
                    DB.delete_one(delete_user_id)
                    DB.delete_one(delete_order_sn)
                    DB.commit()
                    print '该用户良粉身份已经删除 --！'
                    Updete_LF(DB)
                else:
                    print '删除良粉会员失败，请联系管理员！'
              else:
                print u"该订单不存在，请重新输入，或检查连接库是否正确。"
               # print(unicode("该订单不存在，请重新输入，或检查连接库是否正确。",'utf-8').encode('gbk'))
                Updete_LF(DB)



def OrderDB():
  try:
        #print (unicode("请输入测试环境数据库（120,121,122,100）：",'utf-8').encode('gbk'))
        #Worders=raw_input()
        Worders=raw_input("请输入测试环境数据库（122,168,100）：")
        Worder=Worders.strip()#自动去空
        if Worder=='120':

            conn = ToolsDB.OrderDBconn(host="192.168.88.120",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            DB=conn


        if Worder=='121':
            conn = ToolsDB.OrderDBconn(host="192.168.88.121",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            DB=conn


        if Worder=='122':
            conn = ToolsDB.OrderDBconn(host="192.168.88.122",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            DB=conn


        if Worder=='100':
            conn = ToolsDB.OrderDBconn('10.0.0.100','3306','testxiaoshuxiong', '9bo0388lAxA4XsCY','mama_mall')
            DB=conn

        Updete_LF(DB)

  except:
    print "输入数据库错误。"
    #print (unicode("输入数据库错误。",'utf-8').encode('gbk'))
    OrderDB()

if __name__ == '__main__':
      OrderDB()



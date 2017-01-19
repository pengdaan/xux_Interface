#-*- coding: utf-8 -*-
__author__ = 'leo'
import MySQLdb
class OrderDBconn(object):

    def __init__(self,host,port,user,passwd,db):
        self.conn = MySQLdb.connect(
            host=host,
            port=int(port),
            user=user,
            passwd=passwd,
            db=db,
            charset="utf8")
        print self.conn

    def cursor(self):#  #获取操作游标
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            return self.conn.cursor()

    def get_all(self, sql_command, cmd_param=None):

        cursor=self.cursor()
        if cmd_param:
            count =cursor.execute(sql_command, cmd_param)
        else:
            count = cursor.execute(sql_command)
        if count:
            sql_result = cursor.fetchall()
        else:
            sql_result = None
        return sql_result

    def get_one(self, sql_command, cmd_param=None):
        cursor=self.cursor()

        if cmd_param:
            count = cursor.execute(sql_command, cmd_param)
        else:
            count = cursor.execute(sql_command)
        if count:
           # print count
            #@sql_result = cursor.fetchoneDict()
            sql_result=cursor.fetchone()
        else:
            sql_result = None
        return sql_result


    def ch_data(self, sql_command, cmd_param=None):
        cursor=self.cursor()

        if cmd_param:
             count = cursor.execute(sql_command, cmd_param)

        else:
             count = cursor.execute(sql_command)

        if count:
            sql_result_count = cursor.fetchone()
            sql_result=sql_result_count[0]

        else:
            sql_result = None

        return sql_result


    def delete_one(self, sql_command, cmd_param=None):
        cursor=self.cursor()

        if cmd_param:
            cursor.execute(sql_command, cmd_param)
        else:
            cursor.execute(sql_command)

       # return count
        #sql_result='删除成功 ==！'
       # return sql_result

    def commit(self): #删除操作必须要提交事务
          try:
            return self.conn.commit()
          except(AttributeError, MySQLdb.OperationalError):
            return self.conn.commit()



    def close(self):#关闭链接
        return self.conn.close()

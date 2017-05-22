# -*- coding: utf-8 -*-
# 数据库配置文件
import Config
import MySQLdb
import time
import pprint
from DBUtils.PooledDB import PooledDB
# 为返回字典格式推荐将连接池的cursorclass设置为它
from MySQLdb.cursors import DictCursor

class PayMysql(object):
    """
    Attributes:
       None
    """
    __mysql_pool = None
    def __init__(self):
        # 获取连接对象
        self._mysql_conn = PayMysql.__get_connection()
        # 创建游标对象
        self._mysql_cursor = self._mysql_conn.cursor()
    @staticmethod
    def __get_connection():
        """Get mysql connection from connection pool.
        Args:
            None
        Returns:
            connection
        """
        # 根据配置文件创建连接池
        if not PayMysql.__mysql_pool:
            PayMysql.__Mysql_pool = PooledDB(
                creator=MySQLdb,
                use_unicode=False,
                cursorclass=DictCursor,
                db=Config.MysqlConfigPay['db'],
                host=Config.MysqlConfigPay ['host'],
                port=Config.MysqlConfigPay ['port'],
                user=Config.MysqlConfigPay ['user'],
                passwd=Config.MysqlConfigPay ['passwd'],
                charset=Config.MysqlConfigPay ['charset'],
                mincached=Config.MysqlConfigPay ['mincached'],
                maxcached=Config.MysqlConfigPay ['maxcached'],
                maxconnections=Config.MysqlConfigPay ['maxconnections'])
        # 返回连接池中连接对象
        return PayMysql.__Mysql_pool.connection()

    def get_all(self, sql_command, cmd_param=None):
        """"Get all sql command execute result.
        Args:
            sql_command: sql command
            cmd_param  : sql command paramaters
        Returns:
            tuple
        """
        if cmd_param:
            count = self._mysql_cursor.execute(sql_command, cmd_param)
        else:
            count = self._mysql_cursor.execute(sql_command)
        if count:
            sql_result = self._mysql_cursor.fetchall()
        else:
            sql_result = None
        return sql_result

    def get_one(self, sql_command, cmd_param=None):
        """"Get one sql command execute result.
        Args:
            sql_command: sql command
            cmd_param  : sql command paramaters
        Returns:
            dict
        """
        if cmd_param:
            count = self._mysql_cursor.execute(sql_command, cmd_param)
        else:
            count = self._mysql_cursor.execute(sql_command)
        if count:
            sql_result = self._mysql_cursor.fetchoneDict()
        else:
            sql_result = None
        return sql_result

def paysecret(own_mch_id): #这里只需要查询Api_secret是否存在，存在的话就return到验签里面去就好了

    own_mch_ids = "SELECT * FROM pay_merchant WHERE own_mch_id='%s'"%own_mch_id
    merchant_key = "SELECT merchant_key FROM pay_merchant WHERE own_mch_id='%s'"%own_mch_id
    mysql = PayMysql()
    datas=mysql.get_all(own_mch_ids )


    if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
        data=mysql.get_one(merchant_key)
      #  print data['merchant_key']
        return data['merchant_key']
    else:
        print '商户号不存在。'


def Payapi_secret(**test_data):
    if isinstance(test_data,dict):
        own_mch_id=test_data.get('own_mch_id')
        return own_mch_id
    else:
        return None


















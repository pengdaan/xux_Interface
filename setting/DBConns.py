# -*- coding: utf-8 -*-
# 数据库配置文件
import Config
import MySQLdb
import pymysql
from DBUtils.PooledDB import PooledDB
# 为返回字典格式推荐将连接池的cursorclass设置
from MySQLdb.cursors import DictCursor

class Mysql(object):
    """
    Attributes:
       None
    """
    __mysql_pool = None
    def __init__(self):
        # 获取连接对象
        self._mysql_conn = Mysql.__get_connection()
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
        if not Mysql.__mysql_pool:
            Mysql.__mysql_pool = PooledDB(
                creator=MySQLdb,
                use_unicode=False,
                cursorclass=DictCursor,
                db=Config.MysqlConfig['db'],
                host=Config.MysqlConfig['host'],
                port=Config.MysqlConfig['port'],
                user=Config.MysqlConfig['user'],
                passwd=Config.MysqlConfig['passwd'],
                charset=Config.MysqlConfig['charset'],
                mincached=Config.MysqlConfig['mincached'],
                maxcached=Config.MysqlConfig['maxcached'],
                maxconnections=Config.MysqlConfig['maxconnections'])
        # 返回连接池中连接对象
        return Mysql.__mysql_pool.connection()
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


def secret(api_key): #这里只需要查询Api_secret是否存在，存在的话就return到验签里面去就好了

    Api_key = "SELECT * FROM mall_app WHERE api_key='%s'"%api_key
    api_secret = "SELECT api_secret FROM mall_app WHERE api_key='%s'"%api_key
    mysql = Mysql()
    datas=mysql.get_all(Api_key )

    if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
        data=mysql.get_one(api_secret)
      #  print data['api_secret']
        return data['api_secret']
    else:
        print 'api_key不存在'


def pmssecret(api_key): #这里只需要查询Api_secret是否存在，存在的话就return到验签里面去就好了

    Api_key = "SELECT * FROM mall_promotion_sign WHERE api_key='%s'"%api_key
    api_secret = "SELECT api_secret FROM mall_promotion_sign WHERE api_key='%s'"%api_key
    mysql = Mysql()
    datas=mysql.get_all(Api_key )

    if (datas!= None):#判断该订单是否存在，存在为1 不存在为0
        data=mysql.get_one(api_secret)
       # print data['api_secret']
        return data['api_secret']
    else:
        print 'api_key不存在'




def Api_secret(**test_data):#这里要做的事情应该是处理data里面的数据，把api_key抽离出来，返回api_key ( **test_data表示关键字参数,它是一个dict)
    if isinstance(test_data,dict):
       # test_data.has_key('api_key')#python2的写法
       # test_data.in()
        api_key=test_data.get('api_key')
        return api_key
    else:
        return None
































'''
旧的pay_own_mch_id验证代码，已废弃
'''
# def Payapi_secret(**test_data):
#     if isinstance(test_data,dict):
#         own_mch_id=test_data.get('own_mch_id')
#         return own_mch_id
#     else:
#         return None



'''
旧的pmssecret获取代码，已废弃
'''

# def pmssecret(api_key): #这里只需要查询Api_secret是否存在，存在的话就return到验签里面去就好了
#     conn= pymysql.connect( #新回归环境
#         host='10.0.0.100',
#         port = 3306,
#         user='testxiaoshuxiong',
#         passwd='9bo0388lAxA4XsCY',
#         db ='mama_mall',
#         )
#     cur = conn.cursor()# 通过获取到的数据库连接conn下的cursor()方法来创建游标
#     Api_key = "SELECT * FROM mall_promotion_sign WHERE api_key='%s'"%api_key
#     api_secret = "SELECT api_secret FROM mall_promotion_sign WHERE api_key='%s'"%api_key
#    # print (api_secret)
#     datas=cur.execute(Api_key)
#     if (datas==1):#判断该订单是否存在，存在为1 不存在为0
#         cur.execute(api_secret)# 使用execute方法执行SQL语句
#         data = cur.fetchone()# 使用 fetchone() 方法获取一条数据库。
#     #    print data[0]
#         return data[0]
#     else:
#         print datas
#         return datas
#
#     cur.close()
#     conn.commit()
#     conn.close()


'''
旧的pay_own_mch_id获取代码，已废弃
'''


# def paysecret(own_mch_id): #这里只需要查询Api_secret是否存在，存在的话就return到验签里面去就好了
#     conn= pymysql.connect( #新回归环境
#         host='10.0.0.100',
#         port = 3306,
#         user='testxiaoshuxiong',
#         passwd='9bo0388lAxA4XsCY',
#         db ='mama_pay',
#         )
#     cur = conn.cursor()# 通过获取到的数据库连接conn下的cursor()方法来创建游标
#     own_mch_ids = "SELECT * FROM pay_merchant WHERE own_mch_id='%s'"%own_mch_id
#     merchant_key = "SELECT merchant_key FROM pay_merchant WHERE own_mch_id='%s'"%own_mch_id
#     datas=cur.execute(own_mch_ids)
#     if (datas==1):#判断该订单是否存在，存在为1 不存在为0
#         cur.execute(merchant_key)# 使用execute方法执行SQL语句
#         data = cur.fetchone()# 使用 fetchone() 方法获取一条数据库。
#         print data[0]
#
#         return data[0]
#     else:
#         print '商户号不存在。'
#         return datas
#
#     cur.close()
#     conn.commit()
#     conn.close()




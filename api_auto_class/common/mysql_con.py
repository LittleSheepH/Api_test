# -*-coding:utf-8-*-
# @Time       :2018/12/22 23:14
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :mysql_con.py
# @Software   :PyCharm
import pymysql
from api_auto_class.common.config import Configloader
class MysqlUtil:
    def __init__(self):
        config = Configloader()
        host = config.get('mysql','host')
        port = config.getint('mysql','port')
        user = config.get('mysql','user')
        pwd = config.get('mysql','password')
        self.mysql = pymysql.connect(host=host,port=port,user=user,password=pwd,cursorclass=pymysql.cursors.DictCursor)

    #点查询的过程封装成一个方法，查询一条数据并返回
    def fetch_one(self,sql):
        cursor=self.mysql.cursor()#使用数据库的实例声明一个游标，返回一个cursor的实例
        cursor.execute(sql)#开始执行，根据什么执行呢？根据sql语句执行查询
        # cursor.fetchall()#返回所有查询结果
        # cursor.fetchmany(size)#size制定返回多少条
        return cursor.fetchone()#返回一条
    def fetch_all(self,sql):
        cursor = self.mysql.cursor()  # 使用数据库的实例声明一个游标，返回一个cursor的实例
        cursor.execute(sql) # 开始执行，根据什么执行呢？根据sql语句执行查询
        return cursor.fetchall()
    def close(self):
        return self.mysql.close()


if __name__ == '__main__':
    sql = "select mobilephone from future.member where mobilephone != ''order by mobilephone desc limit 1 "
    sql1 = "select LeaveAmount from future.member where MobilePhone='13417543096'"
    print(sql1)
    mysql = MysqlUtil()
    print('-----------')
    result1= mysql.fetch_one(sql)
    print(result1)
    result =mysql.fetch_all(sql1)#result是一个元祖,根据索引取
    # max_mobile = int(result[0])+1
    print(type(*result),result)
    print(len(result))
    # print(max_mobile)
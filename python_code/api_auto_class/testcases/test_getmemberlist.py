# -*-coding:utf-8-*-
# @Time       :2018/12/31 22:49
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_getmemberlist.py
# @Software   :PyCharm

from api_auto_class.common.doexcel import readcase
from api_auto_class.common import concants
from api_auto_class.common.request import Request
import unittest
from ddt import ddt, data
import json
from api_auto_class.common.base_data import Context
from api_auto_class.common.base_data import DoRegex
from api_auto_class.common.mysql_con import MysqlUtil

read = readcase(concants.data)
test_data = read.get_case('8getmemberlist')


@ddt
class TestGetmemberList(unittest.TestCase):
    def setUp(self):
        self.mysql = MysqlUtil()
        sql= 'SELECT * FROM future.member'
        self.database_actural=self.mysql.fetch_all(sql)
        print(len(self.database_actural))



    @data(*test_data)
    def test_getmemberlist(self, item):
        print("******test_getmemberList***")
        if item.data != None:
            data = DoRegex.replace(item.data)
            if data != None:
                print("****data is not none**********{}".format(data))
            else:
                print("****data is none**********")
            actural_data = json.loads(data)
            if hasattr(Context, 'cookies'):
                print("**************")
                cookies = getattr(Context, 'cookies')
            else:
                print("******NONE********")
                cookies = None
            res = Request(item.method, item.url, data=actural_data, cookies=cookies)
            print(res.get_json())
            if res.get_cookie():
                print("******res.get_cookie()********{}".format(res.get_cookie()))
                # cookies =setattr(Context,'cookies',res.get_cookie())
                cookies = res.get_cookie()
                setattr(Context, 'cookies', res.get_cookie())
        else:

            cookie = getattr(Context, 'cookies')
            print("******cookie**{}".format(cookie))
            print("******method**{}".format(item.method))
            print("******url**{}".format(item.url))
            print("***********",item.case_id)
            res = Request(item.method, item.url, cookies=cookie)
            print(len(res.get_json()['data']))
            try:
                self.assertEqual(len(self.database_actural),len(res.get_json()['data']))
                # self.assertListEqual(self.database_actural,res.get_json()['data'])
                result='PASS'
            except AssertionError as e:
                result='FILED'
                raise e
            finally:
                print('---------------------------------------------------------------------------------------')
                print("*******len ",len(res.get_json()['data']))
                print(result)
                read.write_actural_by_case_id('8getmemberlist',case_id=item.case_id,actural=len(res.get_json()['data']),result=result)



    def tearDown(self):
        self.mysql.close()
        print('关闭数据库连接！')


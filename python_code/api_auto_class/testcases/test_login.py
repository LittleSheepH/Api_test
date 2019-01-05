# -*-coding:utf-8-*-
# @Time       :2018/12/25 20:35
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_recharge.py
# @Software   :PyCharm

from api_auto_class.common.request import Request
from api_auto_class.common.doexcel import readcase
from api_auto_class.common import concants
from ddt import ddt,data
import unittest
import json
read=readcase(concants.data)
test_data = read.get_case('2login')
@ddt
class TestLogin(unittest.TestCase):

    @data(*test_data)
    def test_login(self,item):
        print(item.url)
        print(type(item.data),item.data)
        data= json.loads(item.data)
        res=Request(item.method,item.url,data)
        print(res.get_json())
        try:
            self.assertEquals(str(item.excepted),res.get_json()['code'])
            result='PASS'
        except AssertionError as e:
            result='FAIL'
            raise e
        finally:
            read.write_actural_by_case_id('2login', item.case_id, actural=res.get_text(), result=result)



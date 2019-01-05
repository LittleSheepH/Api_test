# -*-coding:utf-8-*-
# @Time       :2018/12/22 17:35
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_register.py
# @Software   :PyCharm
import unittest
#unittest
#case.py 测试用例
#suite.py 测试套件addtest addtests
#loader.py加载测试用例
#run.py  执行测试用例
#result.pu 测试结果
#main在单元测试测试test
#mock模拟测试
from api_auto_class.common.doexcel import *
from api_auto_class.common import concants
from api_auto_class.common.request import Request
import json
from ddt import data,ddt
import re
from api_auto_class.common.mysql_con import MysqlUtil
from api_auto_class.common.config import Configloader
readexcel = readcase(concants.data)
test_data = readexcel.get_case('register')
sql = "select mobilephone from future.member where mobilephone != ''order by mobilephone desc limit 1 "
conf = Configloader()
patten=conf.get('Patten','patten')
@ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        print('测试准备')
        connect = MysqlUtil()
        mobile = connect.fetch_one(sql)
        self.max_mobile = int(mobile['mobilephone']) + 1
    @data(*test_data)
    def test_register(self,date):
        #测试数据读出来
        s=date.data
        resp =str(self.max_mobile)
        res = re.sub(patten,resp,s)
        # res = re.findall(patten,s)
        # if res:
        #     end =s.replace(res[0],str(self.max_mobile))
        # else:
        #     end=s
        resp = Request(date.method,date.url,data=eval(res))
        self.assertEqual(json.loads(date.excepted),resp.get_json())
        if date.excepted == resp.get_text():
            print("resule:PASS")
            readexcel.write_actural_by_case_id('register', date.case_id, resp.get_text(), 'PASS')
        else:
            print("result:FAIL")
            readexcel.write_actural_by_case_id('register', date.case_id, resp.get_text(), 'FAIL')

    def tearDown(self):
        print("测试清除")

# -*-coding:utf-8-*-
# @Time       :2018/12/25 20:35
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_recharge.py
# @Software   :PyCharm
from api_auto_class.common.doexcel import *
from api_auto_class.common import concants
from api_auto_class.common.request import Request
import json
from ddt import data,ddt
import re
import unittest
from api_auto_class.common.mysql_con import MysqlUtil
from api_auto_class.common.config import Configloader
from api_auto_class.common.base_data import *
#读取测试数据
readexcel = readcase(concants.data)
test_data = readexcel.get_case('recharge')
#读取配置文件
conf = Configloader()
patten=conf.get('Patten','patten')

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global connect
        connect = MysqlUtil()
        print('测试准备，连接数据库')
    @data(*test_data)
    def test_recharge(self,item):
        data=DoRegex.replace(item.data)#查找excel中数据并且替换
        s=json.loads(data)#s是字典类型的一组data数据
        if hasattr(Context,'cookies'):
            cookies=getattr(Context,'cookies')
        else:
            cookies=None
        print('--------------开始执行第{}条用例---------------'.format(item.case_id))
        resp = Request(item.method,item.url,data=s,cookies=cookies)
        # print(type(resp.get_json()),'--------------------------')
        # 判断有没有cookies
        if resp.get_cookie():  # 如果有就写到Context里面啊
            setattr(Context, 'cookies', resp.get_cookie())
        #数据库校验
        if resp.get_json()['msg']=='充值成功':
            self.sql = "select LeaveAmount from future.member where MobilePhone={}".format(getattr(Context, 'normal_user'))
            after_amount = connect.fetch_one(self.sql)['LeaveAmount']#充值成功，检验有没有加到数据库
            print(resp.get_json(),'******************************************************************')
            try:
                self.assertEqual(str(after_amount),resp.get_json()['data']['leaveamount'])
                database="数据写入成功"+resp.get_json()['data']['leaveamount']
                print("数据写入成功")
            except AssertionError as e:
                database = '数据写入失败'+resp.get_json()['data']['leaveamount']
                print('数据写入失败')
                raise e
        try:
            self.assertEqual(str(item.excepted),str(resp.get_json()['code']))
            print('测试通过！')
            result='PASS'
        except AssertionError as e:
            print('测试失败！')
            result="FAIL"
            raise e
        finally:
            readexcel.write_actural_by_case_id('recharge', item.case_id,actural= resp.get_text(),result= result)
    @classmethod
    def tearDownClass(cls):
        connect.close()
        print("关闭数据库连接")

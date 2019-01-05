# -*-coding:utf-8-*-
# @Time       :2018/12/31 19:33
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_invest.py
# @Software   :PyCharm
from api_auto_class.common.request import Request
from api_auto_class.common.doexcel import readcase
from api_auto_class.common import concants
from ddt import ddt,data
from api_auto_class.common.base_data import *
from api_auto_class.common.mysql_con import MysqlUtil
import unittest
import json
read=readcase(concants.data)
test_data = read.get_case('4invest')

@ddt
class TestInvest(unittest.TestCase):
    def setUp(self):
        self.mysql=MysqlUtil()
        #投资前的账户余额
        self.sql='select * from future.member where mobilephone = {}'.format(Context.normal_user)
        self.pre_amount = self.mysql.fetch_one(self.sql)['LeaveAmount']
        print("投资前的账户余额：",self.pre_amount)
    @data(*test_data)
    def test_invest(self,item):
        data=DoRegex.replace(item.data)
        actural_data = json.loads(data)
        print("---------------------------开始执行第{}条用例".format(item.case_id))
        print("发送的data数据----------------------",actural_data)
        if hasattr(Context,'cookies'):
            # cookies = getattr(Context,'cookies')
            cookies = Context.cookies
        else:
            cookies = None

        res = Request(item.method, item.url, actural_data, cookies=cookies)
        #判断返回是否有cookies
        if res.get_cookie():
            setattr(Context,'cookies',res.get_cookie())
        print("得到的返回数据----------------------",res.get_json())
        #判断code是否一致
        self.assertEqual(item.excepted,int(res.get_json()['code']))
        print("code校验成功******************************")
        if res.get_json()['msg']=='加标成功':
            sql="select * from future.loan where memberId ={} order by createtime desc limit 1".format(Context.loan_member_id)
            all=self.mysql.fetch_one(sql)
            print(type(all['Id']),type(all))
            if all is not None:
                setattr(Context,'loan_id',str(all['Id']))# 放一个str类型的进去，以备后面正则替换，正则替换必须是字符串
                #需要加断言判断是否添加成功，判断amount和titile字段
                #审核数据校验，status=4
                print(Context.loan_id)
        if res.get_json()['msg']=='竞标成功':
            after_amount = self.mysql.fetch_one(self.sql)['LeaveAmount']
            print('本次投资的金额', actural_data['amount'])
            print("投资成功后的账户余额",after_amount)
            self.assertEqual(float(self.pre_amount),float(after_amount)+float(actural_data['amount']))
if __name__ == '__main__':
    unittest.main()
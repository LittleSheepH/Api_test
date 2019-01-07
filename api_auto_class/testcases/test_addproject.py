# -*-coding:utf-8-*-
# @Time       :2018/12/31 19:57
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :test_addproject.py
# @Software   :PyCharm

from api_auto_class.common.doexcel import readcase
from api_auto_class.common import concants
from api_auto_class.common.request import Request
import unittest
from ddt import ddt,data
import json
from api_auto_class.common.base_data import Context
from api_auto_class.common.base_data import DoRegex
read = readcase(concants.data)
test_data= read.get_case('5addproject')

@ddt
class TestAddproject(unittest.TestCase):
    @data(*test_data)
    def test_addproject(self,item):
        print(item.url)
        data=DoRegex.replace(item.data)
        actural_data = json.loads(data)
        print(type(data),'发送的数据------',data)
        if hasattr(Context,'cookies'):
            cookies = getattr(Context,'cookies')
            print('打印cookies值------',cookies)
        else:
            cookies= None
        res =Request(item.method,item.url,actural_data,cookies=cookies)
        print(res.get_json())
        #写入cookies
        if res.get_cookie():
            setattr(Context,'cookies',res.get_cookie())
#
if __name__ == '__main__':
    unittest.main()
# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:29
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :Api_testcase.py
# @Software   :PyCharm
import unittest
from ddt import ddt,data
from api_auto.common.do_logging import Mylog
from api_auto.common.do_config import *
from api_auto.common.do_excel import do_excel
from api_auto.common.http_request import Http_request
from api_auto.common import project_path
config_value = Readconfig().read_config(project_path.config_path,'Case','button')
test_data = do_excel().readdata(config_value)
Mylogger = Mylog()
COOKIES=None
@ddt#有遍历的作用
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)#把excel里面读取好的数据传进来，脱掉[],再按逗号划分，分别成为一个case的输入数据，每个输入数据可以按字典取值
    def test_api(self,item):
        Mylogger.info(u'目前正在执行第{}条用例'.format(item['case_id']))
        # Mylog().info('-------------开始检查我们的URL------------------------------')
        # Mylog().debug('url:{}'.format(item['url']))
        # Mylog().info('-------------开始检查我们的data------------------------------')
        # Mylog().debug('data:{}'.format(item['data']))
        global COOKIES
       # Mylog().info('-------------开始http请求------------------------------')
        res = Http_request().http_request(item['url'],item['data'],item['http_method'],COOKIES)
        # Mylog().info('-------------结束http请求-----------------------------')
        # Mylog().debug("登陆请求结果：{}".format(res.json()))
        if res.cookies:
            COOKIES = res.cookies
       # Mylog().info('-------------开始断言-----------------------------')
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            result='Pass'
        except AssertionError as e:
            Mylog().error("断言出错了{}".format(e))
            result ='Failed'
            raise e
        # finally:
        #
        #     Mylog().info('-------------测试结果：{}------------------------'.format(result))

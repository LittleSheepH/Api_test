# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:29
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :Api_testcase.py
# @Software   :PyCharm
import unittest
from HomeWork_1207.logging_1207.http_request import Http_request
from ddt import ddt,data
from HomeWork_1207.logging_1207.do_logging import do_logging
from HomeWork_1207.logging_1207.do_config import *
from HomeWork_1207.logging_1207.do_excel import do_excel
from HomeWork_1207.logging_1207.http_request import Http_request
config_value = Readconfig().read_config('do_logging.conf')
test_data = do_excel().readdata(config_value['button'])
conf = Readconfig().read_config('do_logging.conf')
logset=do_logging().setlogging(conf['logger'],conf['login_level'],conf['logout_level'],conf['logfile_name'],
                               conf['formatter'])

COOKIES=None
@ddt#有遍历的作用
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)#把excel里面读取好的数据传进来，脱掉[],再按逗号划分，分别成为一个case的输入数据，每个输入数据可以按字典取值
    def test_api(self,item):
        logset.info('目前正在执行第{}条用例'.format(item['case_id']))
        logset.info('-------------开始检查我们的URL------------------------------')
        logset.debug('url:{}'.format(item['url']))
        logset.info('-------------开始检查我们的data------------------------------')
        logset.debug('data:{}'.format(item['data']))
        global COOKIES
        logset.info('-------------开始http请求------------------------------')
        res = Http_request().http_request(item['url'],item['data'],item['http_method'],COOKIES)
        logset.info('-------------结束http请求-----------------------------')
        logset.debug("登陆请求结果：{}".format(res.json()))
        if res.cookies:
            COOKIES = res.cookies
        logset.info('-------------开始断言-----------------------------')
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            result='Pass'
        except AssertionError as e:
            logset.error("断言出错了{}".format(e))
            result ='Failed'
            raise e
        logset.info('-------------测试结果：{}------------------------'.format(result))

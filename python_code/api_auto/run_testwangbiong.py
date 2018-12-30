# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:42
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :run_test.py
# @Software   :PyCharm
import unittest
from api_auto.common import HTMLTestRunnerNew
from api_auto.test_case.Api_testcase import TestHttpRequest
from api_auto.common import project_path


suite=unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


with open(project_path.report_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title="Api接口测试",description="登陆/充值接口测试",tester="王丹慧")
    runner.run(suite)

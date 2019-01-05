# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:42
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :run_test.py
# @Software   :PyCharm
import unittest
from HomeWork_1207.logging_1207 import HTMLTestRunnerNew
from HomeWork_1207.logging_1207.Api_testcase import *


suite=unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


with open('test_Api_report.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title="Api接口测试",description="登陆/充值接口测试",tester="王丹慧")
    runner.run(suite)

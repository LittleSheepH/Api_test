# -*-coding:utf-8-*-
# @Time       :2018/12/23 9:18
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :run_test_suite.py
# @Software   :PyCharm
import unittest
from api_auto_class.common import HTMLTestRunnerNew
from api_auto_class.common import concants
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromTestCase(TestRegister))
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
discover = unittest.defaultTestLoader.discover(concants.test_cases,pattern='test*.py')
#top_level_dir 如果有二级目录时候
with open(concants.report_html,'wb') as file:

    runner  = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='API',description='API测试报告',tester='DaBaiCai')
    runner.run(discover)
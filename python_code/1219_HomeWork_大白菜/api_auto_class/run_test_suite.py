# -*-coding:utf-8-*-
# @Time       :2018/12/23 9:18
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :run_test_suite.py
# @Software   :PyCharm
import unittest
from api_auto_class.testcases.test_register import TestRegister
suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestRegister))

runner = unittest.TextTestRunner()
runner.run(suite)
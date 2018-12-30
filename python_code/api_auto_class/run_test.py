# -*-coding:utf-8-*-
# @Time       :2018/12/21 7:33
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :run_test.py
# @Software   :PyCharm
from api_auto_class.common.doexcel import readcase
from api_auto_class.common.request import Request
from api_auto_class.common import concants
import os
do_excel= readcase(concants.data)
sheetnames=do_excel.get_sheet_names()
print(sheetnames)
case_list=['register']
for sheetname in sheetnames:
    if sheetname in case_list:
        cases =do_excel.get_case(sheetname)#返回的是一个列表
        print('测试用例个数',len(cases))
        for case in cases:#遍历测试用例列表，每个列表元素是一个实例，实例的属性才是要的值，每进for一次，就取一个case实例
                #print("case信息;",case.__dict__)#打印case信息,每个object都有这个属性，打印每个object的值，是一个字典
            data = eval(case.data)
            resp = Request(method=case.method,url=case.url,data=data)
            print(resp.get_statue_code())
                #判断接口响应是否和excel里面的expected的值一致
            print(data)
            print(resp.get_text())
            print(case.excepted)
            # do_excel.write_actural_by_case_id(sheetname,case.case_id,resp.get_text())
            if case.excepted== resp.get_text():
                print("resule:PASS")
                do_excel.write_actural_by_case_id(sheetname,case.case_id,resp.get_text(),'PASS')
            else:
                print("result:FAIL")
                do_excel.write_actural_by_case_id(sheetname, case.case_id, resp.get_text(),'FAIL')

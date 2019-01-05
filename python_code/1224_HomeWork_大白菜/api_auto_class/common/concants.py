# -*-coding:utf-8-*-
# @Time       :2018/12/21 6:37
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :concants.py
# @Software   :PyCharm
#常量管理
import os
#obspath跟realpath同，file是当前文件
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#项目根路径

#获取当前文件的文件夹dirname
configs_dir = os.path.join(base_dir,'configs')
# print(configs_dir)

datas_dir =os.path.join(base_dir,'datas')
data=os.path.join(datas_dir,'testdatas.xlsx')
# print(data)
# print(datas_dir)

reports_dir= os.path.join(base_dir,'reports')
# print(reports_dir)

logs_dir = os.path.join(base_dir,'logs')
# print(logs_dir)
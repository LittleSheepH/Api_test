# -*-coding:utf-8-*-
# @Time       :2018/12/20 6:38
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :studyjson.py
# @Software   :PyCharm
import json
dist='{"mobilephone":"18611223344","pwd":"1234567890"}'
# str_test=json.dumps(dict)
# print(str_test)
dict_test=json.loads(dist)#字符串转化为字典
print(dict_test)
print(type(dict_test))
str2='{"mobilephone":1861223344,"pwd":1234567890}'#key必须是双引号引起来
a=json.loads(str2)
print(a)
print(json.dumps(a))#字典转化为json
print(type(json.dumps(a)))

#字符编码
dict_obj={"status":1,"code":"10001","data":None,"msg":"注册成功"}
str_obj=json.dumps(dict_obj)
print(str_obj)
print(type(str_obj))
print('*'*50)
dict_obj={"status":1,"code":"10001","data":None,"msg":"注册成功"}
str_obj=json.dumps(dict_obj,ensure_ascii=False,indent=4)
print(str_obj)
print(type(str_obj))

#load 将文件里面的json反序列为str,贴到那个json自动识别程序如果能转换就是正常的
f=open('datas/data.json')#进入目录路径就不用写'/'了
s=json.load(f)#有乱码怎么办
print(s)

#dump将dict写入到文件
dict_obj={'a':1,'b':None}
f=open('datas/data.json','w+')
json.dump(dict_obj,fp=f)




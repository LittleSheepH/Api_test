# -*-coding:utf-8-*-
# @Time       :2018/12/23 0:18
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :study_re.py
# @Software   :PyCharm
import re
from api_auto_class.common.config import Configloader
str = 'oHelloH'
patten = 'H'#正则表达式 string目标表达式，flags 标识
res =re.match(patten,str)#按照partten去str里面找，必须第一位就匹配才能找到，显示下标，后面的找不了
#如果要找多个需要用findall
print(res)#返回的查找的第一个字符串的下表
res1 = re.findall(patten,str)#找到所有字符，全部匹配，并且返回一个字典
print(res1)
res2 = re.search(patten,str)#任意位置开始找,并返回第一个的位置，
# match必须是开始就找到，search不用是开始的，但都只能返回一个
print(res2)
patten1='\d{11}'
s ='{"mobilephone":"13711223355","pwd":"1234567890","regname":"huihui"}'
res3 = re.findall(pattern=patten1,string=s)#d代表只匹配数字
print(res3[0])
ss =s.replace(res3[0],'13899888888899')
print(ss)
print("------------分隔符---------------------")
#自定义开始位置结束位置是一个变量名，只要能匹配到就可以了
conf = Configloader()
patten2=conf.get('Patten','patten')
s1='{"mobilephone":"${register}","pwd":"1234567890","regname":"huihui"}'
# patten2 ='\$\{(.*?)\}'
register='138000000001'
res4 = re.findall(patten2,s1)#使用正则表达式将变量名取出来.
# s使用点号来取得任意字符，*取得不同长度的字符，？表示至少找到一个
print(res4[0])
sss = s1.replace(res4[0],register)
print('res4',res4)
print(sss)

print('-------------------------分隔符-----------------------')
s5='{"mobilephone":"${register}","pwd":"1234567890","regname":"huihui"}'
res5=re.sub(patten2,register,s5)
print(res5)
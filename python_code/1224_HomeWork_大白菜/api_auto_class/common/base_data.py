# -*-coding:utf-8-*-
# @Time       :2018/12/25 22:08
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :base_data.py
# @Software   :PyCharm
from api_auto_class.common.config import Configloader
import re
conf = Configloader()

class Context:
    normal_user=conf.get('basic','normal_user')#这是一个类变量，初始化函数里面的变量是成员变量
    pwd=conf.get('basic','pwd')
class DoRegex:
    @staticmethod
    def replace(target):#查找并且替换
        patten = conf.get('Patten', 'patten')
        while re.search(patten,target):
            m = re.search(patten,target)
            key = m.group(1)
            user = getattr(Context,key)
            target = re.sub(patten,user,target,count=1)
        return target
if __name__ == '__main__':
    data='{"mobilephone":"${normal_user}","pwd":"${pwd}"}'
    s=DoRegex.replace(data)
    print(s)
    patten = conf.get('Patten', 'patten')
    # while re.search(patten, data):
    #     m = re.search(patten, data)
    #     print(m)
    #     # key = m.group(0)
        # print(key)
        # user = getattr(Context, key)
        # s= re.sub(patten, user, data, count=1)
    # print(s)
    # P ='(w)(ww)'
    # s4 ='www.lemonban.com'
    # M = re.search(P, s4)
    # S= re.sub(patten,'123',data)
    # print(S)
    # print(M)
    # print(M.group(1))
    # print(M.group(2))
    #
    #
    #
    #
    #

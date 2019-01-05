# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:48
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :do_config.py
# @Software   :PyCharm
import configparser
class Readconfig:
    def read_config(self,confname):
        cf = configparser.RawConfigParser()
        cf.read(confname,encoding='UTF-8')
        sub_data = {}
        for i in cf.sections():
            for j in cf.options(i):
                sub_data[j]=cf.get(i,j)
        return sub_data
                #print(j,"-----",cf.get(i,j))

if __name__ == '__main__':

    #sub_data = Readconfig().read002('do_logging.conf')

    print("==={}".format(sub_data))
    for i in sub_data.keys():
        print("==key==={}\n==Value==={}".format(i,sub_data[i]))
    for i in sub_data:
        print("====={}".format(sub_data[i]))




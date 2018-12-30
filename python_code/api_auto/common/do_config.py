# -*-coding:utf-8-*-
# @Time       :9/12/18下午12:48
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :do_config.py
# @Software   :PyCharm
import configparser

class Readconfig:
    def read_config(self,confname,section,option):
        cf = configparser.RawConfigParser()
        cf.read(confname,encoding='UTF-8')
        # sub_data = {}
        # for i in cf.sections():
        #     for j in cf.options(i):
        #         sub_data[j]=cf.get(i,j)
        # return sub_data
                #print(j,"-----",cf.get(i,j))
        return cf.get(section,option)


if __name__ == '__main__':
    from api_auto.common import project_path
    print(Readconfig().read_config(project_path.config_path,'Case','button'))








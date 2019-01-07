# -*-coding:utf-8-*-
# @Time       :2018/12/21 6:31
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :config.py
# @Software   :PyCharm
import configparser
#创建实例 加载配置文件，通过section，option定位东西
from api_auto_class.common import concants
import os
class  Configloader:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        file_name = os.path.join(concants.configs_dir, 'global.conf')
        self.conf.read(file_name,encoding='utf-8')
        if self.conf.getboolean('switch','on'):#读取开关值并且返回bool类型
            file_name = os.path.join(concants.configs_dir, 'online.conf')
            self.conf.read(file_name,encoding='utf-8')
        else:
            file_name = os.path.join(concants.configs_dir, 'test.conf')
            self.conf.read(file_name,encoding='utf-8')

    def get(self,sectin,option):
        return self.conf.get(sectin,option)

    def getbool(self,section,option):
        return self.conf.getboolean(section,option)

    def getint(self,section,option):
        return self.conf.getint(section,option)

    def getfloat(self,section,option):
        return self.conf.getfloat(section,option)


if __name__ == '__main__':
    config = Configloader()
    url =config.get('api','url_pre')
    print(url)


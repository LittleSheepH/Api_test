# -*-coding:utf-8-*-
# @Time       :9/12/18下午2:02
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :do_logging.py
# @Software   :PyCharm
import logging
from api_auto.common import project_path
from api_auto.common.do_config import Readconfig
class Mylog:
    def my_log(self,level,msg):
        # 收集器和收集级别
        My_logger = logging.getLogger(Readconfig().read_config(project_path.config_path,'Dolog','logger'))
        My_logger.setLevel(Readconfig().read_config(project_path.config_path,'Dolog','login_level'))
        # 设置输出渠道和级别
        ch = logging.StreamHandler()
        fh = logging.FileHandler(project_path.log_path,encoding='UTF-8')

        # ch.setLevel(Readconfig().read_config(project_path.config_path,'Dolog','logout_level'))
        ch.setLevel(level)
        fh.setLevel(level)
        #设置输出格式
        ch.setFormatter(logging.Formatter(Readconfig().read_config(project_path.config_path,'Dolog','formatter')))

        #连接
        My_logger.addHandler(ch)
        My_logger.addHandler(fh)
        if level=='DEBUG':
            My_logger.debug(msg)
        elif level=="INFO":
            My_logger.info(msg)
        elif level=='WARNING':
            My_logger.warning(msg)
        elif level == 'CRITICAL':
            My_logger.critical(msg)
        elif level == 'ERROR':
            My_logger.error(msg)
        My_logger.removeHandler(ch)
        My_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log("INFO",msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__ == '__main__':
        my_logger=Mylog()
        my_logger.debug("66666")
        my_logger.info('777777')
        my_logger.error('8888888')
        my_logger.critical('9999999')


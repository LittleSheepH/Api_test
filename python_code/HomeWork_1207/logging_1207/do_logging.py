# -*-coding:utf-8-*-
# @Time       :9/12/18下午2:02
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :do_logging.py
# @Software   :PyCharm
import logging
class do_logging:
    def setlogging(self,loggername,login_level,logout_level,logfile_name,formatter):
        # 收集器和收集级别
        Bai_logger = logging.getLogger(loggername)
        Bai_logger.setLevel(login_level)
        # 设置输出渠道和级别

        ch = logging.StreamHandler()

        fh = logging.FileHandler(logfile_name)
        ch.setLevel(logout_level)
        fh = logging.FileHandler(logfile_name)
        fh.setLevel(logout_level)
        #设置输出格式
        ch.setFormatter(logging.Formatter(formatter))
        fh.setFormatter(logging.Formatter(formatter))

        #连接
        Bai_logger.addHandler(ch)
        Bai_logger.addHandler(fh)
        return Bai_logger

if __name__ == '__main__':
    from HomeWork_1207.logging_1207.do_config import Readconfig

    conf = Readconfig().read_config('do_logging.conf')
    logset=do_logging().setlogging(conf['logger'],conf['login_level'],conf['logout_level'],conf['logfile_name'],
                               conf['formatter'])
    logset.info("info")
    logset.error('error')










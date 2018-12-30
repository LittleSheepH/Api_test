import os
#专门存储路径
base_path =os.path.split(os.path.split( os.path.realpath(__file__))[0])[0]
#配置文件的路径
config_path = os.path.join(base_path,'conf','do_logging.conf')
#测试报告路径
report_path = os.path.join(base_path,'test_result','report','test_api.html',)
#日志路径
log_path = os.path.join(base_path,'test_result','logs','test_api.txt')
#测试用例路径
case_path = os.path.join(base_path,'test_datas','Api_test_case.xlsx')
if __name__ == '__main__':
    print(config_path)
    print(report_path)
    print(log_path)
    print(case_path)
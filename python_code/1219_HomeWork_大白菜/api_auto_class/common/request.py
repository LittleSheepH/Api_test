# -*-coding:utf-8-*-
# @Time       :2018/12/18 23:34
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :request.py
# @Software   :PyCharm
import requests
#from api_auto1.common import doexcel
class Request:
    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=='get':
                self.resp= requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=='post':
                self.resp = requests.post(url=url, data=data, cookies=cookies,headers=headers)
        except Exception as e :
            raise e
    def get_statue_code(self):
        return self.resp.status_code
    def get_text(self):
        return self.resp.text
    def get_json(self):
        return self.resp.json()


# -*-coding:utf-8-*-
# @Time       :2018/12/18 23:34
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :request.py
# @Software   :PyCharm
import requests
import json
#from api_auto1.common import doexcel
class Request:
    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=='get':
                self.resp= requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=='post':
                self.resp = requests.post(url=url,data=data, cookies=cookies,headers=headers)
        except Exception as e :
            raise e
    def get_statue_code(self):
        return self.resp.status_code
    def get_text(self):
        return self.resp.text
    def get_json(self):
        resp_text = json.dumps(self.resp.json(),ensure_ascii=False,indent=4)
        # print('response:',resp_text)
        return self.resp.json()
    def get_cookie(self,key=None):
        if key is not None:
            return self.resp.cookies[key]
        else:
            return  self.resp.cookies
if __name__ == '__main__':
    data={"mobilephone": "13417543096", "pwd": "12345678"}
    url ='http://test.lemonban.com/futureloan/mvc/api/member/register'
    url1='http://120.78.128.25:8080/futureloan/mvc/api/member/recharge'
    res=Request('get',url1,data)
    print(res.get_text())

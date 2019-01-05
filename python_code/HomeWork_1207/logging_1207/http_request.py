# -*-coding:utf-8-*-
# @Time       :9/12/18上午11:56
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :http_request.py
# @Software   :PyCharm
import requests
class Http_request:
    def http_request(self,url,param,http_method,cookie=None):
        if http_method =='get':
            res = requests.get(url,param,cookies=cookie)
        else:
            res = requests.post(url,param,cookies=cookie)
        return res
if __name__ == '__main__':
    data ={"mobilephone": "13417543096", "pwd": "12345678"}
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
    url1 = 'http://120.78.128.25:8080/futureloan/mvc/api/member/recharge'
    res = Http_request().http_request( url, data,'get')
    print(res.status_code)
    print(res.json())


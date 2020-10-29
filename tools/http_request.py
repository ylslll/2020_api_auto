import requests
from tools.GetData import *

class HttpRequest():

    def http_request(self, host, url, method, data):
        headers = {"content-type": "application/json;charset=utf-8", "token": getattr(GetData, "Token")}
        URL = "{0}{1}".format(host, url)
        data=data.encode('utf-8')
        try:
            if method.lower() == "post":
                re = requests.post(URL, data, headers=headers)
            elif method.lower() == "get":
                re = requests.get(URL, data, headers=headers)
        except Exception as e:
            raise e
        return re

if __name__ == '__main__':
    # re11 = HttpRequest().http_request('https://test-admin.yelopack.com','/api/basicdata/api/management/login','post',data='{"password":"123456","userAccount":"33","loginType":"2"}')
    re22 = HttpRequest().http_request('https://test-vip.yelopack.com','/api/api/user/register','post',data='{"mobile":"17888323984","email":"","verifyCode":"207303","password":"Aa123456","checkPassword":"Aa123456"}')
    # print(re11.status_code, re11.json())
    print(re22.status_code,re22.json())


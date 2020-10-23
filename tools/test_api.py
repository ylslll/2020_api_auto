import unittest
from ddt import ddt,data
from tools.DoExcel import ReadTestData
from tools.FilePath import *
from tools.my_log import MyLog
from tools.read_conf import ReadConf
from tools.http_request import HttpRequest
from tools.GetData import *
import re
import time


# 获取测试数据
test_data = ReadTestData().read_test_data(test_data_tray_path)

@ddt
class TestApiTray(unittest.TestCase):
    def setUp(self):
        MyLog().info("-----------------开始测试-----------------")

    @data(*test_data)
    def test_api(self, item):
        MyLog().info("执行用例{0}{1}".format(item["case_id"], item["title"]))
        host = ReadConf().read_conf(conf_path, "HTTP", "test_host")

        res = HttpRequest().http_request(host, url=item["url"], data=item["data"], method=item["method"])
        MyLog().info("接收到的测试数据{0}".format(item["data"]))

        # 登录获取token
        if item["title"] == "正常登录":
            setattr(GetData, "Token", res.headers["token"])

        # if item['title'] == '新增客户成功':
        if re.match(r'新增C客户',item['title']):
            ReadTestData().write_customer_name(test_data_tray_path)


        global test_result
        # 断言
        try:
            self.assertEqual(item["expected"], res.json()["errcode"])
            test_result = "Pass"
        except AssertionError as e:
            test_result = "Failed"
            MyLog().info("执行用例失败啦{0}".format(e))
            raise e
        finally:
            ReadTestData().write_result(test_data_tray_path, item["sheet_name"], item["case_id"]+1, res.json(), test_result)
            MyLog().error("测试获取到的结果是：{0}".format(res.json()))
        time.sleep(3)

    def tearDown(self):
        MyLog().info("-----------------测试结束-------------------")

if __name__ == '__main__':
    re=TestApiTray().test_api















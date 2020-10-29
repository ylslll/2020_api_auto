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
from tools.get_locationX import getLocationX
import json
from tools.mysql import MysqlCon


# 获取测试数据
test_data = ReadTestData().read_test_data(test_data_tray_path)

@ddt
class TestApiTray(unittest.TestCase):
    def setUp(self):
        MyLog().info("-----------------开始测试-----------------")

    @data(*test_data)
    def test_api(self, item):
        MyLog().info("执行用例{0}{1}".format(item["case_id"], item["title"]))
        # 根据接口所属领域区分，来获取对应的host
        if re.match(r'^admin',item['sheet_name']):
            host = ReadConf().read_conf(conf_path, "HTTP", "test_host")
        elif re.match(r'^web', item['sheet_name']):
            host = ReadConf().read_conf(conf_path, "HTTP", "test_host_web")
        # 登录和注册接口不需要token
        if re.match(r'注册',item['title']):
            setattr(GetData, 'Token', None)

        # 检查用例的入参是否需要依赖另一接口返回数据
        if item['rely_on_case_id'] != 'None':
            # 获取所依赖的字段值
            result_data = ReadTestData().read_result(filename=test_data_tray_path, sheet_name=item['sheet_name'], case_id=item['rely_on_case_id'],rely_on_value=item['rely_on_value'])
            # 获取验证码接口
            if item['url'] == '/api/api/verificationCode/getVerificationCode':
                locationX = getLocationX(float(result_data['random']))
                result_data.pop('random')
                result_data['locationX'] = locationX
                ReadTestData().write_deff_telephone(filename=test_data_tray_path)
            request_data = json.loads(item['data'])
            for k, v in result_data.items():
                request_data[k] = v
            item['data'] = json.dumps(request_data)
            # 将替换后的data写入到excel中
            ReadTestData().write_rely_on_data(filename=test_data_tray_path, sheet_name=item['sheet_name'], case_id=item['case_id'], replace_datas=item['data'])

        # 注册接口，查询数据库获取验证码
        if item['url'] == '/api/api/user/register':
            mobile = getattr(GetData, 'mobilephone')
            data1 = json.loads(item['data'])
            data1['mobile'] = mobile
            select_result = MysqlCon().select('SELECT verification_code FROM t_verification_code WHERE created_by=%s ORDER BY id DESC LIMIT 1'%mobile, 'test_yelo_basicdata')
            verifyCode = select_result[0][0]
            data1['verifyCode'] = verifyCode
            item['data'] = json.dumps(data1)
            ReadTestData().write_rely_on_data(filename=test_data_tray_path, sheet_name=item['sheet_name'], case_id=item['case_id'], replace_datas=item['data'])

        # 执行
        res = HttpRequest().http_request(host, url=item["url"], data=item["data"], method=item["method"])
        MyLog().info("接收到的测试数据{0}".format(item["data"]))

        # 登录获取token
        if item["title"] == "正常登录" or item["title"] =="注册成功":
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
    re = TestApiTray().test_api















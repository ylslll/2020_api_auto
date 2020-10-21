import unittest
import HTMLTestRunner

from tools.FilePath import *
from tools.test_api import TestApiTray
from tools.sned_email import send_email

class Run():
    def run(self,test_name):
        suite=unittest.TestSuite()
        loader=unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(test_name))

        test_api_name = str(test_name).split('.')[-1]
        report_file=report_path+str(test_api_name)[2:-2]+".html"
        with open(report_file,"wb") as f:
            runner=HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title="接口测试报告",description="云盘接口测试")
            runner.run(suite)

        #发送邮件
        send_email(report_file)


if __name__ == '__main__':
    Run().run(TestApiTray)


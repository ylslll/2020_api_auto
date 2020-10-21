import os
import datetime

#读取项目的根目录
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#拼接路径
#配置文件路径
conf_path=os.path.join(project_path,'conf','conf.ini')

#设置日志文件路径
log_path=os.path.join(project_path,"test_result","logs","2020-auto-api.txt")

#设置测试用例文件路径
test_data_tray_path=os.path.join(project_path,"test_data","test_tray.xlsx")
test_data_logistics_path=os.path.join(project_path,"test_data","test_logistics.xlsx")
test_data_warehouse_path=os.path.join(project_path,"test_data","test_warehouse.xlsx")

#设置测试报告路径
report_path=os.path.join(project_path,"test_result","html_test_report","test_report")
import logging
from tools.FilePath import *

class MyLog():
    def my_log(self,level,msg):
        #定义一个日志收集器
        my_logger=logging.getLogger('2020_api_auto')
        #定义日志收集器级别
        my_logger.setLevel(logging.DEBUG)
        #设置日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #定义一个我们自己的输出渠道
        #输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        #输出到指定文件
        fh=logging.FileHandler(log_path,encoding='utf-8',mode='a')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)

        #两者结合
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level=="WARNING":
            my_logger.warning(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        elif level=="CRITICAL":
            my_logger.critical(msg)

        #关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log("DEBUG",msg)

    def info(self,msg):
        self.my_log("INFO",msg)

    def warning(self,msg):
        self.my_log("WARNING",msg)

    def error(self,msg):
        self.my_log("ERROR",msg)

    def critical(self,msg):
        self.my_log("CRITICAL",msg)













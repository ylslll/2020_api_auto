import configparser  #导入模板读取配置文件
class ReadConf():
    def read_conf(self,filepath,session,option):
        #实例化
        cf=configparser.ConfigParser()
        #打开配置文件，并设置字符集
        cf.read(filepath)
        return cf[session][option]


from doctest import REPORTING_FLAGS
from ntpath import realpath
import yaml
import os
#from config.config import ROOT_DIR

#print(__file__) #文件 当前路径
# curpath = os.path.realpath(__file__)
# # #print(curpath)
# root_dir = os.path.dirname(os.path.dirname(curpath))#获取根文件路径
# # print(root_dir)
# yaml_path = os.path.join(root_dir,"data","test_data_login.yml") #获取yaml文件路径
# print(yaml_path)

def readyml(data_name):
    '''读取yaml文件内容
    参数path: 相对路径，起始路径：项目的根目录
    realPath: 文件的真实路径,绝对路径地址 '''

    curpath = os.path.realpath(__file__)
    root_dir = os.path.dirname(os.path.dirname(curpath))#获取根文件路径
    #print("root_dir = %s" %root_dir)
    yamlPath = os.path.join(root_dir,"data",data_name)
    #print("yaml_path = %s" %yamlPath)

    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
        # open方法打开直接读出来
    
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.safe_load(cfg)
    f.close()

    # 用load方法转字典
    #print("读取的测试文件数据：%s"%d)
    return d

if __name__ == '__main__':
    #yaml_path = os.path.join(root_dir,"data","sigin.yml")
    data_name = "check_data.yml"
    d =  readyml(data_name)
    print(d)




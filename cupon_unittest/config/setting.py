import os,sys
Base_dir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(Base_dir)

#测试数据文件
Test_Data_yaml=os.path.join(Base_dir,"testdata")
# 测试报告目录
TEST_REPORT = os.path.join(Base_dir,"report")
# 测试用例目录
TEST_DIR = os.path.join(Base_dir,"testcase")
# 配置文件
CONFIG_DIR = os.path.join(Base_dir,"database","user.ini")
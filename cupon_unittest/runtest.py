import unittest,os,time
from testcase import test_memberMan
from config import setting
from package import HTMLTestRunner
from public.models.newReport import new_report
from public.models.sendmail import send_mail
from public.models import sendmail1

if not os.path.exists(setting.TEST_REPORT):os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

def add_case(test_path=setting.TEST_DIR):
    discover = unittest.defaultTestLoader.discover(test_path,pattern='test*.py')
    return discover


def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='优惠券系统页面自动化测试报告',description='环境：windows 10 浏览器：chrome')
    runner.run(all_case)


    fp.close()
    report = new_report(setting.TEST_REPORT) #调用模块生成最新的报告
    # send_mail(report) #调用发送邮件模块
    # sendmail1.email(report)

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)



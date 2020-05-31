from selenium import webdriver
import unittest
import time,yaml,random,ddt,os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException
from config import setting

try:
    str1=setting.Test_Data_yaml
    str=setting.Test_Data_yaml+ '/' +'memberdel_data.yaml'
    f=open(setting.Test_Data_yaml+ '/' +'memberdel_data.yaml',encoding='utf-8')
    testData=yaml.load(f,Loader=yaml.FullLoader)
    print("memberdel_data.yaml文件存在")
except FileNotFoundError as fileN:
    # log=Log()
    # log.error("文件不存在：{0}".format(fileN))
    print("memberadd_data.yaml文件不存在")

@ddt.ddt
class memberdel(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    @ddt.data(*testData)
    def test_delMember(self,datayaml):
        driver = self.driver
        lists = driver.find_elements_by_xpath('.//span[@class="ng-binding"]')
        lists[1].click()
        driver.find_element_by_xpath('.//span[@class="ng-binding"]').click()
        driver.find_element_by_xpath('.//span[@class="font-bold ng-binding"]').click()

        WebDriverWait(driver,20).until(EC.presence_of_all_elements_located())
        driver.find_element_by_xpath('.//input[@ng-model="name"]').send_keys(datayaml['data']['membername'])
        driver.find_element_by_class_name('btn nh-btn-info').click()

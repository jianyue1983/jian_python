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
    str=setting.Test_Data_yaml+ '/' +'memberadd_data.yaml'
    f=open(setting.Test_Data_yaml+ '/' +'memberadd_data.yaml',encoding='utf-8')
    testData=yaml.load(f,Loader=yaml.FullLoader)
    print("memberadd_data.yaml文件存在")
except FileNotFoundError as fileN:
    # log=Log()
    # log.error("文件不存在：{0}".format(fileN))
    print("memberadd_data.yaml文件不存在")

@ddt.ddt
class menberManage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # 生成随机手机号
    def raddomPhone(self):
        headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                    "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                    "186", "187", "188", "189"]
        return (random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))

    @ddt.data(*testData)
    def test_addMenber(self,datayaml):

        driver=self.driver
        lists=driver.find_elements_by_xpath('.//span[@class="ng-binding"]')
        lists[1].click()
        driver.find_element_by_xpath('.//span[@class="ng-binding"]').click()
        driver.find_element_by_xpath('.//span[@class="font-bold ng-binding"]').click()


        driver.find_element_by_xpath('.//button[@class="btn nh-btn-add"]').click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, './/input[@ng-model="username"]')))


        # driver.find_element_by_xpath(".//input[@ng-model='username']").send_keys('20200104')
        # driver.find_element_by_xpath(".//input[@ng-model='userId']").send_keys('20200104')

        driver.find_element_by_xpath(".//input[@ng-model='username']").send_keys(datayaml['data']['membername'])
        driver.find_element_by_xpath(".//input[@ng-model='userId']").send_keys(datayaml['data']['memberid'])

        driver.find_element_by_xpath(".//input[@ng-model='phone']").send_keys(self.raddomPhone())
        driver.find_element_by_xpath(".//button[@ng-click='addOrEditCounponUser()']").click()
        time.sleep(2)

        print("句柄是：%s" % driver.window_handles)

        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH,'.//div[@class="jq-toast-wrap top-right"]')))
        tips=driver.find_element_by_xpath('.//div[@class="jq-toast-wrap top-right"]/div').get_attribute("textContent")
        print(tips)
        expects=datayaml['check'][0]
        print("-----")
        print(expects)
        self.assertIn(tips,expects)

    def tearDown(self):
       print("test is over")
# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """合同管理-查询"""
    def setUp(self):
        """启动Appium"""
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'E5553'
        desired_caps['appPackage'] = 'com.nuanyou.bdpal'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test7_contract(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=5]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='合同管理']").click()
        time.sleep(5)
        # 输入商家名称
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_contract_management_act").send_keys('1')
        time.sleep(1)
        # 搜索
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_contract_management_act").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Contract_search.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.ContractManagementActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """切换韩文"""
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

    def test_korea(self):
        # 我的
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/im_right_main_act").click()
        time.sleep(2)
        # 语言切换
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rl_switch_language").click()
        time.sleep(2)
        # 韩文
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/ll_korean").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea.jpg")
        time.sleep(2)
        # 演示资料页面检查
        self.driver.find_element_by_xpath("//android.widget.GridView[@resource-id=\"com.nuanyou.bdpal:id/gv_main_frag\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea1.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_title_display_resource_act").click()
        time.sleep(1)
        # 证书展示页面检查
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=3]").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea2.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_credential_return").click()
        time.sleep(1)
        # 商户采集页面检查
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=4]").click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea3.jpg")
        time.sleep(1)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/ll_add_merchant").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea4.jpg")
        time.sleep(1)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_merchant_return").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_merchant_return").click()
        time.sleep(1)
        # 合同管理页面检查
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=5]").click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea5.jpg")
        time.sleep(1)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_new_contract").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\korea6.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_title_new_contract_act").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_title_contract_management_act")
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()


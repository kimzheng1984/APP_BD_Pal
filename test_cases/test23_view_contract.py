# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """商户采集-查看合同"""
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

    def test14_mch_view_contract(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=4]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='商户采集']").click()
        time.sleep(15)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_item_merchant_location").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_dialog_view_contract").click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\mch_view_contract.jpg")
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]").click()
        time.sleep(1)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\mch_new_contract1.jpg")
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_cancle_view_contract_act").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\mch_new_contract2.jpg")
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_back_relate_contract").click()
        time.sleep(1)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\mch_new_contract2.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.EditMerchantActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """商户采集"""
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

    def test6_merchant(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=4]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='商户采集']").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\MCH.jpg")
        time.sleep(5)
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MerchantAcquisitionActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


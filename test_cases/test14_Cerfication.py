# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """证书展示"""
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

    def test5_credential(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=3]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='证书展示']").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Cer.jpg")
        time.sleep(2)
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.CredentialActivity')
        except AssertionError:
            print activity
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_item_credential").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Cer1.jpg")
        try:
            self.assertEqual(activity, '.activity.CredentialActivity')
        except AssertionError:
            print activity
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_item_credential_show").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Cer2.jpg")
        try:
            self.assertEqual(activity, '.activity.CredentialActivity')
        except AssertionError:
            print activity

if __name__ == "__main__":
    unittest.main()


# coding=utf-8

from appium import webdriver
import unittest
import time

class BD(unittest.TestCase):
    """退出"""
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
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test2_logout(self):
        # 我的
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/im_right_main_act").click()
        time.sleep(2)
        # 退出登陆
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_exit_login").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\logout.jpg")

if __name__ == "__main__":
    unittest.main()


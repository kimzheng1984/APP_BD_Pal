# coding=utf-8

from appium import webdriver
import unittest
import time

class BD(unittest.TestCase):
    """登录与语言切换至中文"""
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

    def test_logout(self):
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\login.jpg")
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_login_account").clear()
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_login_account").send_keys('ceshi')
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_login_pwd").send_keys('111111')
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_login").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\main.jpg")
        time.sleep(2)
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MainActivity')
        except AssertionError:
            print activity

        self.driver.find_element_by_id("com.nuanyou.bdpal:id/im_right_main_act").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rl_switch_language").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/ll_china").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\main1.jpg")


if __name__ == "__main__":
    unittest.main()


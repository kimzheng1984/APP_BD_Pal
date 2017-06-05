# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """我的"""
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

    def test9_me(self):
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/im_right_main_act").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me.jpg")
        time.sleep(2)
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MainActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rl_switch_language").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me1.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.SwitchLanguageActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_switch_language_exit").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me2.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MainActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rl_modify_password").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me3.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.ModifyPasswordActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/fl_modify_password_exit").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me4.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MainActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/im_left_main_act").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\me5.jpg")
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.MainActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


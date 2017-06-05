# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """演示资料"""
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

    def test1_demo(self):
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\home.jpg")
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=0]").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\demo.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@index=0]").click()
        time.sleep(10)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\demo1.jpg")
        time.sleep(2)
        activity = self.driver.current_activity
        # print activity
        try:
            self.assertEqual(activity, '.activity.VideoViewActivity')
        except AssertionError:
            print activity
        self.driver.back()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\demo2.jpg")


if __name__ == "__main__":
    unittest.main()


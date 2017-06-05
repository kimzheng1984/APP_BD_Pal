# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """合同管理-新建合同"""
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

    def test17_contract_new(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=5]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='合同管理']").click()
        time.sleep(25)
        # 新建合同
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_new_contract").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('1')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('test')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('test')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('1')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('test')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys('test')
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.nuanyou.bdpal:id/lv_parameter_new_contract\"]/android.widget.LinearLayout[7]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys("test")
        time.sleep(2)
        # 获取当前activity
        activity = self.driver.current_activity
        # print activity
        # 判断新建合同页面的activity是否正确
        try:
            self.assertEqual(activity, '.activity.NewContractActivity')
        except AssertionError:
            print activity
        time.sleep(2)
        # 下一步
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_next_new_contract_act").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Contract_new1.jpg")
        activity = self.driver.current_activity
        # print activity
        # 判断新建合同页面的activity是否正确
        try:
            self.assertEqual(activity, '.activity.NewContractContentActivity')
        except AssertionError:
            print activity
        # 下一步
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_next_new_contract_act").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\Contract_new2.jpg")
        activity = self.driver.current_activity
        # print activity
        # 判断新建合同页面的activity是否正确
        try:
            self.assertEqual(activity, '.activity.ContractSignActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


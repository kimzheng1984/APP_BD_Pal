# coding=utf-8

from appium import webdriver
import unittest
import time


class BD(unittest.TestCase):
    """商户采集-新增商户"""
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

    def test15_new_mch(self):
        # xpath以index来定位控件
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=4]").click()
        # xpath以text来定位控件
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='商户采集']").click()
        time.sleep(15)
        # 新增商户
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/ll_add_merchant").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\new_mch.jpg")
        # 输入店名
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_new_merchant_name").send_keys('test')
        time.sleep(1)
        # 选择商家上线状态：隐藏
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rb_merchant_state_hide").click()
        time.sleep(1)
        # 单品状态：隐藏
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rb_product_state_hide").click()
        time.sleep(1)
        # 团购状态：隐藏
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rb_group_buy_state_hide").click()
        time.sleep(1)
        # 商品分类：购物
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/rb_merchant_assortment_shopping").click()
        time.sleep(1)
        # 输入短信接收手机
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/et_item_phone_1").send_keys('11111111111')
        time.sleep(2)
        # 请抓取：经纬度
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/btn_please_grab").click()
        time.sleep(1)
        # 第一次抓取经纬度，需加入获取位置
        # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # time.sleep(2)
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\new_mch_1.jpg")
        # 保存获取的经纬度
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/tv_finish_map").click()
        time.sleep(1)
        # 添加列表图
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_merchant_storefront").click()
        time.sleep(1)
        # 相册里选一张图
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/v_selected").click()
        # 完成
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/done").click()
        # 裁剪
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/btn_crop").click()
        time.sleep(1)
        # 保存
        self.driver.find_element_by_id("com.sonyericsson.photoeditor:id/filtershow_done").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\new_mch2.jpg")
        time.sleep(2)
        # 添加详情图
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/iv_merchant_shop_inner").click()
        time.sleep(1)
        # 相册里选一张图
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/v_selected").click()
        # 完成
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/done").click()
        # 裁剪
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/btn_crop").click()
        time.sleep(1)
        # 保存
        self.driver.find_element_by_id("com.sonyericsson.photoeditor:id/filtershow_done").click()
        self.driver.get_screenshot_as_file("C:\\WORK\\workspace\\python\\report\\BD\\new_mch3.jpg")
        time.sleep(2)
        # 获取当前activity
        activity = self.driver.current_activity
        # print activity
        # 判断新增商户的activity是否正确
        try:
            self.assertEqual(activity, '.activity.EditMerchantActivity')
        except AssertionError:
            print activity
        # 保存新增的商户
        self.driver.find_element_by_id("com.nuanyou.bdpal:id/ll_save_merchant").click()
        time.sleep(1)
        # 获取当前activity
        activity = self.driver.current_activity
        # print activity
        # 判断商户采集的activity是否正确
        try:
            self.assertEqual(activity, '.activity.MerchantAcquisitionActivity')
        except AssertionError:
            print activity


if __name__ == "__main__":
    unittest.main()


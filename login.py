# -*- coding: utf-8 -*-
'''
Created on 2016年1月26日

@author: wang
'''
#mycs登陆测试

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import strings
from itertools import count



class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = strings.url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #正常登陆
    def test_login(self):  
        login_count = 0
        driver = self.driver
        driver.get(self.base_url + "/")
        while login_count <=0:   
            driver.find_element_by_css_selector("div.top_bar > div > ul > li > a").click()
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(strings.login_username[login_count])
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(strings.login_pwd)
            driver.find_element_by_id("login_btn").click()
            print strings.login_name[login_count]
            print driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").text
            self.assertEqual(strings.login_name[login_count], driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").text)
            driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a").click()
            time.sleep(5)
            print login_count
            login_count = login_count + 1
            
#     #用户名密码空
#     def test_login_null(self):
#         driver = self.driver
#         driver.find_element_by_css_selector("div.top_bar > div > ul > li > a").click()
#         driver.find_element_by_id("login_btn").click()
#         self.assertEqual(strings.login_error1, driver.find_element_by_xpath("html/body/div[8]/form/div/ul/li[1]/span/text()"), u"用户名密码均为空时，测试异常")
#     
#     #密码错误
#     def test_login_pwd_wrong(self):
#         driver = self.driver
#         driver.find_element_by_css_selector("div.top_bar > div > ul > li > a").click()
#         driver.find_element_by_id("login_btn").click()
#         self.assertEqual(strings.login_error2, driver.find_element_by_xpath("html/body/div[8]/form/div/ul/li[1]/span/text()"), u"密码错误时，测试异常")      
#         
#     #密码位数不足六位
#     def test_login_pwd_less(self):
#         login_count = 0
#         driver = self.driver
#         driver.find_element_by_css_selector("div.top_bar > div > ul > li > a").click()
#         driver.find_element_by_id("login_btn").click()
#         self.assertEqual(strings.login_error2, driver.find_element_by_xpath("html/body/div[8]/form/div/ul/li[1]/span/text()"), u"密码错误时，测试异常")   
#        
#        
       
       
       
       
       
       
       
       
       
       
       
       
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.base_url = "http://5elementslearning.dev/"
        self.driver.implicitly_wait(30)
      
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "demosite/")
        driver.find_element_by_link_text("My Account").click()
        driver.find_element_by_name("email_address").clear()
        driver.find_element_by_name("email_address").send_keys("abc@demo.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("demo@123")
        driver.find_element_by_id("tdb5").click()
        driver.find_element_by_link_text("Log Off").click()
        driver.find_element_by_link_text("Continue").click()
    
    def tearDown(self):
        self.driver.close()
       

if __name__ == "__main__":
    unittest.main()

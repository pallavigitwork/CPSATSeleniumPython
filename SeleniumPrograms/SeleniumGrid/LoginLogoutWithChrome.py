# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver  = webdriver.Remote(
              command_executor="http://localhost:4444/wd/hub",
              desired_capabilities={
                  "browserName": "chrome",
            })
        
        self.base_url = "http://5elementslearning.dev/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/demosite/")
        driver.find_element_by_link_text("My Account").click()
        driver.find_element_by_name("email_address").clear()
        driver.find_element_by_name("email_address").send_keys("abc@demo.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("demo@123")
        driver.find_element_by_id("tdb5").click()
        driver.find_element_by_link_text("Log Off").click()
        driver.find_element_by_link_text("Continue").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

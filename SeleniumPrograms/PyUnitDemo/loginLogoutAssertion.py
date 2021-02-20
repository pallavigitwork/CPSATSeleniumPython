# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://5elementslearning.dev/"
        
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/demosite/")
        driver.find_element_by_link_text("My Account").click()
        driver.find_element_by_name("email_address").clear()
        driver.find_element_by_name("email_address").send_keys("abc@demo.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("dem123")
        driver.find_element_by_id("tdb5").click()
        if(driver.page_source.find("My Account Information")!=-1):
            
           
            
                driver.find_element_by_link_text("Log Off").click()
                driver.find_element_by_link_text("Continue").click()
                print("valid user credential")
                self.assertTrue(True,"valid user credential")
        else:
            #print("bad user credential")
            self.assertFalse(True,"bad user credential")
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

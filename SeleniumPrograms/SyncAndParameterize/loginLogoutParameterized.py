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
        driver.get(self.base_url + "demosite/")
        file = open("D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\datasets\data.csv", "r") 
        for line in file:
            driver.find_element_by_link_text("My Account").click()
            data=line.split(",") #an array of strings data[0] - username, data[1] - passwd
            print(data)
            driver.find_element_by_name("email_address").clear()
            driver.find_element_by_name("email_address").send_keys(data[0])
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(data[1].strip())  #Removing the new line char \n
            driver.find_element_by_id("tdb5").click()
            if(driver.page_source.find("My Account Information")!=-1):
                driver.find_element_by_link_text("Log Off").click()
                driver.find_element_by_link_text("Continue").click()
                print("Valid user credential")
                self.assertTrue(True,"valid user credential")
            else:
                print("Bad user credential")
                self.assertFalse(True,"bad user credential")
        file.close()
         
    def tearDown(self):
        self.driver.quit()
       
if __name__ == "__main__":
    unittest.main()

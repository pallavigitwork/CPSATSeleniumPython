# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class WorkWithAlerts(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://the-internet.herokuapp.com/javascript_alerts"
    
    
    def test_alerts(self):
        browser=self.driver
        browser.get(self.base_url)
        browser.find_element_by_xpath("//button[contains(text(),'Click for JS Confirm')]").click()
        time.sleep(2)
        alert=browser.switch_to_alert()
        print(alert.text)
        time.sleep(5)
        alert.dismiss() #press on OK button
        time.sleep(5)
        if(browser.page_source.find("You clicked: Cancel")):
            print("Alert handled")
        else:
            print("Error")
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class WorkWithAlerts(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://the-internet.herokuapp.com/windows"
          
    
    def test_alerts(self):
        browser=self.driver
        browser.get(self.base_url)
        browser.find_element_by_link_text("Click Here").click()
        wndHand=browser.window_handles
        browser.switch_to_window(wndHand[1])
        browser.close()
        browser.switch_to_window(wndHand[0])
        #browser.close()
        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

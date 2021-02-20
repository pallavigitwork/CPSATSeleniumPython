# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class FrameExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "https://the-internet.herokuapp.com/nested_frames"

    
    def test_frame(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.switch_to_frame(driver.find_element_by_name("frame-top"))
        driver.switch_to_frame(driver.find_element_by_name("frame-left"))
        if(driver.page_source.find("LEFT")):
            print("Switched")
        else:
            print("Error")
        driver.switch_to_default_content() #switch back to the main page
        print(driver.page_source)
       
    
    def tearDown(self):
        self.driver.quit()
  
if __name__ == "__main__":
    unittest.main()

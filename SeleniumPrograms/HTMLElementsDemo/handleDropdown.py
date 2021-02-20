# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
import time

class SelectExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.base_url = "http://5elementslearning.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dropdown(self):
        browser=self.driver
        browser.get('http://5elementslearning.dev/demosite')
        browser.maximize_window()
        browser.find_element_by_link_text("My Account").click()
        browser.find_element_by_link_text("Continue").click()
        drpdwnCountry=Select(browser.find_element_by_name("country")) #drop down country web element
        drpdwnCountry.select_by_visible_text("Cyprus")
        time.sleep(2)
        print(drpdwnCountry.first_selected_option.text)
        drpdwnCountry.select_by_value("188")
        time.sleep(2)
        print(drpdwnCountry.first_selected_option.text)
           
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

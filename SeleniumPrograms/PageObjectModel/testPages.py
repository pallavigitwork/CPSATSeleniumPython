import unittest
from selenium import webdriver
from Day12.pages import *
from Day12.locators import *
from selenium.webdriver.common.by import By

class TestLoginLogout(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.get("http://5elementslearning.dev/demosite")
        
    def test_sign_in_with_valid_user(self):
        homePage = HomePage(self.driver)
        homePage.click_myaccount()
        loginPage=LoginPage(self.driver)
        loginPage.login("abc@demo.com","demo@123")
        logoutPage=LogoutPage(self.driver)
        logoutPage.logout()


if __name__ == "__main__":
    unittest.main()
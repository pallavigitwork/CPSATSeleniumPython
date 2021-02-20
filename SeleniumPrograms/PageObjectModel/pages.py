from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Day12.base import Page
from Day12.locators import *
from selenium.webdriver.support.ui import WebDriverWait


# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class HomePage(Page):
    def click_myaccount(self):
        self.find_element(*HomePageLocators.MYACCOUNT).click()
        return self.driver
    
class LoginPage(Page):
    def enter_email(self, email):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def enter_password(self,pwd):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(pwd)

    def click_login_button(self):
        self.find_element(*LoginPageLocators.SIGNIN).click()

    def login(self, email,pwd):
        self.enter_email(email)
        self.enter_password(pwd)
        self.click_login_button()
        return self.driver


class LogoutPage(Page):
    def click_logoff(self):
        self.find_element(*LogoutPageLocators.LOGOFF).click()

    def click_continue(self):
          self.find_element(*LogoutPageLocators.CONTINUE).click()

    def logout(self):
        self.click_logoff()
        self.click_continue()
       
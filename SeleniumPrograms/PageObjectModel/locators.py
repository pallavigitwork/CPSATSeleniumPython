from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class HomePageLocators(object):
  MYACCOUNT       = (By.LINK_TEXT, 'My Account')
  

class LoginPageLocators(object):
  EMAIL         = (By.NAME, 'email_address')
  PASSWORD      = (By.NAME, 'password')
  SIGNIN        = (By.ID, 'tdb5')

class SearchPageLocators(object):
    SEARCH      =(By.NAME, 'keywords')

class LogoutPageLocators(object):
  LOGOFF         = (By.LINK_TEXT, 'Log Off')
  CONTINUE      = (By.LINK_TEXT, 'Continue')
 
 
class ChangeProfilePageLocators(object):
    CHANGEPROFILE   =(By.LINK_TEXT, 'View or change my account information.')
    LASTNAME    =(By.NAME, 'lastname')
    CTNBTN  =(By.ID, 'tdb5')
from selenium import webdriver
from selenium.webdriver.support.select import Select


import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implicit Wait
        self.base_url = "http://5elementslearning.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        browser=self.driver
        browser.get('http://5elementslearning.com/demosite')
        browser.maximize_window()
        file = open("D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\datasets\infouser.txt", "r") 
        for line in file:
            data=line.split(",")
            browser.find_element_by_link_text("My Account").click()
            browser.find_element_by_link_text("Continue").click()
            browser.find_element_by_name("gender").click()
            browser.find_element_by_name("firstname").send_keys(data[0])
            browser.find_element_by_name("lastname").send_keys("Again")
            browser.find_element_by_id("dob").send_keys("08/01/1987")
            browser.find_element_by_name("email_address").send_keys(data[1])
            browser.find_element_by_name("company").send_keys("5Elements Learning")
            browser.find_element_by_name("street_address").send_keys("First Address")
            browser.find_element_by_name("suburb").send_keys("Second Address")
            browser.find_element_by_name("postcode").send_keys("110001")
            browser.find_element_by_name("city").send_keys("New Delhi")
            browser.find_element_by_name("state").send_keys("Delhi")
            sel=Select(browser.find_element_by_name("country"))
            sel.select_by_visible_text("India")
            browser.find_element_by_name("country")
            browser.find_element_by_name("telephone").send_keys("1234567890")
            browser.find_element_by_name("fax").send_keys("0123456789")
            browser.find_element_by_name("newsletter").click()
            browser.find_element_by_name("password").send_keys(data[2].strip())
            browser.find_element_by_name("confirmation").send_keys(data[2].strip())
            browser.find_element_by_xpath("//span[@class='ui-button-text'][contains(text(),'Continue')]").click()
            print(browser.title)
            print("User created")
            browser.find_element_by_xpath("//span[@class='ui-button-text'][contains(text(),'Continue')]").click()
            print("Logged in successfully")
            print(browser.title)
            browser.find_element_by_link_text("Log Off").click()
            browser.find_element_by_link_text("Continue").click()
            print("Logged Out")
        file.close()
    
    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
import time

browser= webdriver.Chrome(executable_path='D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')

browser.get("http://www.5elementslearning.dev/demosite")#open the chrome with url
browser.find_element_by_link_text("My Account").click()
browser.find_element_by_name("email_address").send_keys("abc@demo.com")
browser.find_element_by_name("password").send_keys("demo@123")
browser.find_element_by_id("tdb5").click()
browser.find_element_by_link_text("Log Off").click()
browser.find_element_by_link_text("Continue").click()
browser.close()


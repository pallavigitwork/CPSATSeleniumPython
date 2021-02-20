from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
driver.maximize_window()
driver.get("http://5elementslearning.dev/demosite")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").clear()
driver.find_element_by_name("email_address").send_keys("abc@demo.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("demo@123")
driver.find_element_by_id("tdb5").click()
driver.find_element_by_link_text("Log Off").click()
driver.find_element_by_link_text("Continue").click()
driver.quit() 

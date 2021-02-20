from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
driver.get("http://5elementslearning.dev/demosite")
print(driver.find_element_by_link_text("My Account").text)
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").clear()
driver.find_element_by_name("email_address").send_keys("abc@demo.com")
print(driver.find_element_by_name("email_address").get_attribute("value"))
print(driver.find_element_by_name("email_address").tag_name)
print(driver.find_element_by_name("email_address").is_displayed())
print(driver.find_element_by_name("email_address").text)


time.sleep(2)
driver.quit() #close the current instance of the browser
#driver.quit - close all instances of the chrome browser associated with the driver object


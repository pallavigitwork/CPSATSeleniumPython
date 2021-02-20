from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
driver.get("http://5elementslearning.dev/demosite")
print(driver.page_source) #print the entire contents of the page
print(driver.current_url)
print(driver.title)
driver.find_element_by_link_text("My Account").click()
time.sleep(2)
driver.quit() #close the current instance of the browser
#driver.quit - close all instances of the chrome browser associated with the driver object


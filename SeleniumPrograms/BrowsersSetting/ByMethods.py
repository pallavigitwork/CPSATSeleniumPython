from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
driver.get("http://5elementslearning.dev/demosite")
driver.find_element_by_link_text("My Account").click()
driver.back()
driver.find_element_by_partial_link_text("Account").click()
print(driver.find_element_by_name("email_address").is_displayed())
print(driver.find_element_by_xpath("//input[@name='password']").is_displayed())
print(driver.find_element_by_css_selector("#tdb5").is_enabled())
driver.find_element_by_name("keywords").send_keys("unreal")
driver.find_element_by_xpath("//input[contains(@title,'Quick Find')]").click()
time.sleep(3)
print(driver.find_element_by_class_name("productListingHeader").is_displayed())
driver.quit() 
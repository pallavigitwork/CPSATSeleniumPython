from selenium import webdriver
from selenium.webdriver.ie.options import Options
import time

ie_options = Options()
ie_options.ignore_protected_mode_settings = True
ie_options.ignore_zoom_level=True
driver=webdriver.Ie(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\IEDriverServer.exe',options=ie_options)
driver.get('http://5elementslearning.dev/demosite')
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").send_keys("abc@demo.com")
str=driver.find_element_by_name("email_address").get_attribute("junk")
time.sleep(5)
driver.close()
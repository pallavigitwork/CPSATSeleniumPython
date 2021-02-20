from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
driver.get("http://5elementslearning.dev/demosite")
print(driver.page_source) #print the entire contents of the page
print(driver.current_url)
print(driver.title)
print ("Headless Chrome Initialized")
driver.quit()
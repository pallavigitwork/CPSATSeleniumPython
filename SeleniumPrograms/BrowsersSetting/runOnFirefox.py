from selenium import webdriver
import time
browser =webdriver.Firefox(executable_path=r'D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\geckodriver.exe')
browser.get('http://5elementslearning.dev/demosite')
time.sleep(5)
browser.quit()



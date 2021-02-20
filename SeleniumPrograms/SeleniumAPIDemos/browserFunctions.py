from selenium import webdriver
import time

browser =webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
browser.get('http://5elementslearning.dev/demosite')
browser.maximize_window()
print(browser.current_url)
print(browser.title)
print(browser.name)
print(browser.get_window_size(windowHandle='current'))
print(browser.page_source)
browser.find_element_by_link_text("My Account").click()
browser.back()
time.sleep(3)
browser.forward()
time.sleep(3)
browser.quit()



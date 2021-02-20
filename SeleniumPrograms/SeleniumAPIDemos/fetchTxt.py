from selenium import webdriver

browser =webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
browser.get('http://5elementslearning.dev/demosite')
browser.find_element_by_link_text("My Account").click()
browser.find_element_by_name("email_address").send_keys("abc@demo.com")
str=browser.find_element_by_name("email_address").get_attribute("junk")
print(str)
str1=browser.find_element_by_name("email_address").text
print(str1)
str2=browser.find_element_by_id("tdb5").text
print(str2)
browser.quit()
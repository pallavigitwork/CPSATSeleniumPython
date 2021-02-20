from selenium import webdriver

browser =webdriver.Chrome(executable_path='D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
browser.implicitly_wait(20)

browser.get('http://5elementslearning.dev/demosite')
browser.find_element_by_link_text("My Account").click()
browser.find_element_by_name("email_address").send_keys("abc@demo.com")
browser.find_element_by_name("password").send_keys("demo@123")
browser.find_element_by_id("tdb5").click()

if(browser.page_source.find("My Account Information")!=-1):
    browser.find_element_by_link_text("Log Off").click()
    browser.find_element_by_link_text("Continue").click()
    print("Valid user credentials")
else:
    print("Invalid user credentials")

browser.close()

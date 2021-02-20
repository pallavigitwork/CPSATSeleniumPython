from selenium import webdriver

browser =webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
browser.get('http://5elementslearning.dev/demosite')
elementsList=[]
elementsList=browser.find_elements_by_xpath("//a") #Fetch all anchor /link elements

#Fetch all the links and print their text and href attribute
for ele in elementsList:
    print(ele.text)
    print(ele.get_attribute("href"))
browser.quit()
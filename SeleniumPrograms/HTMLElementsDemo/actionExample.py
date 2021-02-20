from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time

class actionExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://swisnl.github.io/jQuery-contextMenu/demo/trigger-hover.html"
        
    
    def test_Action(self):
        try: 
            driver = self.driver
            driver.get(self.base_url)
            actions = ActionChains(driver)
            hvrme=driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
            actions.move_to_element(hvrme).perform()
            time.sleep(5)
            optnPast=driver.find_element_by_xpath("/html/body/ul/li[4]")
            actions.move_to_element(optnPast).click(optnPast).perform() #composite action
            time.sleep(5)
            alert=driver.switch_to_alert()
            alert.accept() #press on OK button
            time.sleep(5)
        except Exception as e:
            print(e)
                          
             
    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()

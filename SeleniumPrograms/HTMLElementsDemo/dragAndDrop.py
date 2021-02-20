from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time
from selenium.webdriver.chrome.options import Options

class dragAndDrop(unittest.TestCase):
    def setUp(self):
        options = Options() 
        options.add_argument("--start-maximized") 
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe', chrome_options=options)
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://jqueryui.com/droppable/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Action(self):
        driver = self.driver
        driver.get(self.base_url)
        actions = ActionChains(driver)
        driver.switch_to_frame(driver.find_element_by_class_name("demo-frame"))
        draggable=driver.find_element_by_id("draggable");
        droppable=driver.find_element_by_id("droppable");
        actions.drag_and_drop(draggable, droppable).perform();
        time.sleep(3)
             
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

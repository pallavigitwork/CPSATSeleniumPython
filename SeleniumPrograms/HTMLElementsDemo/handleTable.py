# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TableExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Eclipse\workspace\SeleniumWithPython\SeleniumWithPython\drivers\chromedriver.exe')
        self.driver.implicitly_wait(30) #Introducing Implict Wait
        self.base_url = "http://5elementslearning.dev/"
        self.verificationErrors = []
        self.accept_next_alert = True
        rows=[]
        cols=[]
    
    def test_table(self):
        driver = self.driver
        driver.get(self.base_url + "/demosite/")
        prodTable=driver.find_element_by_tag_name("table")
        #Fetch rows
        rowsList=prodTable.find_elements_by_xpath("//*/tbody/tr") #returns a list of table rows
        i=1
        for row in rowsList: #outer for loop is for rows
            #Fetch cols for each row
            colsList=row.find_elements_by_xpath("td") #returns a list of cols
            #print(len(cols))
            j=1
            for col in colsList: #inner for loop is for columns
                print("row: ",i, "col: ", j, "-", col.text)
                j=j+1
            i=i+1
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

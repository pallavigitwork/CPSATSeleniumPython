import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoAllure(unittest.TestCase):
    def test_site_loads(self):
        driver =webdriver.Chrome(executable_path='D:\WORK\AGILE TEST ALLIANCE\CPSAT-PYTHON\ECLIPSE\PythonCPSATProject\drivers\chromedriver.exe')
        driver.get("http://5elementslearning.dev/demosite")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))


if __name__ == '__main__':
    unittest.main()
import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Pages.testindex import testindex

class UniversityManagementSystemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://127.0.0.1:5000/")
        cls.driver.maximize_window()
        
    def test_indexpage(self):
        driver = self.driver
        test_1 = testindex(driver)
        test_1.clickAccessStudentPortal()
        time.sleep(10)
        
        
        
    
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()
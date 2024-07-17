import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unit_test_admin_login_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://127.0.0.1:5000/admin")
        cls.driver.maximize_window()
        
    def test_admin_login_positive(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin_1")
        driver.find_element(By.ID, "password").send_keys("admin_1")
        driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/input").click()
        time.sleep(2)
        
    def test_admin_login_negative_test(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin_1")
        driver.find_element(By.ID, "password").send_keys()
        driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/input").click()
        assert "Wrong Username or Password" in driver.page_source
        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
  
if __name__=="__main__":
    unittest.main()
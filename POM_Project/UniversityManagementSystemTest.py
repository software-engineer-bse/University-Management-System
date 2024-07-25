import time
import unittest
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Pages.testindex import testindex
from Pages.test_admin_login import test_admin_login

class UniversityManagementSystemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        
    def test_indexpage_student_admin_portal_button(self):
        driver = self.driver
        test_index_page = testindex(driver)
        test_index_page.open_page("http://127.0.0.1:5000/")
        test_index_page.clickAccessStudentPortal()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        test_index_page.clickAccessAdminPortal()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        
        
    def test_admin_login_page(self):
        driver = self.driver
        test_admin_login_1 = test_admin_login(driver)
        test_admin_login_1.open_page("http://127.0.0.1:5000/admin")
        test_admin_login_1.enter_user_name("admin_1")
        test_admin_login_1.enter_password("admin_1")
        time.sleep(2)
        test_admin_login_1.click_login_button()
        time.sleep(2)
        
        
    
        
        
        
    
        
        
    
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()
from selenium.webdriver.common.by import By
class testindex:
    def __init__(self, driver):
        self.driver = driver
        self.accessStudentPortal_XPATH = "/html/body/div/div/div/div/div/div[2]/div/div/a"
        self.accessAdminPortal_XPATH = "/html/body/div/div/div/div/div/div[3]/div/div/a"
        
        
    def clickAccessStudentPortal(self):
        self.driver.find_element(By.XPATH,self.accessStudentPortal_XPATH).click()
        
    def clickAccessAdminPortal(self):
        self.driver.find_element(By.XPATH,self.accessAdminPortal_XPATH).click()
        
    
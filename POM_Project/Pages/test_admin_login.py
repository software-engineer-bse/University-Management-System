from selenium.webdriver.common.by import By
class test_admin_login:
    def __init__(self, driver):
        self.driver = driver
        self.username_id = "username"
        self.password_id = "password"
        self.button_XPATH = "/html/body/div/div/div/div/form/input"
        
    def open_page(self, link):
        self.driver.get(link)
        self.driver.maximize_window()
        
    def enter_user_name(self, username):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.button_XPATH).click()
        
        
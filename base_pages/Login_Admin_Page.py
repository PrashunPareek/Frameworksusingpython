from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    logout_Xpath = "//*[@id='navbarText']/ul/li[3]/a"
    btn_login_xpath = "//*[@type = 'submit']"
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.btn_login_xpath))).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_Xpath).click()

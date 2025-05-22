import time
from utilities.custom_logger import log_maker
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilities.read_properties import Read_Config
class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = log_maker.log_gen()
    def test_title_verification(self, setup):
        self.logger.info("*************************Test_01_Admin_Login**************************")
        self.logger.info("***********************************Verificaiton of Admin login page Title***********************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("E:\\Important stuff\\Frameworksusingpython\\screenshots\\test_verification_title.png")
            self.driver.close()
            assert False
    def test_valid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_test = self.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/nav/ul/li[1]/a/p").text
        if act_dashboard_test == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("E:\\Important stuff\\Frameworksusingpython\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False
    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("E:\\Important stuff\\Frameworksusingpython\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False

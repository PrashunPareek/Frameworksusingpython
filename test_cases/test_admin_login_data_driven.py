import time
from utilities.custom_logger import log_maker
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilities.read_properties import Read_Config
from utilities import excel_utils
class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()
    path = "E:\\Important stuff\\Frameworksusingpython\\test_data\\admin_login_data.xlsx"
    logger = log_maker.log_gen()
    status_list = []
    def test_valid_admin_login_data_driven(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        self.cols = excel_utils.get_col_count(self.path,"Sheet1")
        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path,"Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            time.sleep(2)
            self.admin_lp.click_login()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("Test data is Failed")
                    self.status_list.append("Fail")
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is Failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")
        print("Status List is : ", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is Failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is Passed")
            assert True


import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from undetected_geckodriver.utils import generate_random_string
from test_cases.conftest import setup
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import log_maker
from base_pages.Add_customer_page import add_customer_page

class Test_03_add_new_user:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = log_maker.log_gen()
    def test_add_new_customer(self,setup):
        self.logger.info("*******************Test_03_add_new_user Started**************************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*************Login Completed****************")
        self.logger.info("*****************Starting Add Customer Test************************")
        self.add_customer = add_customer_page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_option()
        self.add_customer.click_addnew()
        self.logger.info("**************Providing Customer info started ************************")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Jack")
        self.add_customer.enter_lastname("Shaw")
        self.add_customer.select_gender("Male")
        self.add_customer.company_name("Mycompany")
        self.add_customer.click_IsTaxExempt()
        self.add_customer.select_newsletter()
        self.logger.info("******************Test Store 2 Selected**********************")
        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Test admin comment")
        self.add_customer.click_save()

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com','example.com'])
    return f"{username}@{domain}"
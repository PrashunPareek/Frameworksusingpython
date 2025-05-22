import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class add_customer_page:
    link_customers_menu_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/a/p"
    link_customer_menuoption_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/p"
    link_addnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    text_email_id = "Email"
    text_password_id = "Password"
    text_fname_id = "FirstName"
    text_lname_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_dob_id = "DateofBirth"
    text_companyname_id = "Company"
    chbx_tax_exempt_id = "IsTaxExempt"
    newsletter_cusrole_list_xpath = "//*[@id='customer-info']/div[2]/div[8]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    newsletter_cusrole_click_list_xpath = "//*[@id='select2-SelectedNewsletterSubscriptionStoreIds-result-6jpw-1']"
    cusroles_field_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul"
    cusrole_guests_xpath = "//li[contains(text(),'Guests')]"
    cusrole_administratior_xpath = "//li[contains(text(),'Administrators')]"
    cusrole_forummoderators_xpath = "//li[conatains(text(),'Forum Moderators')]"
    cusrole_redigstered_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]/span"
    cusrole_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdwn_mngrofvendro_id = "VendorId"
    text_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver
    def click_customers(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath).click()
    def click_customers_from_menu_option(self):
        self.driver.find_element(By.XPATH,self.link_customer_menuoption_xpath).click()
    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.link_addnew_xpath).click()
    def enter_email(self, email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)
    def enter_password(self,password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)
    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID,self.text_fname_id).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID,self.text_lname_id).send_keys(lastname)
    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdo_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()

    def company_name(self, company_name):
        self.driver.find_element(By.ID,self.text_companyname_id).send_keys(company_name)
    def click_IsTaxExempt(self):
        self.driver.find_element(By.ID,self.chbx_tax_exempt_id).click()
    def select_newsletter(self):
        self.driver.find_element(By.XPATH,self.newsletter_cusrole_list_xpath).send_keys("nopCommerce admin demo store"+ Keys.ENTER)
    def select_customer_role(self, role):
        cusrole_field = self.driver.find_element(By.XPATH,self.cusroles_field_xpath)
        cusrole_field.click()
        time.sleep(3)
        if role == 'Guests':
            self.driver.find_element(By.XPATH,self.cusrole_redigstered_xpath).click()
            cusrole_field.click()
            self.driver.find_element(By.XPATH,"//li[contains(text(), 'Guests')]").click()
        elif role == "Administrators":
            cusrole_field.send_keys("Administrators"+Keys.ENTER)
        elif role == "Forum Moderators":
            cusrole_field.send_keys("Forum Moderators"+ Keys.ENTER)
        elif role == "Registered":
            pass
        elif role == "Vendors":
            cusrole_field.send_keys("Vendors"+Keys.ENTER)
        else:
            cusrole_field.send_keys("Administrators" + Keys.ENTER)
    def select_manager_of_vendor(self,value):
        drp_dwn = Select(self.driver.find_element(By.ID, self.drpdwn_mngrofvendro_id))
        drp_dwn.select_by_visible_text(value)
    def enter_admin_comments(self, admincomments):
        self.driver.find_element(By.ID, self.text_admincomment_id).send_keys(admincomments)
    def click_save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()


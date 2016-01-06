from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from BaseObjects.basePage import BasePage
from BaseObjects.locators import RegistrationLocator


class RegisterationPage(BasePage):
    """ this class represent create new account page elements manipulations and functions"""
    # Locators
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID,'lastname')
    EMAIL = (By.ID,'email_address')
    PASSWORD = (By.ID,'password')
    CONFIRM_PASS = (By.ID,'confirmation')
    SUBMIT_BTN = (By.CLASS_NAME,'button')

    def __init__(self, driver):
        super(RegisterationPage, self).__init__(driver)

    def register_new_account(self, fname, lname, email, password, confirm_pass):
        self.driver.find_element(*RegisterationPage.FIRST_NAME).send_keys(fname)
        self.driver.find_element(*RegisterationPage.LAST_NAME).send_keys(lname)
        self.driver.find_element(*RegisterationPage.EMAIL).send_keys(email)
        self.driver.find_element(*RegisterationPage.PASSWORD).send_keys(password)
        self.driver.find_element(*RegisterationPage.CONFIRM_PASS).send_keys(confirm_pass)
        self.driver.find_element(*RegisterationPage.SUBMIT_BTN).click()
        self.driver.find_element(*RegisterationPage.CONFIRM_PASS).send_keys(Keys.RETURN)


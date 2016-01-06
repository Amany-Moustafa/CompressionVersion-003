from BaseObjects.basePage import BasePage
from BaseObjects.locators import LoginPageLocator
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """ this class represent login page elements manipulations and functions"""

    # Locators
    USERNAME = (By.ID, 'email')
    PASSWORD = (By.ID, 'pass')
    LOGIN_BTN = (By.ID, 'send2')
    Error_LBL = (By.CLASS_NAME, 'error-msg')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def login_with_Invalid_credentials(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()
        error_LBL = self.driver.find_element(*LoginPage.Error_LBL)
        self.assertTrue(error_LBL.is_displayed())

    def login_with_valid_credentials(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BTN).click()



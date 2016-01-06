from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseObjects.basePage import BasePage
from BaseObjects.basePage import InvalidPageException
from BaseObjects.locators import EditAccountLocator


class AccountEditPage(BasePage):
    """ this class represent Edit account page elements manipulations and functions"""
    # Locators
    LOGIN_SUCESS_MSG_LBL = (By.CSS_SELECTOR, 'li.success-msg > ul > li > span')
    LOGIN_NAME_LBL = (By.CLASS_NAME, 'welcome-msg')
    MYACCOUNT_LNK = (By.LINK_TEXT, 'My Account')
    LOGOUT_LNK = (By.XPATH, '/html/body/header/div[1]/div/div/div[2]/div/div[2]/div/ul[2]/li/ul/li[4]/a')

    def __init__(self, driver):
        super(AccountEditPage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name("main")
        except:
                raise InvalidPageException("Home Page not loaded")

    def get_registration_success_message(self):
        return self.driver.find_element(*AccountEditPage.LOGIN_SUCESS_MSG_LBL).text

    def get_login_Name(self):
        # WebDriverWait(self.driver, 10).until(EC._element_if_visible(*EditAccountLocator.LOGIN_NAME_LBL),True)
        # self.driver.implicitly_wait(10)
        return self.driver.find_element(*AccountEditPage.LOGIN_NAME_LBL).text

    def logout(self):
        my_account = self.driver.find_element(*AccountEditPage.MYACCOUNT_LNK)
        hover = ActionChains(self.driver).move_to_element(my_account)
        hover.perform()
        # self.driver.implicitly_wait(15)
        # use explicit wait for 10 sec till logout link
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div[1]/div/div/div[2]/div/div[2]/div/ul[2]/li/ul/li[4]/a')))
        element.click()

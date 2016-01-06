from selenium.webdriver.common.by import By
from BaseObjects.basePage import BasePage
from BaseObjects.locators import MainPageLocator
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    """ this class represent Main page elements manipulations and functions"""
    # Locators
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, 'Create an Account')
    LOGIN_LINK = (By.LINK_TEXT, 'Sign In')
    slider_img_container = (By.CSS_SELECTOR, \
                            'div.responsivebanner.revslider-initialised.tp-simpleresponsive > ul')
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def get_page_title(self):
        """function to return page title"""
        return self.driver.title

    def open_create_account(self):
        """function to open link of crete new account"""
        self.driver.find_element(*MainPage.CREATE_ACCOUNT_LINK).click()

    def open_login(self):
        """function to open link of login"""
        self.driver.find_element(*MainPage.LOGIN_LINK).click()

    def menu_navigation(self):

        pass


    def check_exists_by_class_name(self,classname):
        try:
            self.driver.find_element_by_class_name(classname)
        except NoSuchElementException:
            return False
        return True

    def get_slider_image_container(self):
        return self.driver.find_element(*MainPage.slider_img_container)
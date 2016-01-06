from BaseObjects.basePage import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    #Locators
    Continue_Shopping_BTN = (By.CSS_SELECTOR, 'button.button.btn-continue')
    Update_Shopping_Cart_BTN = (By.LINK_TEXT, 'Update Shopping Cart')
    Clear_Shopping_Cart_BTN = (By.LINK_TEXT, 'Clear Shopping Cart')
    success_message = (By.CSS_SELECTOR, 'li.success-msg > ul > li > span')
    Checkout_BTN = (By.CSS_SELECTOR, 'button.button.btn-proceed-checkout.btn-checkout')

    def __int__(self, driver):
        super(CartPage, self).__init__(driver)

    def click_continue_shopping(self):
        self.driver.find_element(*CartPage.Continue_Shopping_BTN).click()

    def get_sucess_message(self):
        return self.driver.find_element(*CartPage.success_message).text

    def click_checkout_button(self):
        self.driver.find_element(*CartPage.Checkout_BTN).click()
from selenium.webdriver.support.select import Select

from BaseObjects.basePage import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPopUP(BasePage):
    #Locators
    COLOR_DDL = (By.ID, 'attribute911')
    Size_DDL = (By.ID, 'attribute2261')
    QUANTITY_TXT = (By.ID, 'qty')
    ADD_TO_CART_BTN = (By.XPATH, "//*[@id='product_addtocart_form']/div[3]/div[5]/div[1]/button")
        #(By.XPATH, '//*[@id="product_addtocart_form"]/button')


    def __int__(self, driver):
        super(ProductDetailsPopUP, self).__init__(driver)

    def set_color_value(self):
       color_options = Select(self.driver.find_element(*ProductDetailsPopUP.COLOR_DDL))
       color_options.select_by_index(1)

    def set_size_value(self):
        size_options = Select(self.driver.find_element(*ProductDetailsPopUP.Size_DDL))
        size_options.select_by_index(2)

    def set_quantity_value(self):
        self.driver.find_element(*ProductDetailsPopUP.QUANTITY_TXT).clear()
        self.driver.find_element(*ProductDetailsPopUP.QUANTITY_TXT).send_keys('2')

    def click_add_to_cart_btn(self):
        self.driver.find_element(*ProductDetailsPopUP.ADD_TO_CART_BTN).click()


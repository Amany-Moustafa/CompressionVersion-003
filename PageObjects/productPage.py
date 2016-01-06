from selenium.webdriver.common.by import By
from BaseObjects.basePage import BasePage
from BaseObjects.locators import ProductPageLocator


class ProductPage(BasePage):

    # Locators
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'div.addtocart.br > button > span > span')
    ADD_TO_CART_LIST_BTN = (By.CSS_SELECTOR, 'button.button.btn-cart')
    WISH_LIST_BTN = (By.CSS_SELECTOR, 'div.confix-produclist-category > ul > li:nth-child(1) > a')
    PRODUCT_DETAILS_LNK = (By.CSS_SELECTOR, 'div.col-xs-12.col-sm-3.col-md-3.col-lg-4.item.first.hover-effect > h3')
    MY_CART_LNK = (By.CSS_SELECTOR, 'div.top-link ul.links li.last a')
    TOTAL_ITEMS_LBL = (By.CLASS_NAME, 'amount')
    EMPTY_CART_CONTENT = (By.XPATH, "//*[@class = 'ajaxcart']/div[2]/p")
    CART_LBL = (By.CLASS_NAME, 'mt-cart-label')
    OPTIONAL_BTN = (By.CSS_SELECTOR, '.button.btn-cart.show-options')
    NOT_OPTIONAL_BTN = (By.CSS_SELECTOR, 'div.addtocart.br > button:not(.show-options)')
                        #'.category-products:not(.show-options)')

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def get_mycart_value(self):
        return self.driver.find_element(*ProductPage.MY_CART_LNK).text

    def open_product_details_page(self):
        self.driver.find_element(*ProductPage.PRODUCT_DETAILS_LNK).click()

    def get_page_title(self):
        """function to return page title"""
        return self.driver.title

    def get_total_item_lable_text(self):
        lbl_txt = self.driver.find_element(*ProductPage.TOTAL_ITEMS_LBL).text
        return lbl_txt

    def click_add_to_cart(self):
        self.driver.find_element(*ProductPage.ADD_TO_CART_BTN).click()

    def get_cart_count_label_value(self):
        cart_value = self.driver.find_element(*ProductPage.CART_LBL).text
        return cart_value

    def get_cart_content(self):
        cart_content = self.driver.find_element(*ProductPage.CART_CONTENT)
        return cart_content

    def validate_product_page_images(self):
        # function to validate all page product images has been loaded
        # self.driver.get('http://www.compressionwellness.com/brand/core-spun.html')
        container = self.driver.find_element_by_class_name('products-grid')
        image_file = container.find_elements_by_xpath("//*[@class = 'product-image']/img")
        for i in (image_file):
            img_src = i.get_attribute('src')
            image_present = self.driver.execute_script("return arguments[0].complete &&"
                                                      " typeof arguments[0].naturalWidth != \"undefined\" &&"
                                                      " arguments[0].naturalWidth > 0", i)
        if not image_present:
            return False
        else:
            return True

    def get_all_AddToCart_btns(self):
        return self.driver.find_elements(*ProductPage.ADD_TO_CART_LIST_BTN)

    def get_option_btn(self):
        return self.driver.find_elements(*ProductPage.OPTIONAL_BTN)

    def get_not_optional_btn(self):
        return self.driver.find_elements(*ProductPage.NOT_OPTIONAL_BTN)








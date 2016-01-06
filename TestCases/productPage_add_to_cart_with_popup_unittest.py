import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseObjects.basetestcase import BaseTestCase
from PageObjects.menuObject import MenuObject
from PageObjects.productPage import ProductPage
from PageObjects.productCartDetailesPopUp import ProductDetailsPopUP
from PageObjects.cartPage import CartPage


class TestProductPage(BaseTestCase):
    def test_add_to_cart(self):
        # 1- Open product page and assert page is opened
        MenuObject.click_list_of_brands(self,'CEP')
        self.assertIn('Items', ProductPage.get_total_item_lable_text(self))
        # 2- check all page images loaded successfully
        ProductPage.validate_product_page_images(self)
        # 3- Get value of cart label
        old_cart_value = ProductPage.get_cart_count_label_value(self)
        old_int_value = int(old_cart_value[7])# get the 8th char
        # get list of all add to cart buttons
        add_to_cart_with_option_popup = ProductPage.get_option_btn(self)

        for x in add_to_cart_with_option_popup:
            x.click()
            #wait till popup displayed
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//form[@id='product_addtocart_form']/..")))#get parent element of the form tag
            #insert form data
            ProductDetailsPopUP.set_color_value(self)
            ProductDetailsPopUP.set_size_value(self)
            ProductDetailsPopUP.set_quantity_value(self)
            ProductDetailsPopUP.click_add_to_cart_btn(self)
            self.assertIn('was added to your shopping cart',CartPage.get_sucess_message(self))
            #CartPage.click_checkout_button(self)
            break
            #MenuObject.click_list_of_brands(self,'CEP')
            #CartPage.click_continue_shopping(self)

        # 5- Check cart value incremented by 1
        new_cart_value = ProductPage.get_cart_count_label_value(self)
        new_int_value = int(new_cart_value[7])
        expected_cart_value = old_int_value +2 # incremented by value added in the quantity field
        self.assertEqual(new_int_value,expected_cart_value)


if __name__ == '__main__':
    unittest.main()

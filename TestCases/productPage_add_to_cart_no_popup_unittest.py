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

    def test_add_to_cart_no_popup(self):
        # 1- Open product page and assert page is opened
        MenuObject.click_list_of_brands(self,'CEP')
        self.assertIn('Items', ProductPage.get_total_item_lable_text(self))

        # 2- check all page images loaded successfully
        ProductPage.validate_product_page_images(self)
       # add_to_cart_without_option_popup = ProductPage.get_not_optional_btn(self)

        # 3- Get value of cart label
        old_cart_value = ProductPage.get_cart_count_label_value(self)
        old_int_value = int(old_cart_value[7])# get the 8th char

        # 4- Click add to cart
        ProductPage.click_add_to_cart(self)
        # 5- wait till ifram appeared to ensure new cart value
        alert = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located((By.CLASS_NAME,'message-alert')))
        # get text from alert
        alert_text = alert.text

        # assert alert text
        self.assertIn('was added to your shopping cart',alert_text)

        # 5- Check cart value incremented by 1
        new_cart_value = ProductPage.get_cart_count_label_value(self)
        new_int_value = int(new_cart_value[7])
        expected_cart_value = old_int_value +1

        self.assertEqual(new_int_value,expected_cart_value)



if __name__ == '__main__':
    unittest.main()

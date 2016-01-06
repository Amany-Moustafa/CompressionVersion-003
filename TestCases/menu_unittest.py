import unittest
from DataSource.ExcelLib import ReadExcel
from BaseObjects.basetestcase import BaseTestCase
from ddt import ddt, data, unpack
from PageObjects.productPage import ProductPage
from PageObjects.menuObject import MenuObject
from BaseObjects.locators import ProductPageLocator
from PageObjects.mainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@ddt
class TestProductPages(BaseTestCase):

    @data(*ReadExcel.get_data('../TestData/Data.xlsx', 'BrandMenu'))
    @unpack
    def test_menu(self, MenuListItems):
        ProductPage_Obj = ProductPage
        Menu_obj =  MenuObject
        Menu_obj.click_list_of_brands(self, MenuListItems)
        WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located(By.CLASS_NAME,'category-products'))

        self.assertIn('item', ProductPage.get_total_item_lable_text(self))

        #bodyelm = 'catalog-category-view categorypath-mediven category-mediven'
        #MainPage.check_exists_by_class_name(self,bodyelm)
        #self.assertEqual(MenuListItems,ProductPage_Obj.get_page_title(self))



if __name__ == '__main__':
    unittest.main()

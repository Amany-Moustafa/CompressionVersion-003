import unittest
from DataSource.ExcelLib import ReadExcel
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

from BaseObjects.basetestcase import BaseTestCase
from PageObjects.accountEditPage import AccountEditPage
from PageObjects.loginPage import LoginPage
from PageObjects.mainPage import MainPage
from PageObjects.productPage import ProductPage

@ddt
class TestLogin(BaseTestCase):
    """ this class for Test login page """

    @data(*ReadExcel.get_data('../TestData/Data.xlsx', 'LoginCredentials'))
    @unpack
    def testLogin(self,Username,Password,LoginName):
       # declare page objects will be used by class
        Main_Obj = MainPage
        Login_Obj = LoginPage
        EditAccount_obj = AccountEditPage
        ProductPage_Obj = ProductPage
        Main_Obj.open_login(self)
        self.assertIn("Customer Login" , Main_Obj.get_page_title(self))

        if Username == 'aabdelfattah@integrant.com':
                Login_Obj.login_with_valid_credentials(self,Username,Password)
                try:
                    self.assertIn(LoginName,EditAccount_obj.get_login_Name(self))
                    BaseTestCase.take_screen_shoot(self)
                    EditAccount_obj.logout(self)
                except NoSuchElementException:
                    BaseTestCase.take_screen_shoot(self)
                    raise
        else:
                Login_Obj.login_with_Invalid_credentials(self,Username,Password)


if __name__ == '__main__':
    unittest.main()
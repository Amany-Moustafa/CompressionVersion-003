import unittest
from ddt import ddt, data, unpack
from PageObjects.checkOutPage import checkOutPage
from PageObjects.loginPage import LoginPage
from PageObjects.mainPage import MainPage
from DataSource.ExcelLib import ReadExcel
from BaseObjects.basetestcase import BaseTestCase
from DataSource.readxml import read_xml

@ddt
class checkout(BaseTestCase):

    @data(*ReadExcel.get_data('../TestData/Checkout_Data.xlsx', 'Checkout'))
    @unpack
    def test_checkout(self,firstname,lastname,company,streetaddress1,streetaddress2,city,state,postalcode,country,telephone,fax):
        #get paymentinfo from XML
        creditCardType = str(read_xml.read_tag_text_from_xml('../TestData/checkout_data.xml','PaymentInformation','creditCardType'))
        CreditCardNumber = str(read_xml.read_tag_text_from_xml('../TestData/checkout_data.xml','PaymentInformation','CreditCardNumber'))
        ExpirationDate = str(read_xml.read_tag_text_from_xml('../TestData/checkout_data.xml','PaymentInformation','ExpirationDate'))
        ExpirationYear = str(read_xml.read_tag_text_from_xml('../TestData/checkout_data.xml','PaymentInformation','ExpirationYear'))

        # declare page objects will be used by class
        chkout_Obj = checkOutPage
        loginpage_Obj = LoginPage
        mainpage_Obj = MainPage
        mainpage_Obj.open_login(self)
        loginpage_Obj.login_with_valid_credentials(self,"rami.shedid@gmail.com","123456")
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.compressionwellness.com/checkout/onepage/')
        #self.driver.get('http://www.compressionwellness.com/checkout/cart/')
        chkout_Obj.set_Billing_Information(self,firstname,lastname,company,streetaddress1,streetaddress2,city,state,postalcode,country,telephone,fax)
        chkout_Obj.set_Shipping_Information(self)
        chkout_Obj.set_Payment_Information_As_Credit_Card(self,creditCardType,CreditCardNumber,ExpirationDate,ExpirationYear)
        #chkout_Obj.read_Products(self)
        chkout_Obj.read_taxes(self)

if __name__ == '__main__':
    unittest.main()

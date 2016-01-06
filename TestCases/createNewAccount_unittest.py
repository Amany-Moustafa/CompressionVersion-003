import unittest
from ddt import ddt, data, unpack
from BaseObjects.basetestcase import BaseTestCase
from DataSource.RandomGen import RandomGen
from PageObjects.accountEditPage import AccountEditPage
from PageObjects.createNewAccountPage import RegisterationPage
from PageObjects.mainPage import MainPage
from DataSource.ExcelLib import ReadExcel


@ddt
class TestCreateNewAccount(BaseTestCase):
    """This class for test create new account page"""

    @data(*ReadExcel.get_data('../TestData/Data.xlsx', 'RandomData'))
    @unpack
    def test_CreateNewAccount(self, Fname, Lname, Email, PasswordChar):
        # declare page objects will be used by class
        Main_Obj = MainPage
        Register_Obj = RegisterationPage
        acountEdit_obj = AccountEditPage

        self.assertIn('Compression Wellness', Main_Obj.get_page_title(self))
        Main_Obj.open_create_account(self)
        self.assertEqual("Create New Customer Account", Main_Obj.get_page_title(self))
        _FirstName = RandomGen.Random_char(int(Fname))
        _LastName = RandomGen.Random_char(int(Lname))
        _Email = RandomGen.Random_Email(int(Email))
        _Password = RandomGen.Random_char(int(PasswordChar))
        _Confirmpass = _Password
        Register_Obj.register_new_account(self, _FirstName, _LastName, _Email, _Password, _Confirmpass)
        # assert edit account page title
        self.assertEqual('Account Information',Main_Obj.get_page_title(self))
        # assert registeration successfull message appeared
        self.assertEqual('Thank you for registering with compressionwellness.com.',
                         acountEdit_obj.get_registration_success_message(self))


if __name__ == '__main__':
    unittest.main()

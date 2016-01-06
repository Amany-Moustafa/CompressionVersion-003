import unittest
import sys
from TestCases.login_unittest import TestLogin
from TestCases.createNewAccount_unittest import TestCreateNewAccount
from BaseObjects.basetestcase import BaseTestCase
from TestCases.MainPage_unittest import MainPageTest

class TestSuite(BaseTestCase):

     def test_main(self):
        # suite of TestCases
        #
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin.testLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateNewAccount.test_CreateNewAccount),
            unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTest.test_checklogo_displayed(self))

            ])
        runner = unittest.TextTestRunner()
        runner.run (self.suite)

if __name__ == '__main__':
    unittest.main()

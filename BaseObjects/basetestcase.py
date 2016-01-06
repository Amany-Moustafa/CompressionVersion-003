import unittest
from selenium import webdriver
from datetime import datetime
from DataSource.readxml import read_xml


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        #get app url
        url = read_xml.read_tag_attribute_from_xml('../Datasource/configuration.xml','url')
        # navigate to the application home page
        self.driver.get(url)

    """
    def setUp(self):
        '''Running a test on the Selenium standalone server '''
        desired_caps = {}
        desired_caps['platform'] = 'WINDOWS'
        desired_caps['browserName'] = 'firefox'
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.CHROME)
        self.driver.get('https://www.compressionwellness.com/')
        self.driver.maximize_window()
    """

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def take_screen_shoot(self):
        st = (datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
        file_name = self.driver.title[:11] + st + ".png"
        self.driver.save_screenshot('../ScreenShoots/' + file_name)






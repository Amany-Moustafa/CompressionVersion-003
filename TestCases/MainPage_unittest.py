import unittest
from BaseObjects.basetestcase import BaseTestCase
from PageObjects.mainPage import MainPage


class MainPageTest(BaseTestCase):


    def test_check_slider_images(self):
        container = MainPage.get_slider_image_container(self)
        slider_images = container.find_elements_by_css_selector(' li > div.slotholder > img')
        for i in slider_images:
            image_present = self.driver.execute_script("return arguments[0].complete &&"
                                                      " typeof arguments[0].naturalWidth != \"undefined\" &&"
                                                      " arguments[0].naturalWidth > 0", i)
        if not image_present:
            return False
        else:
            return True

    def test_checklogo_displayed(self):
        pass




if __name__ == '__main__':
    unittest.main()

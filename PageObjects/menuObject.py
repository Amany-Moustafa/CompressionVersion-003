
from selenium.webdriver import ActionChains
from BaseObjects.basePage import BasePage
from selenium.webdriver.common.by import By


class MenuObject(BasePage):

    # Locators
    MENU = (By.CLASS_NAME, 'megamenu')
    BRAND_LNK = (By.LINK_TEXT, 'BRAND')
    BRAND_MENU_LIST = (By.CSS_SELECTOR, '#mtnav > li.level0.nav-1.level-top.first.parent > div > div > div > ul.level0')
    STYLE_LNK = (By.LINK_TEXT, 'Style')
    STYLE_MENU_LIST = (By.CSS_SELECTOR, '#mtnav > li.level0.nav-2.level-top.parent > div > div > div.mtmenu-block.mtmenu-block-center.menu-items.grid12-6.itemgrid.itemgrid-2col > ul.level0')
    WOMEN_LNK = (By.LINK_TEXT,'women')
    WOMEN_MENU_LIST = (By.CSS_SELECTOR, '#mtnav > li.level0.nav-2.level-top.parent > div > div > div.mtmenu-block.mtmenu-block-center.menu-items.grid12-6.itemgrid.itemgrid-2col > ul')
    MEN_LNK = (By.LINK_TEXT, 'Men')
    MEN_MENU_LIST = (By.CSS_SELECTOR, '#mtnav > li.level0.nav-4.active.level-top.last.parent > div > div > div > ul.level0')
    HELP_LNK = (By.LINK_TEXT,'help')
    HELP_MENU_lIST = (By.CSS_SELECTOR, '#mtnav > li.level0.level-top.parent.custom-block > div > div > ul.level0')

    def __init__(self, driver):
        super(MenuObject, self).__init__(driver)

    def click_list_of_brands(self, click_here):
        _brand = self.driver.find_element(*MenuObject.BRAND_LNK)
        hover = ActionChains(self.driver).move_to_element(_brand)
        hover.perform()

        _brand_list = self.driver.find_element(*MenuObject.BRAND_MENU_LIST)
        _brand_items = _brand_list.find_elements_by_xpath('//*[@id="mtnav"]/li[1]/div/div/div/ul/li[2]/a/span')


        for item in _brand_items:

            if str(item.text) == str(click_here):
                item_click = ActionChains(self.driver).move_to_element(item)
                item_click.click().perform()
                #item_click.click_and_hold().perform()



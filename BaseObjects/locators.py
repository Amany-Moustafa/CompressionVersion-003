from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    """Class for login page locators, all page locators should come here"""
    USERNAME = (By.ID, 'email')
    PASSWORD = (By.ID, 'pass')
    LOGIN_BTN = (By.ID, 'send2')


class MainPageLocator(object):
    """ Class for Main page locators, all page locators should come here"""
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, 'Create an Account')
    LOGIN_LINK = (By.LINK_TEXT, 'Sign In')


class MenuLocator(object):
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


class RegistrationLocator(object):
    """ Class for create new account page locators, all page locators should come here"""
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID,'lastname')
    EMAIL = (By.ID,'email_address')
    PASSWORD = (By.ID,'password')
    CONFIRM_PASS = (By.ID,'confirmation')
    SUBMIT_BTN = (By.CLASS_NAME,'button')


class EditAccountLocator(object):
    """ Class for edit account page locators, all page locators should come here"""
    LOGIN_SUCESS_MSG_LBL = (By.CSS_SELECTOR, 'li.success-msg > ul > li > span')
    LOGIN_NAME_LBL = (By.CLASS_NAME, 'welcome-msg')
    MYACCOUNT_LNK = (By.LINK_TEXT, 'My Account')
    LOGOUT_LNK = (By.XPATH, '/html/body/header/div[1]/div/div/div[2]/div/div[2]/div/ul[2]/li/ul/li[4]/a')
    # (By.CSS_SELECTOR, 'ul.my-account-links > li.last > a')

class ProductPageLocator(object):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'div.addtocart.br > button > span > span')
    WISH_LIST_BTN = (By.CSS_SELECTOR, 'div.confix-produclist-category > ul > li:nth-child(1) > a')
    PRODUCT_DETAILS_LNK = (By.CSS_SELECTOR, 'div.col-xs-12.col-sm-3.col-md-3.col-lg-4.item.first.hover-effect > h3')
    MY_CART_LNK = (By.CSS_SELECTOR, 'div.top-link ul.links li.last a')
    AMOUNT_LBL = (By.CLASS_NAME, 'amount')
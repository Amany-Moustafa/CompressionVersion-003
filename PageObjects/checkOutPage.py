from selenium.webdriver.common.by import By
from BaseObjects.basePage import BasePage
from BaseObjects.locators import ProductPageLocator
from selenium.webdriver.support.select import Select
from builtins import int
from decimal import Decimal
class checkOutPage(BasePage):

    # Locators_Billing_Information
    FIRST_NAME = (By.ID,"billing:firstname")
    LAST_NAME = (By.ID,"billing:lastname")
    COMPANY = (By.ID,"billing:company")
    STREET_ADDRESS1 = (By.ID,"billing:street1")
    STREET_ADDRESS2 = (By.ID,"billing:street2")
    CITY = (By.ID,"billing:city")
    STATE_PROVINCE_LIST = (By.ID,'billing:region_id')
    POSTAL_CODE = (By.ID,'billing:postcode')
    COUNTRY_LIST = (By.ID,'billing:country_id')
    TELEPHONE = (By.ID,'billing:telephone')
    FAX = (By.ID,'billing:fax')
    CONTINUE_BTN = (By.ID,'billingbtn')

    # Locators_Shipping_Information
    CONTINUE_Shipping_BTN = (By.XPATH,"//*[@id='shipping-method-buttons-container']/button")

    # Locators_Payment_Information_AS_Credit_Card
    CREDIT_CARD_RADIO_BTN = (By.ID,"p_method_sfc_cybersource")
    CONTINUE_PAYMENT_BTN = (By.XPATH,"//*[@id='payment-buttons-container']/button")
    CREDIT_CARD_TYPE_LIST = (By.ID,"sfc_cybersource_cc_type")
    CREDIT_CARD_NUMBER = (By.ID,"sfc_cybersource_cc_number")
    CREDIT_CARD_EXP_MONTH = (By.ID,"sfc_cybersource_expiration")
    CREDIT_CARD_EXP_YEAR = (By.ID,"sfc_cybersource_expiration_yr")
    SAVE_CREDIT_CARD_CHKBX = (By.ID,"sfc_cybersource_save_card")
    

    def __init__(self, driver):
        super(checkOutPage, self).__init__(driver)

    def set_Billing_Information(self,firstname,lastname,company,streetaddress1,streetaddress2,city,state,postalcode,country,telephone,fax):
        self.driver.find_element(*checkOutPage.FIRST_NAME).clear()
        self.driver.find_element(*checkOutPage.FIRST_NAME).send_keys(firstname)
        self.driver.find_element(*checkOutPage.LAST_NAME).clear()
        self.driver.find_element(*checkOutPage.LAST_NAME).send_keys(lastname)
        self.driver.find_element(*checkOutPage.COMPANY).clear()
        self.driver.find_element(*checkOutPage.COMPANY).send_keys(company)
        self.driver.find_element(*checkOutPage.STREET_ADDRESS1).clear()
        self.driver.find_element(*checkOutPage.STREET_ADDRESS1).send_keys(streetaddress1)
        self.driver.find_element(*checkOutPage.STREET_ADDRESS2).clear()
        self.driver.find_element(*checkOutPage.STREET_ADDRESS2).send_keys(streetaddress2)
        self.driver.find_element(*checkOutPage.CITY).clear()
        self.driver.find_element(*checkOutPage.CITY).send_keys(city)
        stateDDL = Select(self.driver.find_element(*checkOutPage.STATE_PROVINCE_LIST))
        stateDDL.select_by_visible_text(state)
        self.driver.find_element(*checkOutPage.POSTAL_CODE).clear()
        self.driver.find_element(*checkOutPage.POSTAL_CODE).send_keys(postalcode)
        countryDDL = Select(self.driver.find_element(*checkOutPage.COUNTRY_LIST))
        countryDDL.select_by_visible_text(country)
        self.driver.find_element(*checkOutPage.TELEPHONE).clear()
        self.driver.find_element(*checkOutPage.TELEPHONE).send_keys(telephone)
        self.driver.find_element(*checkOutPage.FAX).clear()
        self.driver.find_element(*checkOutPage.FAX).send_keys(fax)
        self.driver.find_element(*checkOutPage.CONTINUE_BTN).click()

    def set_Shipping_Information(self):
        self.driver.find_element(*checkOutPage.CONTINUE_Shipping_BTN).click()


    def set_Payment_Information_As_Credit_Card(self,creditCardType,CreditCardNumber,ExpirationDate,ExpirationYear):
        self.driver.find_element(*checkOutPage.CREDIT_CARD_RADIO_BTN).click()
        creditCardTypeDDL = Select(self.driver.find_element(*checkOutPage.CREDIT_CARD_TYPE_LIST))
        creditCardTypeDDL.select_by_visible_text(creditCardType)
        self.driver.find_element(*checkOutPage.CREDIT_CARD_NUMBER).send_keys(CreditCardNumber)
        creditCardExpMonthDDL = Select(self.driver.find_element(*checkOutPage.CREDIT_CARD_EXP_MONTH))
        creditCardExpMonthDDL.select_by_visible_text(ExpirationDate)
        creditCardExpYearDDL = Select(self.driver.find_element(*checkOutPage.CREDIT_CARD_EXP_YEAR))
        creditCardExpYearDDL.select_by_visible_text(ExpirationYear)
        self.driver.find_element(*checkOutPage.SAVE_CREDIT_CARD_CHKBX).click()
        self.driver.find_element(*checkOutPage.CONTINUE_PAYMENT_BTN).click()
        
    def read_Products(self):
        container = self.driver.find_elements_by_css_selector('form fieldset table#shopping-cart-table tbody tr')
        items = {}
        x = 1
        total = 0
        for i in container:                    
                    unit_price_lable = i.find_element_by_css_selector('td:nth-child(3).a-right span.cart-price span.price')
                    unit_price_lable_txt = unit_price_lable.text
                    unit_price_lable_float = float(unit_price_lable_txt.strip('$'))
                    total_price_lable = i.find_element_by_css_selector(' td:nth-child(5).a-right span.cart-price span.price')
                    total_price_lable_txt = total_price_lable.text
                    total_price_lable_txt_num_only = total_price_lable_txt.strip('$')
                    total_price_lable_float = float(total_price_lable_txt_num_only)
                    quantity_label = i.find_element_by_css_selector('td.a-center input.input-text.qty').get_attribute('value')
                    quantity_label_int = int(quantity_label)
                    Calc = float(unit_price_lable_float * quantity_label_int)
                    Calc_str = '%.2f' % Calc
                    #print("My Calc :- " + Calc_str)
                    #print("Total price after strip= " + total_price_lable_txt.strip('$'))
                    items["Total price-Of_item_" + str(x)] = unit_price_lable_float * quantity_label_int
                    #self.assertEqual(Calc_str,total_price_lable_txt)
                    x = x+1
        for key,value in items.items():
            total = total + items[key]
        print("CalculatedSubtotal : " + str(total)) 
        actualsubtotal = self.driver.find_element_by_xpath("//*[@id='shopping-cart-totals-table']/tbody/tr[1]/td[2]/span")
        actualsubtotal_txt = (actualsubtotal.text).strip('$')
        actualsubtotal_float = float(actualsubtotal_txt)
        print("ActualSubTotal : " + actualsubtotal_txt)
        self.assertEqual(total,actualsubtotal_float)

    def read_taxes(self):
         items = {}
         x = 1
         total = 0
         container = self.driver.find_elements_by_xpath("//*[@id='shopping-cart-totals-table']/tbody/tr")
         for i in container:
            row_name = i.find_element_by_xpath("//*[@id='shopping-cart-totals-table']/tbody/tr["+str(x)+"]/td[1]")
            row_name_txt = row_name.text
            print(row_name_txt)
            row_value = i.find_element_by_xpath("//*[@id='shopping-cart-totals-table']/tbody/tr["+str(x)+"]/td[2]")
            row_value_txt=(row_value.text).strip('$')
            row_value_float = float(row_value_txt)
            items[row_name_txt]=row_value_float
            print(row_value.text)
            x= x+1
         print (items)
         for key,value in items.items():
            if key != 'Subtotals':
              total = total + items[key]
            print ("Last total = " + str(total))


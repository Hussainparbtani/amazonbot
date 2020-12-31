# importing python libraries we will use
from selenium import webdriver
from time import sleep


# Amazon Purchase Bot Class which as
class Amazon_Purchase_Bot:

    # initilization function within class
    def __init__(self, chrome_driver_path, chrome_profile_path, asin, name, add_line_1, add_line_2, city, state,
                 zip_code, phone_number, card_number, msg):

        options = webdriver.ChromeOptions()

        options.add_argument(chrome_profile_path)

        self.driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)

        self.asin = asin

        self.name = name

        self.add_line_1 = add_line_1

        self.add_line_2 = add_line_2

        self.city = city

        self.state = state

        self.zip_code = zip_code

        self.phone_number = phone_number

        self.card_number = card_number

        self.msg = msg

    # function to go to smile.amazon website using Asin(product identifier)
    def go_to_product_url(self):

        self.driver.get('https://smile.amazon.com/dp/{}'.format(self.asin))

        sleep(3)

    # function to add product to cart
    def add_product_to_cart(self):

        self.driver.find_element_by_id('add-to-cart-button').click()

        sleep(5)

    # function to proceed to checkout
    def proceed_to_checkout(self):

        self.driver.find_element_by_id('attach-sidesheet-checkout-button').click()

        sleep(3)

    # function to add new address
    def add_new_address(self):

        self.driver.find_element_by_id('add-new-address-popover-link').click()

        sleep(3)

        Widget_Info = {
            'FullName': self.name,
            'Line1': self.add_line_1,
            'Line2': self.add_line_2,
            'City': self.city,
            'StateOrRegion': self.state,
            'PostalCode': self.zip_code,
            'PhoneNumber': self.phone_number
        }

        for i in range(len(Widget_Info)):
            self.driver.find_element_by_id(
                'address-ui-widgets-enterAddress{}'.format(list(Widget_Info.keys())[i])).clear()

            self.driver.find_element_by_id(
                'address-ui-widgets-enterAddress{}'.format(list(Widget_Info.keys())[i])).send_keys(
                list(Widget_Info.values())[i])

        self.driver.find_element_by_xpath("//span/span[contains(.,'Add address')]").click()

        sleep(3)

        try:
            driver.find_element_by_xpath("//span/span[contains(.,'Save Address')]").click()
        except:
            pass

        sleep(3)

    # function for selecting and verifying card
    def select_credit_card(self):

        try:

            self.driver.find_element_by_name('ppw-instrumentRowSelection').click()

            self.driver.find_element_by_xpath("//span/span[contains(.,'Use this payment method')]").click()

            self.driver.find_element_by_xpath("//*[contains(@name,'addCreditCardNumber')]").send_keys(self.card_number)

            self.driver.find_element_by_xpath("//span/span[contains(.,'Verify card')]").click()

            self.driver.find_element_by_xpath("//span/span[contains(.,'Use this payment method')]").click()


        except:

            pass

            sleep(3)

    # function to add gift msg
    def add_gift_options(self):

        self.driver.find_element_by_xpath("//span/span[contains(.,'Add gift options')]").click()

        sleep(3)

        self.driver.find_element_by_id('message-area-0').clear()

        self.driver.find_element_by_id('message-area-0').send_keys(self.msg)

        self.driver.find_element_by_xpath(
            "//*[@class='a-button a-button-primary chewbacca-enabled-save-gift-options-button']").click()

        sleep(3)

    # function to sumbit order
    def submit_order(self):

        self.driver.find_element_by_id('bottomSubmitOrderButtonId').click()

        sleep(3)

    # function
    def Auto_Order(self):

        self.go_to_product_url()

        self.add_product_to_cart()

        self.proceed_to_checkout()

        self.add_new_address()

        self.select_credit_card()

        self.add_gift_options()

        self.submit_order()
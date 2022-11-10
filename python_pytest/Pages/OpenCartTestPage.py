from selenium.webdriver.common.by import By
from python_pytest.Config.config import TestData
from python_pytest.Pages.BasePage import BasePage
import time

class OPenCarTestPage(BasePage):
    # Below are all opencart page locators
    Link_Iphone = (By.LINK_TEXT,"iPhone")
    Link_Description = (By.LINK_TEXT,"Description")
    Link_Review =  (By.PARTIAL_LINK_TEXT,"Reviews (0)")
    Input_Name = (By.ID,"input-name")
    Input_Review = (By.ID,"input-review")
    Input_Quantity = (By.ID,"input-quantity")
    Btn_Cart =  (By.ID,"button-cart")
    Cart_Total = (By.ID,"cart-total")
    Cart = (By.XPATH,"//*[@id='cart']/ul/li[2]/div/p/a[1]")
    Quantity= (By.XPATH,"//input[@name='quantity[129]']")
    Accordian_1 = (By.XPATH,"//*[@id='accordion']/div[1]/div[1]/h4/a")
    Accordian_2 = (By.XPATH, "//*[@id='accordion']/div[2]/div[1]/h4/a")
    Accordian_3 = (By.XPATH, "//*[@id='accordion']/div[3]/div[1]/h4/a")
    Checkout = (By.PARTIAL_LINK_TEXT,"Checkout")
    Email= (By.ID,"input-email")
    Password = (By.ID,"input-password")
    Login = (By.ID,"button-login")
    Payment_Address = (By.ID,"button-payment-address")
    Shipping_Address = (By.ID,"button-shipping-address")
    Shipping_Method = (By.ID,"button-shipping-method")
    Agree = (By.XPATH,"//input[@name='agree']")
    Payment_Method = (By.ID,"button-payment-method")
    Confirm = (By.ID,"button-confirm")

    #opencart page class constructor

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.OPENCART_URL)
        self.driver.maximize_window()

    def do_session_creation(self):
        # below line is use to scroll the page to high light the elements
        self.driver.execute_script("window.scrollTo(0, 750);")
        #Click on Iphone Icon
        self.do_click(self.Link_Iphone)
        # below line is use to scroll the page to high lisght the eleement.s
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Description
        self.do_click(self.Link_Description)
        # below line is use to scroll the page to high lisght the element.s
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Description
        self.do_click(self.Link_Review)
        # below line is use to scroll the page to high lisght the element.s
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Enter temprory text as Atul Tupe
        self.do_send_key(self.Input_Name,TestData.INPUT_NAME)
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Input Review
        self.do_click(self.Input_Review)
        preview_text = "Mac Book Pro comes in 13 inch, 14 inch Display with 8 GB & 16 GB Ram"
        self.do_send_key(self.Input_Name, preview_text)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Input Quantity to get highlighted
        self.do_click(self.Input_Quantity)
        # Enter the values in input Quantity
        self.do_send_key(self.Input_Quantity, TestData.INPUT_QUANTITY)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on button cart
        self.do_click(self.Btn_Cart)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Cart Total
        self.do_click(self.Cart_Total)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Cart Total
        self.do_click(self.Cart)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Accordian_1
        self.do_click(self.Accordian_1)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Accordian_2
        self.do_click(self.Accordian_2)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Accordian_3
        self.do_click(self.Accordian_3)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Check-Out
        self.do_click(self.Checkout)
        # Enter input Email
        self.do_send_key(self.Email, TestData.EMAIl)
        # Enter Password_OC is password for open cart
        self.do_send_key(self.Password, TestData.PASSWORD_OC)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Button Login
        self.do_click(self.Login)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Payment_Address
        self.do_click(self.Payment_Address)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Shiiping Address
        self.do_click(self.Shipping_Address)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Shiiping Method
        self.do_click(self.Shipping_Method)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Agree
        self.do_click(self.Agree)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Payment Methodßß
        self.do_click(self.Payment_Method)
        # below line is use to scroll the page to high light the element.
        self.driver.execute_script("window.scrollTo(0, 750);")
        # Click on Payment Methodßß
        self.do_click(self.Confirm)
        #TLTSID is fetch here which is pass to session search Page to replay
























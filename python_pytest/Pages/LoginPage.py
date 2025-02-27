#This class is use to perform login to TLSaaS environment
from selenium.webdriver.common.by import By
from python_pytest.Pages.BasePage import BasePage
from python_pytest.Config.config import TestData
from selenium.common.exceptions import TimeoutException
import time
from python_pytest.Tests.conftest import init_driver
class LoginPage(BasePage):
    ### By Locators or Object Repositories (OR) ###
    # click on login button
    Login_Btn = (By.CLASS_NAME,"login-green-button-inside")
    # click on trust_consent button
    trust_content = (By.ID,"truste-consent-button")
    # Enter the Acoustic ID / Email username
    Acoustic_ID_txt = (By.CLASS_NAME,"bx--text-input")
    # Click on Continue button
    Continue_Btn= (By.CLASS_NAME,"sign-in-form__button""")
    # Enter the password value
    Password_txt = (By.XPATH,"//*[@id='password']")
    # Click on signing in button
    Sign_In_Button =(By.CLASS_NAME,"sign-in-form__button")
    # Click on select organization button
    Org_Btn = (By.XPATH,"//a[@class='btn btn-info btn-xs ng-binding']")

    ### Constructor of LoginClass

    def __init__(self,driver):
        super().__init__(driver)
        #self.driver.get(TestData.Tealeaf_URL)
        self.driver.maximize_window()

    ##These are my Page Actions ###

    #This is page Action to perform the login ###

    def do_login(self,username,get_env):

        #below line clicks on first sign button
        self.do_click(self.Login_Btn)

        # below line clicks on trust button
        self.do_click(self.trust_content)

        # Enter Acoustic Id / email

        self.do_send_key(self.Acoustic_ID_txt,username)

        # Click on sign in button

        self.do_click(self.Continue_Btn)

        if get_env == "Q" or get_env == "S":

            password = "YLyjMKynDN13579!"
        else:
            password =  "YLyjMKynDN13579!"

        print(password)

        self.do_send_key(self.Password_txt,password)

        #Click on final signing button

        self.do_click(self.Sign_In_Button)

        # Click on select organization button

        time.sleep(15)
        try:
            self.do_click(self.Org_Btn)
        except  TimeoutException as ex:
            pass

    def do_login_normal_user(self,username,password):

        #below line clicks on first sign button
        self.do_click(self.Login_Btn)

        # below line clicks on trust button
        self.do_click(self.trust_content)

        # Enter Acoustic Id / email

        self.do_send_key(self.Acoustic_ID_txt,username)

        # Click on sign in button

        self.do_click(self.Continue_Btn)

        self.do_send_key(self.Password_txt,password)

        #Click on final signing button

        self.do_click(self.Sign_In_Button)

        # Click on select organization button

        time.sleep(15)
        try:
            self.do_click(self.Org_Btn)
        except  TimeoutException as ex:
            pass



















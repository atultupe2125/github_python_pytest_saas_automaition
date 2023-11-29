from selenium.webdriver.common.by import By
from python_pytest.Pages.BasePage import BasePage
from python_pytest.Config.config import TestData
from selenium.common.exceptions import NoSuchElementException
import time
class AA_GA_Settings(BasePage):
    ### By Locators or Object Repositories (OR) ###
    #Locator to click on login user to goto to admin settings for that user
    #Below xpath will use to click on login admin user drop down to enter into settings
    Admin_User_Settings_drop_down = (By.XPATH,"//a[@class='dropdown-toggle with-lsep ng-binding']")
    # Click on Admin menu from the drop down
    Admin_Menu = (By.XPATH,"//a[@class='ng-binding'][normalize-space()='Admin']")
    # Click on Settings Menu when enter into admin settings
    Settings_Menu = (By.XPATH,"//a[normalize-space()='Settings']")
    # Click on Edit button in settings
    Settings_Edit_Btn = (By.XPATH,"//button[normalize-space()='Edit']")
    # Select Adobe analytics conversion variable textbox to add its values
    AA_Integration_TxtBx = (By.XPATH,"//input[@id='adobeVariable']")
    # Select Google analytics conversion variable textbox to add its values
    GA_Integration_TxtBx = (By.XPATH,"//input[@id='googleVariable']")\
    # CLick on Save buttob after settings the AA and GA Integration
    Settings_Save_Btn = (By.XPATH,"//button[normalize-space()='Save']")

    # Constructor of AdminSettings Class
    def __init__(self,driver):
        super().__init__(driver)

    ##These are my Page Actions ###

    # This is page Action to perform the AdminSettings

    def do_aa_ga_admin_settings(self):
        #Below xpath will use to click on login admin user drop down to enter into settings
        self.do_click(self.Admin_User_Settings_drop_down)
        time.sleep(2)
        # Click on Admin menu from the drop down
        self.do_click(self.Admin_Menu)
        time.sleep(2)
        # Click on Settings Menu when enter into admin settings
        self.do_click(self.Settings_Menu)
        time.sleep(2)
        # Click on Edit button in settings
        self.do_click(self.Settings_Edit_Btn)
        time.sleep(5)
        # Select Adobe analytics conversion variable textbox to add its values
        self.do_send_key(self.AA_Integration_TxtBx,"TLTSessionId SaaS")
        time.sleep(5)
        # Select Google analytics conversion variable textbox to add its values
        self.do_send_key(self.GA_Integration_TxtBx, "1")
        time.sleep(2)
        # CLick on Save buttob after settings the AA and GA Integration
        self.do_click(self.Settings_Save_Btn)

    # This is page Action to perform the Normal Uset settings

    def do_aa_ga_normal_settings(self):
        #Below xpath will use to click on login admin user drop down to enter into settings
        self.do_click(self.Admin_User_Settings_drop_down)
        time.sleep(2)
        # Click on Admin menu from the drop down
        self.do_click(self.Admin_Menu)

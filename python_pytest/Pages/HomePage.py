from selenium.webdriver.common.by import By
from python_pytest.Pages.BasePage import BasePage
from python_pytest.Config.config import TestData
import time
#Home page is the landing page after the login
class HomePage(BasePage):
    ### By Locators or Object Repositories (OR) ###
    Session_Search = (By.XPATH, "//*[contains(text(),'Session Search')]")
    #Click on extension from hone page
    Extensions = (By.XPATH,"//span[@title='Extensions']")
    #installed chrome extn
    Install_Extn = (By.XPATH,"//*[contains(text(),'Install')]")
    #installed FF extn hyperlink click
    Install_FF_Extn_hyperlink = (By.XPATH,"//p[@class='anchoref ng-binding']")
    # installed FF extn Pop Menu Installed button
    Install_FF_Extn_Btn = (By.XPATH,"//button[@class='btn btn-primary btn-md ng-binding']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_session_search(self):
        # click on session search menu in Home Page
        self.do_click(self.Session_Search)

    #methof to handle the installed of chrome extensions
    def do_installed_extn(self):
        # click on the session menu extension
        #time.sleep(5)

        self.do_click(self.Extensions)

        #time.sleep(2)

        self.do_click(self.Install_Extn)

        # methof to handle the installed of chrome extensions

    def do_installed_FF_extn(self):
        # click on the session menu extension

        #time.sleep(10)

        self.do_click(self.Extensions)

        #time.sleep(10)

        self.do_click(self.Install_Extn)

        #time.sleep(2)

        self.do_click(self.Install_FF_Extn_Btn)





















































































































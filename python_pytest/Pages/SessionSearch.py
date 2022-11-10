from selenium.webdriver.common.by import By
import time
from python_pytest.Pages.OpenCartTestPage import OPenCarTestPage
from python_pytest.Pages.BasePage  import BasePage
from python_pytest.Config.config import TestData

class SessionSearch(BasePage):
    # Enter the TLTSID value in session search
    Session_Search_txt_box = (By.XPATH, "//*[@id='search-input']")
    # Click on session search Icon
    Session_Search_Icon = (By.XPATH,"//*[@id='new-search-btn']")
    # Click on Replay Button to replay the session in BBR
    Replay_Session_Icon = (By.XPATH,"(//span[@title='Replay session'])[1]")
    # Click on the drop down arrow to select the session time 7 days
    Session_Time = (By.XPATH,"//div[@class='fs-icon glyphicon glyphicon-chevron-down']")
    # Select the 7 days sesion time
    Session_Time_Value = (By.XPATH,"//div[normalize-space()='Last 7 days']")


    def __init__(self, driver):
        super().__init__(driver)


    def dosearch_tltsid(self,tltsid):

        #First click on the session search test box
        self.do_click(self.Session_Search_txt_box)

        # Click on the drop down arrow to select the session time 7 days
        self.do_click(self.Session_Time)

        # Select the 7 days session time

        self.do_click(self.Session_Time_Value)

        # TLTSID fetch from OpenCart return value

        self.do_send_key(self.Session_Search_txt_box,tltsid)

        # Click on Session Search Icon

        self.do_click(self.Session_Search_Icon)

        # Click on Relay Session Icon on Search Page

        self.do_click(self.Replay_Session_Icon)


















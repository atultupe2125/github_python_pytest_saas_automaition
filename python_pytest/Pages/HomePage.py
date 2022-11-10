from selenium.webdriver.common.by import By
from python_pytest.Pages.BasePage import BasePage
#Home page is the landing page after the login
class HomePage(BasePage):
    ### By Locators or Object Repositories (OR) ###
    Session_Search = (By.XPATH, "//*[contains(text(),'Session Search')]")
    Extensions = (By.XPATH,"//span[@title='Extensions']")
    Install_Extn = (By.XPATH,"//*[contains(text(),'Install')]")

    def __init__(self, driver):
        super().__init__(driver)

    def do_session_search(self):
        # click on session search menu in Home Page
        self.do_click(self.Session_Search)

    #methof to handle the installed the extensions
    def do_installed_extn(self):
        # click on the session menu extension

        self.do_click(self.Extensions)

        self.do_click(self.Install_Extn)


















































































































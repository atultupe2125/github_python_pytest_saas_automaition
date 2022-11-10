from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from python_pytest.Pages.OpenCartTestPage import OPenCarTestPage
from python_pytest.Pages.SessionSearch import SessionSearch
from python_pytest.Pages.BBR_Replay import BBR_Replay
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData

class Test_Session_Creation_BBR_Replay(BaseTest):

    def test_LoginPage(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD_TL)

    def test_HomePage(self):
        self.home_page = HomePage(self.driver)
        self.home_page.do_installed_extn()



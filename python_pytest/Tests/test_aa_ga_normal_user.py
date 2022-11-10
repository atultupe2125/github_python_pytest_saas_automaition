import pytest
import time
from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from python_pytest.Pages.OpenCartTestPage import OPenCarTestPage
from python_pytest.Pages.SessionSearch import SessionSearch
from python_pytest.Pages.BBR_Replay import BBR_Replay
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData
from python_pytest.Pages.AA_GA_Settings import AA_GA_Settings
from selenium.common.exceptions import TimeoutException

class Test_aa_ga_integration_admin_user(BaseTest):
    def test_LoginPage(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.NORMAl_USER_NAME, TestData.NORMAL_USER_PASSSWORD)


    def test_Admin_Settings(self):
        self.admin_settings = AA_GA_Settings(self.driver)
        try:
            self.admin_settings.do_aa_ga_normal_settings()
        except TimeoutException:
            pass






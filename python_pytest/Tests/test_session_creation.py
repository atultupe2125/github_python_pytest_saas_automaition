import pytest
import time
from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from python_pytest.Pages.OpenCartTestPage import OPenCarTestPage
from python_pytest.Pages.SessionSearch import SessionSearch
from python_pytest.Pages.BBR_Replay import BBR_Replay
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData

class Test_Session_Creation_BBR_Replay(BaseTest):

    def test_create_opencart_session(self):

        self.create_opencart_session = OPenCarTestPage(self.driver)
        #below line will execute the session creation process
        self.create_opencart_session.do_session_creation()












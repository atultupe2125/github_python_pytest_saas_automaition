import pytest
import time
import os
from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from python_pytest.Pages.OpenCartTestPage import OPenCarTestPage
from python_pytest.Pages.SessionSearch import SessionSearch
from python_pytest.Pages.BBR_Replay import BBR_Replay
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData
#from python_pytest.Tests.conftest import glb
from python_pytest.Tests import conftest


class Test_Session_Creation_BBR_Replay(BaseTest):

    def test_LoginPage(self,get_env):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_USER_NAME,get_env)

    def test_HomePage(self):
        self.home_page = HomePage(self.driver)
        self.home_page.do_session_search()

    def test_Session_Search(self):
        self.session_search = SessionSearch(self.driver)
        #absolute path
        #f = open("/Users/atultupe/PycharmProjects/python_pytest/Tests/sid.txt", "r")
        #relative path
        filepath = os.path.dirname(__file__)
        filepath = filepath + "/" + "sid.txt"
        f = open(filepath, "r")
        tltsid = f.read()
        #tltsid = conftest.glb
        f.close()
        self.session_search.dosearch_tltsid(tltsid)

    def test_BBR_Replay(self):
        self.bbr_replay = BBR_Replay(self.driver)
        self.bbr_replay.do_replay_play()
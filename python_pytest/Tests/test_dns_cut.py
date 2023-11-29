from selenium import webdriver
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData
from python_pytest.Config.dns_cut_extract_session_id import dns_cut_extract_session
from python_pytest.Pages.All_page_login import All_page_loginPage
import time
from selenium.common.exceptions import NoSuchElementException

class Test_dns_cut(BaseTest):

    def test_dns_cut_session_extract(self):
        self.dns_cust_extract_session = dns_cut_extract_session()
        self.dns_cust_extract_session.dns_cust_extract_session()

    def test_LoginPage(self):
        self.loginPage = All_page_loginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_USER_PASSWORD, TestData.ADMIN_USER_PASSWORD)

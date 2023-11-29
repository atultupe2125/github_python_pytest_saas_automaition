from python_pytest.Pages.LoginPage import LoginPage
from selenium import webdriver
from python_pytest.Config.config import TestData
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from  python_pytest.Config.installed_FF_extn import  install_FF_etn
import time
from selenium.webdriver import FirefoxOptions

class Test_installed_ff_extn(BaseTest):

    #Write Code for Login Methode
    def test_LoginPage(self,get_env):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_USER_NAME, get_env)

    def test_HomePage(self):
        self.home_page = HomePage(self.driver)
        self.home_page.do_installed_FF_extn()

    time.sleep(2)

    def test_install_FF_extn(self):
       self.install_ff_extn = install_FF_etn()
       self.install_ff_extn.install_FF_extn()






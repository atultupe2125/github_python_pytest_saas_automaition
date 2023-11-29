from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from python_pytest.Tests.test_base import BaseTest
from python_pytest.Config.config import TestData
from python_pytest.Config.installed_chrome_extn import install_chrome_etn

class Test_installed_chrome_ext(BaseTest):

    def test_LoginPage(self,get_env):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.ADMIN_USER_NAME, get_env)

    def test_HomePage(self):
        self.home_page = HomePage(self.driver)
        self.home_page.do_installed_extn()

    def test_install_extn(self):
        self.install_extn = install_chrome_etn()
        self.install_extn.install_chrom_extn()




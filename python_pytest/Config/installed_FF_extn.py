from selenium import webdriver
from python_pytest.Config.config import TestData
from python_pytest.Pages.LoginPage import LoginPage
from python_pytest.Pages.HomePage import HomePage
from selenium.webdriver import FirefoxOptions
import os
import time
class install_FF_etn:

    def install_FF_extn(self):
        options = FirefoxOptions()
        options.headless = True
        #driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH, options=options)
        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        # /Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/Config
        filepath = os.path.dirname(__file__)
        # Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/ -> means it perform $>cd ..
        filepath = os.path.realpath(os.path.join(filepath, '..'))
        # /Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
        filepath = os.path.join(filepath, 'drivers', 'saassnapshotcapture.xpi')
        #path = r"/Users/atultupe/Documents/Tealeaf/Fire_Fox_Etxn/saassnapshotcapture.xpi"
        driver.install_addon(filepath, temporary=True)
        driver.profile = webdriver.FirefoxProfile()
        driver.profile.add_extension(filepath)
        driver.profile.set_preference("security.fileuri.strict_origin_policy", False)
        driver.profile.update_preferences()
        #driver.close()


from python_pytest.Config.config import TestData
from python_pytest.Tests.test_base import BaseTest
from selenium import webdriver
import os
class install_chrome_etn(BaseTest):
    def __init__(self,driver):
        super().__init__(driver)

    def install_chrom_extn(self):

        options = webdriver.ChromeOptions()
        #/Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/Config
        filepath = os.path.dirname(__file__)
        #Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/ -> means it perform $>cd ..
        filepath = os.path.realpath(os.path.join(filepath, '..'))
        #/Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
        filepath = os.path.join(filepath, 'drivers', 'extension_22_9_1_0.crx')
        options.add_extension(filepath)
        webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)

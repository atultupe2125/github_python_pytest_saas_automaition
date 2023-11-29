import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from python_pytest.Config.config import TestData

class BaseTest:

        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.add_extension(TestData.EVENT_COMPOSER_BUID_CRX)
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        # options.add_argument("--headless=new") -> this syntax is now need ot be use for headless
        #options.headless = False -> this syntax is deprecated
        service = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://retail.acoustic-demo.com/')
        driver.maximize_window()

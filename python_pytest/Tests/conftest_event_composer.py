import pytest
import requests
from selenium import webdriver
from python_pytest.Config.config import TestData
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import os

#@pytest.fixture(scope="class")
#def get_browser(request):
#    br = request.config.getoption("--browser")
#    return br

@pytest.fixture(scope = "class")
def init_driver_event_composer():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    options.add_extension(TestData.EVENT_COMPOSER_BUID_CRX)
    options.headless = False
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH,options=options)
    driver.get('https://retail.acoustic-demo.com/')
    driver.maximize_window()
    yield driver
    driver.quit()





import pytest
import requests
from selenium import webdriver
from python_pytest.Config.config import TestData
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import os

global br
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="QA3")

@pytest.fixture(scope="session")
def teardown():
   yield
   #close_session()

@pytest.fixture(scope="class")
def get_browser(request):
    br = request.config.getoption("--browser")
    return br

@pytest.fixture(scope="class")
def get_env(request):
    setup = request.config.getoption("--env")
    return setup

@pytest.fixture(scope="class")
def init_driver(request,get_browser,get_env):
    if get_browser == "Firefox":
        options = FirefoxOptions()
        options.headless = False
        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH,options=options)
    elif get_browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        options.headless = False
        driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH,options=options)
    #below code will select the TLSaaS Env according the parameter value pass while executing the TC
    if get_env == "Q":
        driver.get("https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs")
        passwd  = "YLyjMKynDN13579!"
    elif get_env == "S":
        driver.get("https://tealeaf-staging.goacoustic.com/webapp/login")
        passwd  = "YLyjMKynDN13579!"
    elif get_env == "DAL":
        driver.get("https://tealeaf-us-1.goacoustic.com/webapp/login")
        passwd = "VZyDiWmDO003009!"
    elif get_env == "WDC":
        driver.get("https://tealeaf-us-2.goacoustic.com/webapp/login")
        passwd = "VZyDiWmDO003009!"
    elif get_env == "AP1":
        driver.get("https://tealeaf-ap-1.goacoustic.com/webapp/login")
        passwd = "VZyDiWmDO003009!"
    elif get_env == "EU1":
        driver.get("https://tealeaf-eu-1.goacoustic.com/webapp/login")
        passwd = "VZyDiWmDO003009!"
    request.cls.driver = driver
    yield
    SID = driver.get_cookie("TLTSID")
    filepath = os.path.dirname(__file__)
    filepath = filepath + "/" + "sid.txt"
    file = open(filepath, "w")
    file.write(SID["value"])
    file.close()
    driver.close()
    return get_env


import pytest
import requests
from selenium import webdriver
from python_pytest.Config.config import TestData
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["Chrome"], scope='class')
#@pytest.fixture(params=["firefox"], scope='class')
def init_driver(request):
#    if request.param == "Firefox":
#        options = FirefoxOptions()
#        options.headless = True
#        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH,options=options)
#        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH
    if request.param == "Chrome":
#        options = webdriver.ChromeOptions()
#        options.headless = True
#        driver = webdriver.Chrome(executable_path = TestData.CHROME_EXECUTABLE_PATH,options=options)
         driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    TestData.TLTSID = driver.get_cookie("TLTSID")
    request.cls.driver = driver
    yield
    SID = driver.get_cookie("TLTSID")
    #print(SID["value"])
    file = open("/Users/atultupe/PycharmProjects/python_pytest/Tests/sid.txt", "w")
    file.write(SID["value"])
    file.close()
    driver.close()


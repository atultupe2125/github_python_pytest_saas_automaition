
from selenium import webdriver
from python_pytest.Config.config import TestData
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
import time
"""This class is parent lf all Pages"""
"""It contains generic methods and Utilities"""
class BasePage:
    def __init__(self,driver):
        self.driver = driver

        #Common Actions written in BaseClass

    def do_click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_key(self,by_locator,text):
        WebDriverWait(self.driver,18).until(EC.visibility_of_element_located(by_locator)).clear()
        time.sleep(5)
        WebDriverWait(self.driver, 18).until(EC.visibility_of_element_located(by_locator)).click()
        time.sleep(5)
        WebDriverWait(self.driver,18).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title









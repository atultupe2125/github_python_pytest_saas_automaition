#to excute this code
# 1)click in Python Console
# 2) Place the mouse to location where you want the position
# to be. Then press control+shift+R
#URL to open extn in browser

#XREA Id:-4383 - Create Simple Event with Interaction type - Click from Event Composer

import pyautogui
import pytest
import pytest
import webbrowser
from selenium import webdriver
#import pyttsx3
import time
import random
import os
from selenium.common.exceptions import NoSuchElementException
from python_pytest.Config.config import TestData
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.eventing import Eventing

#Below class Test_event_click_creation extend BaseTest which is class of event composer

class Test_event_click_creation(BaseTest):
    try:
        def test_event_creation_click(self):
            #open the Bread and Butter test page
            self.driver.get("https://qa-pages.tealeaf-aws.com/opencart/sdk-n/qa/index.php")
            self.driver.maximize_window()
            #Click on CRUX® ARTISAN SERIES 5-CUP COFFEE MAKER product for Add to Cart button
            self.driver.find_element('xpath', '//a[normalize-space()="CRUX® ARTISAN SERIES 5-CUP COFFEE MAKER"]').click()
            #test execution steps for event composer extn UI
            event_composer_actions = TestData()
            event_composer_actions.event_composer_actions()

        def test_click_eventing(self):
            self.eventing = Eventing(self.driver)
            #below event creation for add to cart (a2c) Add button click called
            #pass the product unit price xapth to method in event class
            product_id = "//*[@id='content']/div/div[2]/ul[2]/li[1]/h2"
            event_name="CB_Product_unit_price"
            self.eventing.do_event_text_event_for_a2c(product_id,event_name)

    except NoSuchElementException as exc:
        pass
































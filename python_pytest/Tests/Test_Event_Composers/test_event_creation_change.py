#to excute this code
# 1)click in Python Console
# 2) Place the mouse to location where you want the position
# to be. Then press control+shift+R
#URL to open extn in browser

#XREA Id:-4384 - Create Simple Event with Interaction type - Change from Event Composer

import pyautogui
import pytest
import pytest
import webbrowser
from selenium import webdriver
import time
import random
import os
from python_pytest.Config.config import TestData
from selenium.webdriver.common.by import By
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.eventing import Eventing

class Test_event_change_creation(BaseTest):

    def test_event_creation_click(self):
       time.sleep(5)
       #specific click for change event type
       self.driver.find_element('xpath','//a[normalize-space()="Hummingbird printed sweater"]').click()
       time.sleep(5)
       #common actions on Event Composer called
       event_composer_actions = TestData()
       event_composer_actions.event_composer_actions()

    def test_change_eventing(self):
        self.eventing = Eventing(self.driver)
        self.eventing.do_event_change()
        self.driver.close()





























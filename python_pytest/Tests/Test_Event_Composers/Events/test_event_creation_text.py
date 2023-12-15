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
import time
import random
import os
from python_pytest.Config.config import TestData
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.eventing import Eventing
from selenium.common.exceptions import NoSuchElementException

class Test_event_text_creation(BaseTest):

    try:
        def test_event_creation_click(self):
            event_composer_actions = TestData()
            event_composer_actions.event_composer_actions()

        def test_text_eventing(self):
            self.eventing = Eventing(self.driver)
            self.eventing.do_event_text()
            self.driver.close()

    except NoSuchElementException as exc:
        pass





























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
from python_pytest.Config.config import TestData
from selenium.webdriver.common.by import By
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.eventing import Eventing

#Below class Test_event_click_creation extend BaseTest which is class of event composer

class Test_event_click_creation(BaseTest):

    def test_event_creation_click(self):
        event_composer_actions = TestData()
        event_composer_actions.event_composer_actions()

    def test_click_eventing(self):
        self.eventing = Eventing(self.driver)
        self.eventing.do_event_click()
































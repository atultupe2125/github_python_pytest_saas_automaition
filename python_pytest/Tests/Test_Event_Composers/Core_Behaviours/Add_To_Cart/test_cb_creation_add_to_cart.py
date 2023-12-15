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
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.corebehaviour import CoreBehaviour
from python_pytest.Pages.eventing import Eventing
from python_pytest.Tests.Test_Event_Composers.Events.test_event_creation_click import Test_event_click_creation

#Below class Test_event_click_creation extend BaseTest which is class of event composer

class Test_core_behaviour_creation(BaseTest):

    def test_cb_creation_click(self):
        event_composer_actions = TestData() # -> This load the test page and event composer UI
        event_composer_actions.event_composer_actions()  #-> This will perform the actions on UI.

    def test_click_eventing(self):
        self.eventing = Eventing(self.driver)
        self.eventing.do_event_click()

    def test_click_eventing(self):
        self.corebehaviour = CoreBehaviour(self.driver)
        self.corebehaviour.do_cb_add_to_cart()

































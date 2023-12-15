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
import pyttsx3
import time
import random
import os
from python_pytest.Config.config import TestData
from selenium.webdriver.common.by import By
from python_pytest.Tests.test_base_event_composer import BaseTest
from python_pytest.Pages.eventing import Eventing

class Test_event_change_creation(BaseTest):

    def test_event_creation_click(self):
       #Below code will open the Hummingbird printed sweater page on Luna Sites
       #this xpath kept seperate bcos is just single click specific to this Change type case
        time.sleep(5)
        self.driver.find_element_by_xpath('//a[normalize-space()="Hummingbird printed sweater"]').click()
        time.sleep(5)
        # below code is to remove the music icon if it gets loaded when browser loads
        pyautogui.moveTo(1418, 90)
        time.sleep(2)
        pyautogui.rightClick(1418, 90)
        time.sleep(5)
        print(pyautogui.position())
        pyautogui.moveTo(1360, 118)
        pyautogui.click(1360, 118)
        # below code is to remove the music icon if it gets loaded when browser loads
        time.sleep(5)
        #Below coord is to click on Extension
        pyautogui.moveTo(1417,83)
        time.sleep(2)
        pyautogui.click(1417,83)
        time.sleep(2)
        #Below coord is to click on Acoustic Extension
        pyautogui.moveTo(1220,227)
        time.sleep(2)
        pyautogui.click(1220,227)
        #Below coord is to click on login  username
        pyautogui.moveTo(1125,319)
        time.sleep(2)
        pyautogui.click(1125,319)
        pyautogui.typewrite(TestData.ADMIN_USER_NAME)
        #Below coord is to click on login  password
        pyautogui.moveTo(1120,390)
        time.sleep(2)
        pyautogui.click(1120,390)
        pyautogui.typewrite(TestData.ADMIN_USER_PASSWORD)
        #Below coord is to click on login  button
        pyautogui.moveTo(1151,459)
        time.sleep(2)
        pyautogui.click(1151,459)
        time.sleep(20)
        #add code here
        # Below coord is to click on AutoTealeaf Radio button
        pyautogui.moveTo(1122, 360)
        time.sleep(2)
        pyautogui.click(1122, 360)
        time.sleep(5)
        # Below coord is to click on Continue Button after selecting AutoTealeaf
        pyautogui.moveTo(1163, 449)
        time.sleep(2)
        pyautogui.click(1163, 449)
        # new code ends here
        time.sleep(2)
        #Below coord is to click on active and in-active toggle button
        pyautogui.moveTo(1214,353)
        time.sleep(10)
        pyautogui.click(1214,353)
        time.sleep(5)
        #Below coord is to click on Extension excited twice to close open extn window
        pyautogui.moveTo(1417,83)
        time.sleep(2)
        pyautogui.click(1417,83)

        #Below coord is to click on Extension
        pyautogui.moveTo(1417,83)
        time.sleep(2)
        pyautogui.click(1417,83)

    #from above pyautogui code the event composer html code get merge into webpage code
    #bcos of that below complete page is refresh which refreshes luna retail page code with event composer extn code
    #once refresh the driver can then find the respective elements on event composer extns

    def test_eventing(self):
        self.eventing = Eventing(self.driver)
        self.eventing.do_event_change()





























#to excute this code
# 1)click in Python Console
# 2) Place the mouse to location where you want the position
# to be. Then press control+shift+R

#Test Case :- XREA-4385 is automated using below scripts

import pyautogui
import pytest
import pyttsx3
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_pytest.Config.config import TestData

class Test_event_composer_etxn:
    def test_event_composer_etxn(self):
        #Below code will open the new browser session and also installed the acoustic event composer events extension
        self.options = webdriver.ChromeOptions()
        #make the chrome extension path more generic
        # CHROME_EXECUTABLE_PATH="/usr/local/bin/chromedriver"
        filepath = os.path.dirname(__file__)
        # Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/Tests/Test_Event_Composer -> means it perform $>cd ..
        filepath = os.path.realpath(os.path.join(filepath, '..'))
        #Above filepath will contans directory path upto /Users/atultupe/PycharmProjects/python_pytest/Tests
        filepath = os.path.realpath(os.path.join(filepath, '..'))
        # Above filepath will contans directory path upto /Users/atultupe/PycharmProjects/python_pytest/drivers/build.crx
        # /Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
        filepath = os.path.join(filepath, 'drivers', 'build.crx')
        chrome_driver = filepath
        #print(chrome_driver)
        self.options.add_extension(chrome_driver)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.get('https://retail.acoustic-demo.com/')
        #Below coord is to click on Extension
        # below code is to remove the music icon if it gets loaded when browser loads
        time.sleep(5)
        pyautogui.moveTo(1418, 90)
        time.sleep(2)
        pyautogui.rightClick(1418, 90)
        time.sleep(5)
        print(pyautogui.position())
        pyautogui.moveTo(1360, 118)
        pyautogui.click(1360, 118)
        # below code is to remove the music icon if it gets loaded when browser loads
        time.sleep(5)
        # Below coord is to click on Extension
        pyautogui.moveTo(1417, 83)
        time.sleep(2)
        pyautogui.click(1417, 83)
        time.sleep(2)
        # Below coord is to click on Acoustic Extension
        pyautogui.moveTo(1220, 227)
        time.sleep(2)
        pyautogui.click(1220, 227)
        # Below coord is to click on login  username
        pyautogui.moveTo(1125, 319)
        time.sleep(2)
        pyautogui.click(1125, 319)
        pyautogui.typewrite(TestData.ADMIN_USER_NAME)
        # Below coord is to click on login  password
        pyautogui.moveTo(1120, 390)
        time.sleep(2)
        pyautogui.click(1120, 390)
        pyautogui.typewrite(TestData.ADMIN_USER_PASSWORD)
        # Below coord is to click on login  button
        pyautogui.moveTo(1151, 459)
        time.sleep(2)
        pyautogui.click(1151, 459)
        time.sleep(20)
        # add code here
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
        # Below coord is to click on active and in-active toggle button
        pyautogui.moveTo(1214, 353)
        time.sleep(10)
        pyautogui.click(1214, 353)
        time.sleep(5)
        # Below coord is to click on Extension excited twice to close open extn window
        pyautogui.moveTo(1417, 83)
        time.sleep(2)
        pyautogui.click(1417, 83)
        # Below coord is to click on Extension
        pyautogui.moveTo(1417, 83)
        time.sleep(2)
        pyautogui.click(1417, 83)
        self.driver.close()
















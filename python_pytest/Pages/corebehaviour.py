from python_pytest.Pages.BasePage_event_composer import BasePage_event_composer
from selenium.webdriver.common.by import By
import time
import random
import pyautogui

#Below class will be use to defined various xpath, css selectors for core behaviour
# Please note CB stands for CB = CoreBehaviours

class CoreBehaviour(BasePage_event_composer):

    def __init__(self, driver):
        super().__init__(driver)

# Write the complete element selector here for this Text Case

    def do_cb_add_to_cart(self):

        # below is to click on Core Behaviour Tab of Event Composer UI -> Create Core Behaviour Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#landing-page > div:nth-child(2)')""")
        event.click()
        time.sleep(5)

        # below is to click on Core Behaviour Tab of Event Composer UI -> Create Core Behaviour Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#coreBehaviorTypeId > div > div.aco--dropdown > span > div > span')""")
        event.click()
        time.sleep(10)








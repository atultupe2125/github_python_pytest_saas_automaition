from python_pytest.Pages.BasePage_event_composer import BasePage_event_composer
from selenium.webdriver.common.by import By
import time
import random

class Eventing(BasePage_event_composer):

    def __init__(self, driver):
        super().__init__(driver)

    # Write the complete element selector here for this Text Case

    # below is to click on Event Composer UI -> Create Event Button
    Btn_create_event = (By.XPATH, "//div[@id='landing-page']//div[2]")
    #driver.execute_script("""return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")
    #Btn_create_event = self.driver.execute_script("""return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")

    # click on New Event Button
    Btn_new_event = (By.XPATH, "//button[normalize-space()='+ New Event']")

    # Click on interaction type

    interaction_type = (By.XPATH, "//div[@class='aco--dropdown__field']")

    # selecting interaction type as click
    interaction_type_click = (By.XPATH, "//div[@class='aco--dropdown__field']")

    # selecting interaction type as change
    interaction_type_change = (By.XPATH, "//*[@id='interactionType']/div/div[2]/span/div[2]/div/div[2]/div")

    # Below is xpath to interaction type as text

    interaction_type_text = (By.XPATH,"//*[@id='interactionType']/div/div[2]/span/div[2]/div/div[3]/div/div")

    #Below is xpath for interaction type as load
    #//*[@id="interactionType"]/div/div[2]/span/div[2]/div/div[4]/div/div
    interaction_type_load = (By.XPATH,"//*[@id='interactionType']/div/div[2]/span/div[2]/div/div[4]/div/div")

    # Click on Element Selector button on Event Composer extension
    btn_select_element = (By.XPATH, "//button[@id='icon-button']")

    # Select any button or url "Art" hyperlink on Luna Retail page
    # self.driver.find_element_by_xpath('//a[normalize-space()="Art"]').click()
    link_select_element = (By.XPATH, "//a[normalize-space()='Art']")

    # Event name text field clear and then click to make element active and,
    # event name made unique by attached random numbers to it, enter the unique name to event name
    txt_event_name = (By.XPATH, "//input[@id='eventName']")

    # Below click to Submit the Event for creation

    btn_submit = (By.XPATH, "//button[@id='submitEventFields']")

    # Below steps will extract the success msg from event created successfully

    lbl_success_msg = (By.XPATH, "//h3[@class='bx--toast-notification__title']")



    #below xpath is for input quantity

    input_quantity = (By.XPATH, "//input[@id='quantity_wanted']")

    #below is xpath to select the actual text
    txt_event_element = (By.XPATH, "//h2[@class='h2 products-section-title text-uppercase']")

    #load event normalised URL selection

    load_normalised_url = (By.XPATH, "//*[@id='normalized_url']/p[2]")

    def do_event_click(self):
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        # below is to click on Event Composer UI -> Create Event Button
        # self.driver.find_element_by_xpath('//div[@id="landing-page"]//div[2]').click()
        self.do_click(self.Btn_create_event)

        time.sleep(5)
        # click on New Event Button
        # //button[normalize-space()='+ New Event']
        # self.driver.find_element_by_xpath('//button[normalize-space()="+ New Event"]').click()
        self.do_click(self.Btn_new_event)

        time.sleep(5)
        # Click on interaction type
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type)

        # defining click event
        time.sleep(2)
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type_click)

        time.sleep(5)
        # Click on Select Element button on Event Composer extension
        # self.driver.find_element_by_xpath('//button[@id="icon-button"]').click()
        self.do_click(self.btn_select_element)

        time.sleep(2)
        # Select any button or url "Art" hyperlink on Luna Retail page
        # self.driver.find_element_by_xpath('//a[normalize-space()="Art"]').click()
        self.do_click(self.link_select_element)

        time.sleep(2)
        # Event name text field clear and then click to make element active
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').clear()self.do_click(self.txt_event_name)
        self.do_click(self.txt_event_name)
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').click()
        self.do_click(self.txt_event_name)
        time.sleep(2)
        rnd_num = random.randint(0, 20)
        # event name made unique by attached random numbers to it
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').send_keys("ALT_Test_Events_Click_" + str(rnd_num))
        txt = "ALT_Test_Events_Click_" + str(rnd_num)
        self.do_send_key(self.txt_event_name, txt)

        # Below click to Submit the Event for creation
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@id="submitEventFields"]').click()
        self.do_click(self.btn_submit)

        # Below steps will extract the success msg from event created successfully
        time.sleep(2)
        ent_msg = str(self.get_element_text(self.link_select_element))
        if ent_msg == "Success!":
            print("Pass")
        else:
            print("Failed")

    # below code is for event Iteraction type as Change

    def do_event_change(self):
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        # below is to click on Event Composer UI -> Create Event Button
        # self.driver.find_element_by_xpath('//div[@id="landing-page"]//div[2]').click()
        self.do_click(self.Btn_create_event)

        time.sleep(5)
        # click on New Event Button
        # //button[normalize-space()='+ New Event']
        # self.driver.find_element_by_xpath('//button[normalize-space()="+ New Event"]').click()
        self.do_click(self.Btn_new_event)

        time.sleep(5)
        # Click on interaction type
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type)

        # defining click event
        time.sleep(5)
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type_change)

        time.sleep(5)
        # Click on Select Element button on Event Composer extension
        # self.driver.find_element_by_xpath('//button[@id="icon-button"]').click()
        self.do_click(self.btn_select_element)

        time.sleep(2)
        # Select input quantity after click on Element selector button
        # self.driver.find_element_by_xpath('//a[normalize-space()="Art"]').click()
        #self.do_click(self.input_quantity)

        #enter the input quantity value
        txt=str("5")
        self.do_send_key(self.input_quantity, txt)
        
        # Event name text field clear and then click to make element active
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').clear()self.do_click(self.txt_event_name)
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        # event name made unique by attached random numbers to it
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').send_keys("ALT_Test_Events_change_" + str(rnd_num))
        txt = "ALT_Test_Events_change_" + str(rnd_num)
        self.do_send_key(self.txt_event_name, txt)

        # Below click to Submit the Event for creation
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@id="submitEventFields"]').click()
        self.do_click(self.btn_submit)

        # Below steps will extract the success msg from event created successfully
        time.sleep(2)
        ent_msg = str(self.get_element_text(self.link_select_element))
        if ent_msg == "Success!":
            print("Pass")
        else:
            print("Failed")

    # below code is for event Iteraction type as Text

    def do_event_text(self):
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        # below is to click on Event Composer UI -> Create Event Button
        # self.driver.find_element_by_xpath('//div[@id="landing-page"]//div[2]').click()
        self.do_click(self.Btn_create_event)

        time.sleep(5)
        # click on New Event Button
        # //button[normalize-space()='+ New Event']
        # self.driver.find_element_by_xpath('//button[normalize-space()="+ New Event"]').click()
        self.do_click(self.Btn_new_event)

        time.sleep(5)
        # Click on interaction type
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type)

        # defining iteraction text event
        time.sleep(10)
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()

        self.do_click(self.interaction_type_text)

        time.sleep(5)
        # Click on Select Element button on Event Composer extension
        # self.driver.find_element_by_xpath('//button[@id="icon-button"]').click()
        self.do_click(self.btn_select_element)

        time.sleep(2)
        # Select the text element / value to create the event
        self.do_click(self.txt_event_element)

        # Event name text field clear and then click to make element active
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').clear()self.do_click(self.txt_event_name)
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        # event name made unique by attached random numbers to it
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').send_keys("ALT_Test_Events_change_" + str(rnd_num))
        txt = "ALT_Test_Events_text_" + str(rnd_num)
        self.do_send_key(self.txt_event_name, txt)

        # Below click to Submit the Event for creation
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@id="submitEventFields"]').click()
        self.do_click(self.btn_submit)

        # Below steps will extract the success msg from event created successfully
        time.sleep(2)
        ent_msg = str(self.get_element_text(self.link_select_element))
        if ent_msg == "Success!":
            print("Pass")
        else:
            print("Failed")

    # below code is for event Iteraction type as Load
    def do_event_load(self):
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        # below is to click on Event Composer UI -> Create Event Button
        # self.driver.find_element_by_xpath('//div[@id="landing-page"]//div[2]').click()
        self.do_click(self.Btn_create_event)

        time.sleep(5)
        # click on New Event Button
        # //button[normalize-space()='+ New Event']
        # self.driver.find_element_by_xpath('//button[normalize-space()="+ New Event"]').click()
        self.do_click(self.Btn_new_event)

        time.sleep(5)
        # Click on interaction type
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type)

        # defining iteraction text event
        time.sleep(10)
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()

        self.do_click(self.interaction_type_load)

        #//*[@id="normalized_url"]/p[2]

        time.sleep(5)
        # Click on Element Selector button on Event Composer extension
        # self.driver.find_element_by_xpath('//button[@id="icon-button"]').click()
        self.do_click(self.btn_select_element)

        time.sleep(5)
        # select the normalised URL for load event
        self.do_click(self.load_normalised_url)

        # Event name text field clear and then click to make element active
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').clear()self.do_click(self.txt_event_name)
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        # event name made unique by attached random numbers to it
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').send_keys("ALT_Test_Events_change_" + str(rnd_num))
        txt = "ALT_Test_Events_load_" + str(rnd_num)
        self.do_send_key(self.txt_event_name, txt)

        # Below click to Submit the Event for creation
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@id="submitEventFields"]').click()
        self.do_click(self.btn_submit)

        # Below steps will extract the success msg from event created successfully
        time.sleep(2)
        ent_msg = str(self.get_element_text(self.link_select_element))
        if ent_msg == "Success!":
            print("Pass")
        else:
            print("Failed")

        # below code is for event Iteraction type as Page Data
    def do_event_page_data(self):
        time.sleep(5)
        self.driver.refresh()
        time.sleep(15)
        # below is to click on Event Composer UI -> Create Event Button
        # self.driver.find_element_by_xpath('//div[@id="landing-page"]//div[2]').click()
        self.do_click(self.Btn_create_event)

        time.sleep(5)
        # click on New Event Button
        # //button[normalize-space()='+ New Event']
        # self.driver.find_element_by_xpath('//button[normalize-space()="+ New Event"]').click()
        self.do_click(self.Btn_new_event)

        time.sleep(5)
        # Click on interaction type
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        self.do_click(self.interaction_type)

        # defining iteraction text event
        time.sleep(10)
        # self.driver.find_element_by_xpath('//div[@class="aco--dropdown__field"]').click()
        # write the code from below for interaction type Page Data
        self.do_click(self.interaction_type_load)

        # //*[@id="normalized_url"]/p[2]

        time.sleep(5)
        # Click on Element Selector button on Event Composer extension
        # self.driver.find_element_by_xpath('//button[@id="icon-button"]').click()
        self.do_click(self.btn_select_element)

        time.sleep(5)
        # select the normalised URL for load event
        self.do_click(self.load_normalised_url)

        # Event name text field clear and then click to make element active
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').clear()self.do_click(self.txt_event_name)
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        # event name made unique by attached random numbers to it
        # self.driver.find_element_by_xpath('//input[@id="eventName"]').send_keys("ALT_Test_Events_change_" + str(rnd_num))
        txt = "ALT_Test_Events_load_" + str(rnd_num)
        self.do_send_key(self.txt_event_name, txt)

        # Below click to Submit the Event for creation
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@id="submitEventFields"]').click()
        self.do_click(self.btn_submit)

        # Below steps will extract the success msg from event created successfully
        time.sleep(2)
        ent_msg = str(self.get_element_text(self.link_select_element))
        if ent_msg == "Success!":
            print("Pass")
        else:
            print("Failed")



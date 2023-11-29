from python_pytest.Pages.BasePage_event_composer import BasePage_event_composer
from selenium.webdriver.common.by import By
import time
import random

#selector for text
#document.querySelector("#extension_entry").shadowRoot.querySelector("#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown.aco--dropdown--open > span > div.aco--dropdown__menu > div > div:nth-child(3) > div > div")
#document.querySelector("#extension_entry").shadowRoot.querySelector("#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown.aco--dropdown--open > span > div.aco--dropdown__menu > div > div:nth-child(4) > div > div")

class Eventing(BasePage_event_composer):

    def __init__(self, driver):
        super().__init__(driver)

# Write the complete element selector here for this Text Case

    # below is to click on Event Composer UI -> Create Event Button
    #Btn_create_event = (By.XPATH, "//div[@id='landing-page']//div[2]")
    #driver.execute_script("""return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")


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

        # below is to click on Event Composer UI -> Create Event Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#landing-page > div:nth-child(3) > div > div > p.bx--typography-text__body-long-01')""")
        event.click()

        time.sleep(2)
        # click on New Event Button
        new_event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#list-event-definitions > div.styles-module_header__f2zT5LO > button')""")
        new_event.click()

        # select the drop down interaction type
        time.sleep(3)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown > span > div')""")
        interaction_type.click()

        # Select the click interaction type
        time.sleep(5)
        interaction_type_click = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown > span > div')""")
        interaction_type_click.click()


        # Click on element selector
        time.sleep(5)
        element_selector_click = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#icon-button')""")
        element_selector_click.click()

        # click on the Art hyperlink
        time.sleep(5)
        self.driver.find_element("xpath",'//a[normalize-space()="Art"]').click()

        time.sleep(2)
        # Click on the event name
        # document. querySelector("#extension_entry").shadowRoot.querySelector("#eventName")
        event_name = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")
        time.sleep(2)
        event_name.click()
        time.sleep(2)
        event_name.clear()
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        event_name.send_keys("ALT_Test_Events_Interaction_click" + str(rnd_num))

        time.sleep(5)
        # Click on the submit button
        submit_button = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#submitEventFields')""")
        submit_button.click()

    # below code is for event Iteraction type as Change

    def do_event_change(self):

        # below is to click on Event Composer UI -> Create Event Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#landing-page > div:nth-child(3) > div > div > p.bx--typography-text__body-long-01')""")
        event.click()

        time.sleep(2)
        # click on New Event Button
        new_event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#list-event-definitions > div.styles-module_header__f2zT5LO > button')""")
        new_event.click()

        # select the drop down interaction type
        time.sleep(3)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown > span > div')""")
        interaction_type.click()

        time.sleep(5)
        #Select the change interaction type.
        interaction_type_change = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown.aco--dropdown--open > span > div.aco--dropdown__menu > div > div:nth-child(2) > div > div')""")
        interaction_type_change.click()

        # Click on element selector
        time.sleep(5)
        element_selector_click = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#icon-button')""")
        element_selector_click.click()

        time.sleep(2)
        #self.driver.find_element_by_xpath("//input[@id='quantity_wanted']").click()

        txt = str("5")
        self.do_send_key(self.input_quantity, txt)

        # document. querySelector("#extension_entry").shadowRoot.querySelector("#eventName")
        event_name = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")
        time.sleep(2)
        event_name.click()
        time.sleep(2)
        event_name.clear()
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        event_name.send_keys("ALT_Test_Events_Interaction_Change" + str(rnd_num))


        # Below click to Submit the Event for creation
        time.sleep(2)
        # Click on the submit button
        submit_button = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#submitEventFields')""")
        submit_button.click()

    def do_event_text(self):
        # below is to click on Event Composer UI -> Create Event Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#landing-page > div:nth-child(3) > div > div > p.bx--typography-text__body-long-01')""")
        event.click()

        time.sleep(2)
        # click on New Event Button
        new_event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#list-event-definitions > div.styles-module_header__f2zT5LO > button')""")
        new_event.click()

        # select the drop down interaction type
        time.sleep(3)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown > span > div')""")
        interaction_type.click()

        # select the text interaction type
        time.sleep(5)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown.aco--dropdown--open > span > div.aco--dropdown__menu > div > div:nth-child(3) > div > div')""")
        interaction_type.click()

        # Click on element selector
        time.sleep(5)
        element_selector_click = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#icon-button')""")
        element_selector_click.click()

        # click on text "Lorem ipsum dolor sit amet conse ctetu" pn page  https://retail.acoustic-demo.com/
        time.sleep(5)
        self.driver.find_element("xpath", '//*[@id="custom-text"]/p[1]/strong').click()

        time.sleep(2)
        # Click on the event name
        # document. querySelector("#extension_entry").shadowRoot.querySelector("#eventName")
        event_name = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#eventName')""")
        time.sleep(2)
        event_name.click()
        time.sleep(2)
        event_name.clear()
        time.sleep(2)
        rnd_num = random.randint(0, 30)
        event_name.send_keys("ALT_Test_Events_Interaction_text" + str(rnd_num))

        time.sleep(5)
        # Click on the submit button
        submit_button = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#submitEventFields')""")
        submit_button.click()

    def do_event_load(self):

        # below is to click on Event Composer UI -> Create Event Button
        event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#landing-page > div:nth-child(3) > div > div > p.bx--typography-text__body-long-01')""")
        event.click()

        time.sleep(2)
        # click on New Event Button
        new_event = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#list-event-definitions > div.styles-module_header__f2zT5LO > button')""")
        new_event.click()

        # select the drop down interaction type
        time.sleep(3)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown > span > div')""")
        interaction_type.click()

        # select the load interaction type
        time.sleep(5)
        interaction_type = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#interactionType > div > div.styles-module_dropdown-event_eQQ3zHzy.aco--dropdown.aco--dropdown--open > span > div.aco--dropdown__menu > div > div:nth-child(4) > div > div')""")
        interaction_type.click()

        # Click on element selector Track from this link
        time.sleep(5)
        element_selector_click = self.driver.execute_script(
            """return document.querySelector('#extension_entry').shadowRoot.querySelector('#icon-button')""")
        element_selector_click.click()












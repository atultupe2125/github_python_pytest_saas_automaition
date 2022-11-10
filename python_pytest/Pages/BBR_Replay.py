from selenium.webdriver.common.by import By

from python_pytest.Pages.BasePage import BasePage
# BBR relay page is where the user view the replay
class BBR_Replay(BasePage):
    # Click on Replay Button to replay the session in BBR
    Replay_Session = (By.XPATH,"//span[@title='Play']")


    def __init__(self, driver):
        super().__init__(driver)


    def do_replay_play(self):

        # Below will use to perform the relay sessions
        self.do_click(self.Replay_Session)

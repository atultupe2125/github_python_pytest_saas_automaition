import os
import pyautogui
import time
class TestData:
    #Below are some Class Variable initialise
    #CHROME_EXECUTABLE_PATH="/usr/local/bin/chromedriver"
    # Below section will setup the variable CHROME_EXECUTABLE_PATH
    filepath = os.path.dirname(__file__)
    # Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/Config -> means it perform $>cd ..
    filepath = os.path.realpath(os.path.join(filepath, '..'))
    #/Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
    filepath = os.path.join(filepath, 'drivers', 'chromedriver')
    print (filepath)
    CHROME_EXECUTABLE_PATH = filepath
    #Below section will setup the variable FIREFOX_EXECUTABLE_PATH
    filepath = os.path.dirname(__file__)
    # Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/ -> means it perform $>cd ..
    filepath = os.path.realpath(os.path.join(filepath, '..'))
    # /Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
    filepath = os.path.join(filepath, 'drivers', 'geckodriver')
    # Below section will setup the variable FIREFOX_EXECUTABLE_PATH ends
    FIREFOX_EXECUTABLE_PATH = filepath
    # Below section will setup the variable Event_Composer_Extn build.crx file
    filepath = os.path.dirname(__file__)
    # Below line will give path -> /Users/atultupe/PycharmProjects/python_pytest/ -> means it perform $>cd ..
    filepath = os.path.realpath(os.path.join(filepath, '..'))
    # /Users/atultupe/PycharmProjects/python_pytest/drivers/extension_22_9_1_0.crx
    filepath = os.path.join(filepath, 'drivers', 'build.crx')
    # Below section will setup the variable FIREFOX_EXECUTABLE_PATH ends
    EVENT_COMPOSER_BUID_CRX = filepath
    #Tealeaf_URL="https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs"
    #TL SaaS Staging
    #Tealeaf_URL="https://tealeaf-staging.goacoustic.com/webapp/login"
    #opencart QA
    #OPENCART_URL="https://qa-pages.tealeaf-aws.com/opencart/sdk-n/qa/index.php"
    OPENCART_URL="https://qa-pages.tealeaf-aws.com/opencart/sdk-n/mctl-1/index.php"
    #OPENCART_URL = "http://10.235.137.37/opencart/upload/"
    # OpenCart Statging
    #OPENCART_URL = "https://qa-pages.tealeaf-aws.com/opencart/sdk-n/staging/index.php"
    ADMIN_USER_NAME="massweather1980@zoho.eu"
    ADMIN_USER_PASSWORD="YLyjMKynDN13579!"
    NORMAl_USER_NAME="kevin.mssgs@zoho.eu"
    NORMAL_USER_PASSSWORD="WgHLqtD19081984$"
    EMAIl="atul.tupe@gmail.com"
    PASSWORD_OC="Kiran#2125"
    INPUT_QUANTITY="1"
    INPUT_NAME="Atul"
    #TLTSID=""

    # Below method is use to return the TLSaaS URL base on the informaiton in log file
    def dnc_cust_select_env(self):
        with open(r"/Users/atultupe/Documents/Tealeaf/TLSaaS/dns_cut_files/TLSaaSFeeder_20221011.log", 'r') as fp:
            for l_no, line in enumerate(fp):
                # search string
                # env is Staging = Staging

                if 'http://collector-tealeaf-staging.goacoustic.com/collector/collectorPost' in line:
                    self.url = "https://tealeaf-staging.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is QA = QA
                if 'http://collector-eaoc.qa.goacoustic.com/collector/collectorPost' in line:
                    # print('Env is QA')
                    self.url = "https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs"
                    return self.url
                    break
                # env is US-1 = #DAL
                if 'http://lib-us-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is WDC')
                    self.url = "https://tealeaf-us-1.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is US-2 = #WDC
                if 'http://lib-us-2.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is Dal')
                    self.url = "https://tealeaf-us-2.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is AP-1= #Sydney
                if 'http://lib-ap-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is Sydney')
                    self.url = "https://tealeaf-ap-1.goacoustic.com/webapp/login"
                    return self.url
                    break
                # env is AP-1= #Sydney
                if 'http://lib-eu-1.brilliantcollector.com/collector/collectorPost' in line:
                    # print('Env is France')
                    self.url = "https://tealeaf-eu-1.goacoustic.com/webapp/login"
                    return self.url
                    break

    def event_composer_actions(self):

        # To work with pyautogui use shift+control+R to execute the script  after placing the cursor to get the
        # x and y co-ordinates. User print(pyautogui.position()) to print the x,y

        # below code is to right click on music Icon and remove the music icon
        pyautogui.moveTo(1320, 90)
        time.sleep(5)
        pyautogui.rightClick(1320, 90)
        time.sleep(5)
        # below code is to click on music icon menu to remove it
        pyautogui.moveTo(1298, 121)
        time.sleep(2)
        pyautogui.click(1298, 121)
        time.sleep(2)
        # Below code to click on chrome extn icon
        pyautogui.moveTo(1320, 90)
        time.sleep(2)
        pyautogui.click(1320, 90)
        time.sleep(5)
        # Below coord is to click on Extension
        pyautogui.moveTo(1115, 233)
        time.sleep(2)
        pyautogui.click(1115, 233)
        time.sleep(5)
        # Below coord is to click on login  username
        pyautogui.moveTo(1043, 326)
        time.sleep(2)
        pyautogui.click(1043, 326)
        pyautogui.typewrite("massweather1980@zoho.eu")
        # Below coord is to click on login  password
        pyautogui.moveTo(1066, 396)
        time.sleep(2)
        pyautogui.click(1066, 396)
        pyautogui.typewrite("YLyjMKynDN13579!")
        time.sleep(5)
        # Below coord is to click on login  button
        pyautogui.moveTo(1047, 513)
        time.sleep(2)
        pyautogui.click(1047, 513)
        time.sleep(20)
        # Below coord is to click on active and in-active toggle button
        pyautogui.moveTo(1112, 361)
        time.sleep(2)
        pyautogui.click(1112, 361)
        time.sleep(5)

        # Below coord is to click on Extension  icon twice to close open extn window
        pyautogui.moveTo(1417, 83)
        time.sleep(2)
        pyautogui.click(1417, 83)

        # Below coord is to click on Extension  icon twice to close open extn window
        pyautogui.moveTo(1324, 85)
        time.sleep(2)
        pyautogui.click(1324, 85)
        time.sleep(10)

    # from above pyautogui code the event composer html code get merge into webpage code
    # bcos of that below complete page is refresh which refreshes luna retail page code with event composer extn code
    # once refresh the driver can then find the respective elements on event composer extns






from selenium import webdriver
import time
from xlwt import Workbook
from selenium.common.exceptions import NoSuchElementException
import  sys
#below function
def select_env():
    with open(r"/Users/atultupe/Downloads/dns_cut_files/TLSaaSFeeder_20221011.log", 'r') as fp:
        for l_no, line in enumerate(fp):
            # search string
            # env is Staging = Staging
            if 'http://collector-tealeaf-staging.goacoustic.com/collector/collectorPost' in line:
                url = "https://tealeaf-staging.goacoustic.com/webapp/login"
                return url
                break
            # env is QA = QA
            if 'http://collector-eaoc.qa.goacoustic.com/collector/collectorPost' in line:
                #print('Env is QA')
                url = "https://eaoc.qa.goacoustic.com/webapp/login#/admin/orgs"
                return url
                break
            # env is US-1 = #DAL
            if 'http://lib-us-1.brilliantcollector.com/collector/collectorPost' in line:
                #print('Env is WDC')
                url = "https://tealeaf-us-1.goacoustic.com/webapp/login"
                return url
                break
            # env is US-2 = #WDC
            if 'http://lib-us-2.brilliantcollector.com/collector/collectorPost' in line:
                #print('Env is Dal')
                url = "https://tealeaf-us-2.goacoustic.com/webapp/login"
                return  url
                break
            # env is AP-1= #Sydney
            if 'http://lib-ap-1.brilliantcollector.com/collector/collectorPost' in line:
                #print('Env is Sydney')
                url = "https://tealeaf-ap-1.goacoustic.com/webapp/login"
                return url
                break
            # env is AP-1= #Sydney
            if 'http://lib-eu-1.brilliantcollector.com/collector/collectorPost' in line:
                #print('Env is France')
                url = "https://tealeaf-eu-1.goacoustic.com/webapp/login"
                return  url
                break
dataLog = []
# open the log file in read write mode
with open('/Users/atultupe/Downloads/dns_cut_files/TLSaaSFeeder_20221011.log', 'rt') as f:
    data = f.readlines()
for line in data:
    #Filter only the ines contaning TLTSID and append it to python list (datalog)
    if 'New TLTSID:' in line:
        dataLog.append(line)
# open file in write mode
with open(r'/Users/atultupe/Downloads/dns_cut_files/TLTSID_EXTRACTED.txt', 'w') as fp:
    for item in dataLog:
        # below code is data processing command use to filter out only the TLSSID from the data
        Index=int(item.find('New'))
        item=item.replace(item[:Index], "")
        item=item.replace("New","")
        Index = int(item.find('D:'))
        item = item.replace(item[:Index], "")
        item = item.replace(item[:3], "")
        fp.write(str(item))
dataLog = []
a_file = open(r'/Users/atultupe/Downloads/dns_cut_files/TLTSID_EXTRACTED.txt')
number_of_lines = 1000
for i in range(number_of_lines):
    line = a_file.readline()
    line = line[0:32]
    dataLog.append(line)
unique_list = []
for x in dataLog:
    if x not in unique_list:
        unique_list.append(x)
length=  len(unique_list)
missing_tltsid=[]
for i in range(length):
        tltsid = unique_list[i]
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.maximize_window()
        env = select_env()
        driver.get(env)
        driver.find_element_by_class_name("login-green-button-inside").click()
        driver.find_element_by_id("truste-consent-button").click()
        driver.find_element_by_class_name("bx--text-input").clear()
        driver.find_element_by_class_name("bx--text-input").send_keys("massweather1980@zoho.eu")
        driver.find_element_by_class_name("sign-in-form__button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='password']").clear()
        driver.find_element_by_xpath("//*[@id='password']").send_keys("VZyDiWmDO003009!")
        driver.find_element_by_class_name("sign-in-form__button").click()
        time.sleep(30)
        driver.find_element_by_xpath("//*[contains(text(),'Session Search')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='search-input']").clear()
        driver.find_element_by_xpath("//*[@id='search-input']").click()
        driver.find_element_by_xpath("//*[@id='search-input']").send_keys(tltsid)
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='new-search-btn']").click()
        try:
            time.sleep(10)
            driver.find_element_by_xpath("(//span[@title='Replay session'])[1]").click()
            time.sleep(10)
        except:
            missing_tltsid = tltsid
            print(missing_tltsid)
            pass
        driver.close()
#here empty list means false, hence its reverse to check and testcase is pass
if missing_tltsid:
    # This is true condition means list is not empty
    print('DNS Cut test case fail')
    # Workbook is created
    wb = Workbook()  # add_sheet is used to create sheet.
    ws = wb.add_sheet('Sheet 1')
    first_row = 0
    for index, item in enumerate(missing_tltsid):
        ws.write(index, first_row, item)
    wb.save('/Users/atultupe/Downloads/dns_cut_files/missing_tltsid.xls')
else:
    print('DNS Cut test case pass')







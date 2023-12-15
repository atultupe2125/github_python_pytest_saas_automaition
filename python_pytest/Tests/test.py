import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#from python_pytest.Config.config import TestData
# below code is to remove the music icon if it gets loaded when browser loads
options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=800,600")
options.add_argument("--disable-dev-shm-usage")
options.add_extension("/Users/atultupe/Documents/PycharmProjects/python_pytest/drivers/build.crx")
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# options.add_argument("--headless=new") -> this syntax is now need ot be use for headless
# options.headless = False -> this syntax is deprecated
service = Service(executable_path="/Users/atultupe/Documents/PycharmProjects/python_pytest/drivers/chromedriver", options=options)
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://retail.acoustic-demo.com/')
driver.maximize_window()
#below code is to right click on music Icon and remove the music icon
pyautogui.moveTo(1320, 90)
time.sleep(5)
pyautogui.rightClick(1320, 90)
time.sleep(5)
#below code is to click on music icon menu to remove it
pyautogui.moveTo(1298, 121)
time.sleep(2)
pyautogui.click(1298, 121)
time.sleep(2)
#Below code to click on chrome extn icon
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

# Below coord is to click on Extension excited twice to close open extn window
pyautogui.moveTo(1417, 83)
time.sleep(2)
pyautogui.click(1417, 83)

# Below coord is to click on Extension
pyautogui.moveTo(1324, 85)
time.sleep(2)
pyautogui.click(1324, 85)
time.sleep(10)

print(pyautogui.position())
"""

"""





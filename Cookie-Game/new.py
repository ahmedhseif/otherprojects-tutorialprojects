# Importing required packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up working Selenium for Mac OSX on Chrome 96.4554.55
ser = Service("C:\\Development\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://orteil.dashnet.org/cookieclicker/')
cookie_clicker = driver.find_element(By.ID, 'bigCookie')

# Setting Time Out
PERIOD_OF_TIME = 300
start = time.time()

#Clicking Time
while True:
    # Check it upgrade is available
    price_check = driver.find_elements(By.CSS_SELECTOR, '.product')
    for produce in price_check:
        if produce.get_attribute('class') == 'product unlocked enabled':
            produce.click()
    # click cookie
    cookie_clicker.click()
    # Check if 5 mins have passed
    if time.time() > start + PERIOD_OF_TIME:
        driver.close()
        break
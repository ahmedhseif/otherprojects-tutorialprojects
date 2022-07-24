from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Development\\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&"
           "geoId=106155005&keywords=Python%20developer&location=Egypt")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
# NICE!! Wait for the next page to load.
time.sleep(2)

email = driver.find_element(By.NAME, "session_key")
email.send_keys("EMAIL")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("PASS")
sign_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
sign_in.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()
number = driver.find_element(By.NAME, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2959465065,"
                                      "46784051,phoneNumber~nationalNumber)")
if number.text == "":
    number.send_keys("123456789")

#Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
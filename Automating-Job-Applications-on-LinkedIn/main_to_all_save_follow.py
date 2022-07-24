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

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
listing_no = len(all_listings)
for index in range(listing_no):
    all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    listing = all_listings[index]
    print("called")
    listing.click()
    time.sleep(2)
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save.click()

    company = driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__company-name")
    company.click()
    time.sleep(5)
    follow = driver.find_element(By.CLASS_NAME, "follow")
    follow.click()
    driver.back()
    time.sleep(2)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("123456789")

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

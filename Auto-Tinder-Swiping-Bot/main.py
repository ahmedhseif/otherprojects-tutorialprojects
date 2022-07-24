from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

FB_EMAIL = "YOUR EMAIL"
FB_PASSWORD = "YOUR PASSWORD"

chrome_driver_path = "C:\\Development\\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")

sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]'
                                      '/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
sleep(2)
login_with_fb = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_with_fb.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(FB_EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(FB_PASSWORD)
sleep(2)
login_fb_button = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login_fb_button.click()

sleep(5)
driver.switch_to.window(base_window)
print(driver.title)
sleep(2)

location = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[1]')
location.click()
notification = driver.find_element(By.XPATH, '//*[@id="t492665908"]/div/div/div/div/div[3]/button[2]')
notification.click()
cookies = driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

sleep(5)

for n in range(100):

    # one sec delay between each
    sleep(5)

    try:
        print("called")
        dislike = driver.find_element(By.XPATH, '//*[@id="t-2073920312"]/div/div[1]/div/'
                                                'main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()

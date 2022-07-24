from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep

IG_NAME = "YOUR NAME"
IG_PASS = "YOUR PASS"
SIMILAR_ACCOUNT = "cristiano"
chrome_drive_path = "C:\\Development\\chromedriver.exe"

class InstaFollower:
    # A class to follow others on a popular account follower list.
    def __init__(self, driver_path):
        service = ChromeService(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        enter_user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        enter_user.send_keys(IG_NAME)
        sleep(2)
        enter_pass = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_pass.send_keys(IG_PASS)
        sleep(2)
        enter_pass.send_keys(Keys.ENTER)
        sleep(3)
        not_now = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers_list = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/'
                                                            'section/ul/li[2]/a')
        followers_list.click()
        sleep(2)

    def follow(self):
        follow_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.PZuss button')
        for element in follow_button_list:
            try:
                element.click()
                sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower(chrome_drive_path)
bot.login()
bot.find_followers()
bot.follow()

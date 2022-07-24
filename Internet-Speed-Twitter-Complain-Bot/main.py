from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep

TWITTER_EMAIL = "EMAIL"
TWITTER_USER = "USER"
TWITTER_PASS = "PASS"
PROMISED_UP = 2
PROMISED_DOWN = 20
chrome_driver_path = "C:\\Development\\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        service = ChromeService(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()

        sleep(60)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]').text


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        sleep(1)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        sleep(2)
        input_email = self.driver.find_element(By.CSS_SELECTOR, '.css-901oao input')
        input_email.send_keys(TWITTER_EMAIL)
        input_email.send_keys(Keys.ENTER)
        sleep(2)
        input_user = self.driver.find_element(By.CSS_SELECTOR, '.css-901oao input')
        input_user.send_keys(TWITTER_USER)
        input_user.send_keys(Keys.ENTER)
        sleep(2)
        input_pass = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pass.send_keys(TWITTER_PASS)
        input_pass.send_keys(Keys.ENTER)
        sleep(2)
        post_msg = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        post_msg.send_keys(tweet)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        post.click()
        sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()


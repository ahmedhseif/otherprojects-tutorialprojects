import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
             "usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-" \
             "122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22is" \
             "MapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22" \
             "value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%" \
             "2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22v" \
             "alue%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%" \
             "22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%" \
             "3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeJ9Qi-PTnUe33RhXl5Itr3BCr0Caz3WKp1_pRfEyFyI9httQ/viewform?usp=sf_link"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}
CHROME_DRIVE_PATH = "C:\\Development\\chromedriver.exe"


class JobAutomation:
    def __init__(self):
        response = requests.get(ZILLOW_URL, headers=HEADERS)
        website = response.content
        self.soup = BeautifulSoup(website, "lxml")
        service = ChromeService(executable_path=CHROME_DRIVE_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.price_list = []
        self.location_list = []
        self.link_list = []

    def get_data(self):
        price_list_htmls = self.soup.find_all(class_="list-card-price")
        self.price_list = [price.text for price in price_list_htmls]
        location_htmls = self.soup.find_all(class_="list-card-addr")
        self.location_list = [location.text for location in location_htmls]
        link_list_htmls = self.soup.find_all(class_="list-card-img")
        self.link_list = [link.get("href") for link in link_list_htmls]
        self.link_list.pop()
        for n in range(len(self.link_list)):
            if "https" not in self.link_list[n]:
                self.link_list[n] = "https://www.zillow.com" + self.link_list[n]

    def into_form(self):
        for n in range(len(self.link_list)):
            self.driver.get(FORMS_URL)
            address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(self.location_list[n])
            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.price_list[n])
            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(self.link_list[n])
            button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            button.click()
            sleep(1)


bot = JobAutomation()
bot.get_data()
bot.into_form()
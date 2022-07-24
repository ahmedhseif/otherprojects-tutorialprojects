import requests
from bs4 import BeautifulSoup
import smtplib

LINK = "https://www.amazon.com/dp/B07KJXZX94/ref=cm_sw_em_r_mt_dp_3SKR262K9P33HB0B1AQG"
MY_EMAIL = "YOUR EMAIL"
MY_PASS = "YOUR PASSWORD"
BUY_PRICE = 550

HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
}

response = requests.get(LINK, headers=HEADERS)
website = response.content

soup = BeautifulSoup(website, "lxml")
price_tag = soup.find(class_="a-size-medium a-color-price", id="price_inside_buybox")
price = float(price_tag.get_text().split("$")[1].strip())
title = soup.find(id="productTitle").get_text().strip()
print(title)
print(price)

if price < BUY_PRICE:
    message = f"{title} is now ${price}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ahmedseifpython@outlook.com", msg=f"Subject:Amazon Price Alert!\n\n{message}\n{LINK}")

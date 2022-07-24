from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Initiating a Link
chrome_driver_path = "C:\\Development\\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# 2. Get cookie ID to click on & set time
# english = driver.find_element(By.ID, "langSelect-EN")
cookie = driver.find_element(By.ID, "bigCookie")
timeout = time.time() + 5
five_min = time.time() + 60

while True:
    # time.sleep(10000)
    # english.click()
    time.sleep(10000)
    cookie.click()


    # 3. Every 5 seconds do this:
    if time.time() > timeout:
        timeout = time.time() + 5

        wallet_id = driver.find_element(By.ID, "cookies")
        wallet = int(wallet_id.text.split()[0].replace(",", ""))
        products_ids = driver.find_elements(By.CSS_SELECTOR, ".unlocked .price")
        products_all = [int(item.text.replace(",", "")) for item in products_ids]
        products_av = [item for item in products_all if item < wallet]

        print(products_av)

        if wallet > max(products_av):
            item_buy = driver.find_elements(By.CSS_SELECTOR, ".unlocked .price")
            item_list = [item for item in products_ids if int(item.text.replace(",", "")) == max(products_av)]
            chosen = item_list[0]
            chosen = chosen.get_attribute("id").replace("Price", "")
            winner = driver.find_element(By.XPATH, f'//*[@id="{chosen}"]')
            winner.click()
            if time.time() > five_min:
                cookie_per_s = driver.find_element(By.CSS_SELECTOR, "#cookies div").text
                c_s_number = cookie_per_s.split(": ")[1]
                print(f"cookies/second = {c_s_number}")
                break












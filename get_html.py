from os import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# url
url = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/"

# user-agent
user_agent = "Mozilla/5.0 \
    (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/110.0.0.0 \
    Safari/537.36"

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--ignore-certificate-errors-spki-list')

# driver
driver_path = path.join(f"{path.abspath('')}", "chromedriver.exe")
driver = webdriver.Chrome(
    executable_path=driver_path,
    options=options
)
driver.set_window_size(1920,1080)

def get_html():
    try:
        driver.get(url)
        time.sleep(5)
        city = driver.find_element(by=By.CLASS_NAME, value="city-select__text_BTU")
        city.click()
        time.sleep(2)

        input_city = driver.find_element(by=By.CLASS_NAME, value="base-ui-input-search__input_YOW")
        input_city.clear()
        input_city.send_keys("Санкт-Петербург")
        time.sleep(2)
        input_city.send_keys(Keys.ENTER)
        time.sleep(5)
        
        html = driver.find_element(by=By.TAG_NAME, value='html')
        for i in range(8):
            html.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
        with open("smartphones.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
import time
import csv
import json
from bs4 import BeautifulSoup


# Список инфы о смартфонах
smartphones_data = []

# Дата парсинга
date_time = time.ctime()

def parse_it():
    # Открываем сохранённую страничку со смартфонами
    with open("smartphones.html", encoding="utf-8") as file:
        src = file.read()

    # Сохраняем объект BS
    soup = BeautifulSoup(src, 'lxml')
    products = soup.find_all("div", class_="catalog-product ui-button-widget")

    # Создаём csv файл и размечаем поля
    with open("smartphones_data1.csv", "w", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        "Наименование",
                        "Цена",
                        "Дата",
                        "Ссылка на товар"
                    )
                )

    # Собираем информацию о продукте
    for product in products:
        product_name = product.find(
            'a', class_='catalog-product__name ui-link ui-link_black'
            ).find('span').text
        product_url = 'https://www.dns-shop.ru' + product.find(
            'a', class_='catalog-product__name ui-link ui-link_black'
            ).get('href')
        product_price = product.find('div', class_='product-buy__price').text
        product_data = {
            "product_name" : product_name,
            "product_price" : product_price,
            "date_time" : date_time,
            "product_url" : product_url        
        }
        smartphones_data.append(product_data)

        # Добавляем инфо о продукте в csv
        with open(f"smartphones_data1.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        product_name,
                        product_price,
                        date_time,
                        product_url
                    )
                )

    # Собираем всё в json формате
    with open('smartphones_data.json', 'w', encoding="utf-8") as json_file:
        json.dump(smartphones_data, json_file, indent=4, ensure_ascii=False)
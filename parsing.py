from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('https://www.detmir.ru/catalog/index/name/lego/')
except:
    pass

driver.implicitly_wait(5)

pages = 20

total = []

if len(total) <= 500:
    for page in range(1, pages):
        url = 'https://www.detmir.ru/catalog/index/name/lego/page/' + str(page) + '/'
        driver.get(url)
        city_name = driver.find_element(By.CLASS_NAME, 'lV').text
        products_items = len(driver.find_elements(By.XPATH, "//div[contains(@class,'vW wb')]"))

        for i in range(products_items):
            try:
                products = driver.find_elements(By.XPATH, "//div[contains(@class,'vW wb')]")
                for product in products:
                    product_name = product.find_element(By.TAG_NAME, 'p').text
                    product_price = product.find_element(By.CLASS_NAME, 'RA').text
                    promo_price = product.find_element(By.CLASS_NAME, 'RB').text
                    new = ((product_name, product_price, city_name, promo_price))

                    if new not in total:
                        total.append(new)
                    else:
                        pass

            except:
                pass

        df = pd.DataFrame(total, columns=['Название', 'Цена', 'Город', 'Промо цена'])
        df.to_csv('lego.csv', index=False)

        df = pd.read_csv('lego.csv')

else:
    driver.close()

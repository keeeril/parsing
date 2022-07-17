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
# element = driver.find_element_by_id("app-container")

pages = 10

total = []

for page in range(1, pages):
    url = 'https://www.detmir.ru/catalog/index/name/lego/page/' + str(page) + '/'
    driver.get(url)
    products_items = len(driver.find_elements(By.XPATH, "//div[contains(@class,'vW wb')]"))
    for i in range(products_items):
        products = driver.find_elements(By.XPATH, "//div[contains(@class,'vW wb')]")
        for product in products:
            product_name = product.find_element(By.TAG_NAME, 'p').text
            product_price = product.find_element(By.CLASS_NAME, 'RA').text
            new = ((product_name, product_price))
            total.append(new)
    df = pd.DataFrame(total, columns=['Название', 'Цена'])
    df.to_csv('lego.csv', index=False)

    df = pd.read_csv('lego.csv')
    print(df)


# for page in range(pages):
#     pages += 1
#     url = 'https://www.detmir.ru/catalog/index/name/lego/page/' + str(page) + '/'
#     driver.get(url)
#     products_items = driver.find_elements(By.XPATH, "//div[contains(@class,'vW wb')]")
#     for i in products_items:
#         product_name = i.find_element(By.TAG_NAME, 'p').text
#         product_price = i.find_element(By.CLASS_NAME, 'RA').text
#         new = ((product_name, product_price))
#         total.append(new)
#     df = pd.DataFrame(total, columns=['Название', 'Цена'])
#     df.to_csv('lego.csv', index=False)
#
#     df = pd.read_csv('lego.csv')
#     print(df)

# *********if you are using VScode then please run line 2 and 3 in your terminal
# python3 -m venv venv
# source venv/bin/activate
# pip install selenium
# pip install webdriver_manager
# For those who cannot use chrome driver please use Firefox instead!!!!
# This version is using chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    chrome_options=chrome_options
)
i = 1
records = []
while True:
    if i==1:
        url= f"https://hk.iherb.com/search?kw=%E9%8E%82"
    else:
        url = f"https://hk.iherb.com/search?kw=%E9%8E%82&p={i}"
    driver.get (url)

    cells = driver.find_elements(By.CSS_SELECTOR, ".absolute-link.product-link")
    for cell in cells:
        print(cell.text)

    i+= 1
    if i == 3:
        driver.close()

    

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".absolute-link product-link"))
    # )


    for cell in cells:
        try:
            product_name = cell.get_attribute("title")
            product_id = cell.get_attribute("data-ga-product-id")
            discount_price = cell.get_attribute("data-ga-discount-price")
            print(product_name)
            print(product_id)
            print(discount_price)
            record = [
                product_name,
                product_id,
                discount_price,
            ]
            records.append(record)
            
            # print(len(records))
            # if len(records) > 70:
            #     break
        except:
            pass

df = pd.DataFrame(records, columns=["name", "product id", "price"])
df.to_csv("info_list.csv", index=False)
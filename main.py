# import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

# url = "https://www.bhinneka.com"
# r = requests.get(url, timeout=(15, 15))
# soup = BeautifulSoup(r.content, "html.parser")

# Read html from assets folder
path = (
    os.getcwd()
    + "\\assets\\html\\Bhinneka_ Solusi Praktis Untuk Kebutuhan Bisnis Terlengkap.html"
)
f = open(path, "r")
soup = BeautifulSoup(f, "html.parser")
f.close()

list = soup.find_all("div", attrs={"class": "price"})
# Scrap all price to list
price_list = []
for s in list:
    price = s.contents[0].replace("Rp ", "").replace(".", "")
    price_list.append(int(price))

# Scrap all name to list
list = soup.find_all("p", class_="css-194yrqz")
name_list = []
for d in list:
    name_list.append(d.contents[0])

# Convert list to csv
file_name = "ProductList3.csv"
product_list = {"Name": name_list, "Price": price_list}
df = pd.DataFrame(product_list)
df.to_csv(f"assets/csv/{file_name}")

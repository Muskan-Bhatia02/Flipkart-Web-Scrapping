import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(14, 30):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    for i in names:
        name1 = i.text
        Product_name.append(name1)

        # print(Product_name)
        # print(len(Product_name))

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")

    for i in prices:
        name2 = i.text
        Prices.append(name2)

        # print(Prices)
        # print(len(Prices))

    desc = box.find_all("ul", class_="_1xgFaf")

    for i in desc:
        name3 = i.text
        Description.append(name3)

        # print(Description)
        # print(len(Description))

    reviews = box.find_all("div", class_="_3LWZlK")

    for i in reviews:
        name4 = i.text
        if name4 == "":
            name4 = "0"
        Reviews.append(name4)

# print(Reviews)
# print(len(Reviews))


df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
print(df)

df.to_csv("Flipkart_Web_Scrapping.csv")
df.to_csv(("D:/Web Scrapping/Flipkart Web Scrapping/Flipkart_Web_Scrapping.csv"))

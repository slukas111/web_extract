import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/IPhone"
result = requests.get(url).text

phone_dict = {}

soup = BeautifulSoup(result, "lxml")
table = soup.find("table", class_="wikitable")
# get all the rows, exccept the first one
rows = table.find_all("tr")[1::1]


for row in rows:
    data = row.find_all(["th", "td"])
    try:
        # grab a tag, split on the last, get name of phone version
        iphone_version = data[0].a.text.split("/")[-1]
        iphone_version = "".join(i for i in iphone_version if i.isdigit())

        price_text = data[8]
        price = (
            price_text.text.split("/")[-1]
            .split("*")[-1]
            .replace("$", "")
            .replace("\n", "")
        )
        # cleaning data and removing unfinished input. store variable of interger.
        price = int(price)
        version = int(iphone_version)
        if version < 2 and price < 1:
            continue
        # dictionary of iphones
        phone_dict[version] = int(price)
    except:
        pass


csv = open("iphone_price.csv", "a")
csv.write("version,price\n")

for key in phone_dict:
    csv.write(f"{key},{phone_dict[key]}\n")

csv.close()
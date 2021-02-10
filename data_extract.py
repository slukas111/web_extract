import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/IPhone'
result = requests.get(url).text 
# print(result)

soup = BeautifulSoup(result, 'lxml')
table = soup.find('table', class_ = 'wikitable')
#get all the rows, exccept the first one
rows = table.find_all('tr')[1::1]
print(rows)

for row in rows:
    data = row.find_all(['th', 'td'])
    try:

        print(data[0].a.text)
    except:
        pass
import requests

url = 'https://en.wikipedia.org/wiki/IPhone'
result = requests.get(url).text 
print(result)
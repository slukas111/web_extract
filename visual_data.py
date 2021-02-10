import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iphone_price.csv")
print(data['price'])

plt.scatter(data['version'], data['price'])
plt.show()
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("iphone_price.csv")

model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(f"version iphone 20 price will be: {model.predict([[20]])}")


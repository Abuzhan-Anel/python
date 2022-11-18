import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BigmacPrice.csv')
x=df[df["date"] == "2000-04-01"]["name"]
y=df[df["date"] == "2000-04-01"]["dollar_price"]
plt.figure(figsize=(12, 5))
plt.barh(x,y)
plt.xlabel("2000-04-01")
plt.ylabel("Name")
plt.title("Prices")
#plt.xticks([])
#plt.yticks([])
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Q10\iris.csv')
# df = pd.read_csv('iris.csv')

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

df.plot()
plt.show()
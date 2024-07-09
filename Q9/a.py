import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Q9\iris.csv')
# df = pd.read_csv('iris.csv')

df.plot()
plt.show()

df.plot(kind = "scatter", x = 'sepal.length', y = 'petal.length')
plt.show()

x,y = df['petal.length'], df['sepal.length']
plt.scatter(x,y,c='red')

x,y = df['petal.width'], df['sepal.width']
plt.scatter(x,y,c='green')
plt.xlabel('Petal')
plt.ylabel('Sepal')
plt.show()

df['sepal.length'].plot(kind='hist')
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show() 

# Develop a python program read a dataset and perform the following using 
# Pandas  
# • Visualize the dataset using plot (). 
# • Draw the Scatter plot for the dataset on any column. 
# • Display the scatter plot with different colors. 
# • Draw the Histogram for the dataset on any column. 
# 2 1,2,3,5 

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Q9\iris.csv')
# df = pd.read_csv('iris.csv')

df.plot()
plt.show()

df.plot(kind="scatter",x='sepal.length',y='petal.length')
plt.show()

x,y=df['petal.length'],df['sepal.length']
plt.scatter(x,y,c='red')
x,y=df['petal.width'],df['sepal.width']
plt.scatter(x,y,c='green')
plt.show()

df['sepal.length'].plot(kind='hist')
plt.show() 

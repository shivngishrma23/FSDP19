import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('automobile.csv')

print(df)
# to remove mising value from price columns
df['price'] = df['price'].fillna(df['price'].mean())
 
a = np.array(df['price'])

print(df['price'].max())

print(df['price'].min())

print(df['price'].mean())


print(df['price'].std())
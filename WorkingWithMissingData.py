import pandas as pd
import numpy as np

data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
print(data)

print(data.isnull())
print(data.isnull().sum())
print(data.dropna())
print(data.replace(np.nan,"NA"))
print(data.fillna(method = "bfill"))
print(data.fillna(method = "ffill"))

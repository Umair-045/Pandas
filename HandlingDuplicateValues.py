import pandas as pd

data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
print(data.duplicated())
print(data.duplicated().sum())

print(data.drop_duplicates())
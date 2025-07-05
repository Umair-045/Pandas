import pandas as pd

data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
# print(data)

# print(data.head(2))   # it will give first 2 lines
# print(data.tail(2))   # it will give last 2 lines


print(data.info())
print(data.describe())
print(data.isnull().sum())

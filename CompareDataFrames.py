import pandas as pd

dict = {"Fruits":["mangoes","apples","banana","papaya"],
        "price":[100,150,50,35],
        "quantity":[15,10,10,3]}

df1 = pd.DataFrame(dict)
print(df1)

df2 = df1.copy()

df2.loc[0,"price"]=120
df2.loc[1,"price"]=175
df2.loc[3,"price"]=30

df2.loc[0,"quantity"]=12
df2.loc[1,"quantity"]=15
df2.loc[3,"quantity"]=5

print(df2)
print(df1.compare(df2))
print(df1.compare(df2,align_axis=0))
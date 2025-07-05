import pandas as pd
data1 = {"Emp ID":["E01","E02","E03","E04","E05","E06"],
        "Names":["Umair","Uzair","Israr","Zeeshan","Shakir","Alam"],
        "Age":[18,19,25,18,20,17]}

data2 ={"Emp ID":["E01","E02","E03","E04","E05","E06"],
        "salary":[1000,2000,3000,4000,5000,6000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print()
print(df2)

print(pd.merge(df1,df2, on = "Emp ID"))
print(pd.merge(left = df1, right = df2, on = "Emp ID",how = "left"))
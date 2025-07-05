import pandas as pd

# data = pd.read_excel("C:/Users/Ahmed/Desktop/Info.xlsx")
# print(data)
#
# data.loc[(data["Age"]>18),"Eligible or Not Eligible"]="Eligible"
# data.loc[(data["Age"]<=18),"Eligible or Not Eligible"]="Not Eligible"
#
# print(data)




data = {"Months" : ["January", "February","March","April","May","June"]}

df = pd.DataFrame(data)
print(df)

def extract (value):
    return value[0:3]

df["Short_Months"]= df["Months"].map(extract)
print(df)
import pandas as pd

data = {"keys": ["k1", "k2", "k1", "k2"],
        "names": ["john", "ben", "david", "peter"],
        "houses": ["red", "blue", "green", "blue"],
        "Grades":["3rd","4th","7th","8th"]}

df = pd.DataFrame.from_dict(data)
print(df)

print(df.pivot(index="keys",columns="names",values=["houses","Grades"]))

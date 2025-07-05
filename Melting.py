import pandas as pd

data = {
        "names": ["john", "ben", "david", "peter"],
        "houses": ["red", "blue", "green", "blue"],
        "Grades":["3rd","4th","7th","8th"]}

df = pd.DataFrame(data)
print(df)

print(pd.melt(df, id_vars=["names"],value_vars=["houses"]))
print(pd.melt(df, id_vars=["names"],value_vars=["houses", "Grades"],var_name="Houses&Grades",value_name="value"))
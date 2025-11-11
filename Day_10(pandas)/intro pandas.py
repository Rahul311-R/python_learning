import pandas as pd
data = {
    "name":["rahul","akash","kishore"],
    "class":["B","A","C"]
}
p = pd.DataFrame(data)
print(p)
print(p.head())
print(p.head(2))
print(p.tail())
print(p.info())
print(p.describe())
print(p.shape)
print(p.columns)
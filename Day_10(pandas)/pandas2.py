import pandas as pd
d = pd.read_csv("data.csv")
a = d[(d["latitude"]<10000) & (d["country"]=="India")]
print(len(a))

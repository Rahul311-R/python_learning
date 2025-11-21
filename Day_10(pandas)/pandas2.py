import pandas as pd
d = pd.read_csv("data.csv")
a = d[(d["latitude"]<10000) & (d["country"]=="India")]
#print(len(a))
#print(d.mean(numeric_only=True))
#print(d.sum(numeric_only=True))
#print(d.min(numeric_only=True))
print(d.max(numeric_only=True))
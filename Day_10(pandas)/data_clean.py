import pandas as pd

d = pd.read_csv("data.csv")

#to drop a column
#d = d.drop(columns=["country","date"])

#handle missing data
#d = d.dropna(subset = "date")
#d = d.fillna({"recovery_days":"not"})

#fix inconsistence value
#d["country"] = d["country"].replace("India","INDIA")

#standardize form
#d["country"] = d["country"].str.lower()

#fix datatype
#df["Legendary"] = df["Legendary"].astype (bool)

print(d)
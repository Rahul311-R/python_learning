import pandas as pd
r = pd.read_csv("data.csv")
#print(r.isnull().sum())
#print(r.dropna(inplace=True))
#r["recovery_days"].fillna(0, inplace=True)       # fill with 0
# r["country"].fillna("Unknown", inplace=True)     # fill with text
#r.drop_duplicates(inplace=True)
#r["recovery_days"] = r["recovery_days"].astype(int)       #Change data types (if needed)
#r.to_csv("cleaned_data.csv", index=False)

import pandas as pd
r = pd.read_csv("data.csv")
#print(r.country)
#print(r[["date","country"]])
#print(r.columns)
#print(r.iloc[19:35])
#print(r[r["country"]=="India"])
#print(r[(r["country"]=="India")&(r["recovery_days"]>50)])
print(r["date"].unique())     # unique values in class column
print(r["country"].value_counts())  # how many of each


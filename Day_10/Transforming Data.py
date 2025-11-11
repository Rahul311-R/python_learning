import pandas as pd
r = pd.read_csv("data.csv")
#r.sort_values(by="country",ascending=False ,inplace=True)  #descending order
#r.sort_values(by=["country", "recovery_days"], ascending=[True, False], inplace=True) #Sort by multiple columns
#print(r.groupby("country")["recovery_days"].mean())
#print(r.groupby("country")["date"].count())
#print(r.groupby("country")["recovery_days"].agg(["mean", "max", "min"]))


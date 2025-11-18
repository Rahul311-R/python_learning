import pandas as pd
df = pd.DataFrame("data.csv")
region_sales = df.groupby("region")["sales"].sum()
print(region_sales)

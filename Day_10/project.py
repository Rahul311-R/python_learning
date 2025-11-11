import pandas as pd

# 1. Load data
r = pd.read_csv("data.csv")

# 2. Clean
r.dropna(inplace=True)
r.drop_duplicates(inplace=True)

# 3. Transform
r["status"] = r["recovery_days"].apply(lambda x: "Long" if x > 50 else "Short")

# 4. Group & sort
summary = r.groupby("country")["recovery_days"].mean().sort_values(ascending=False)

# 5. Save
summary.to_csv("report.csv")

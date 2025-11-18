import pandas as pd
import matplotlib.pyplot as plt

data = {
    "region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "sales":  [1200, 700, 950, 400, 1500, 900, 1100, 500],
    "profit": [300, 150, 200, 50, 400, 180, 220, 60]
}

df = pd.DataFrame(data)

print(df)
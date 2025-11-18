# day11_step3_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

# --- 1) Create the DataFrame (we reuse the same sample data from earlier) ---
data = {
    "region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "sales":  [1200, 700, 950, 400, 1500, 900, 1100, 500],
    "profit": [300,  150, 200,  50, 400,  180, 220,  60]
}
df = pd.DataFrame(data)

# --- 2) Aggregate: total sales per region (this is what we'll plot) ---
region_sales = df.groupby("region")["sales"].sum()   # Series indexed by region
# region_sales looks like: East:2050, North:2700, South:1600, West:900

# --- 3) BAR CHART: Total sales by region ---
plt.figure(figsize=(8,5))                             # set figure size (width, height) in inches
plt.bar(region_sales.index, region_sales.values)      # draw bars; x labels are region names
plt.title("Total Sales by Region")                    # chart title
plt.xlabel("Region")                                  # x-axis label
plt.ylabel("Sales ($)")                               # y-axis label
plt.grid(True, axis='y', linestyle='--', alpha=0.5)   # horizontal grid lines to read values easily

# Annotate bars with numeric values (makes chart easier to read)
for i, v in enumerate(region_sales.values):
    plt.text(i, v + max(region_sales.values)*0.01,    # x position (i), y a little above bar top
             str(v), ha='center', va='bottom', fontsize=9)

plt.tight_layout()    # avoid clipping labels/title
plt.show()            # display the plot

# --- 4) LINE CHART: sales "trend" across regions (regions are categorical here) ---
plt.figure(figsize=(8,4))
plt.plot(region_sales.index, region_sales.values, marker='o')  # line with markers at data points
plt.title("Sales by Region — Line View")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 5) SCATTER PLOT: show distribution of totals across regions ---
plt.figure(figsize=(6,4))
plt.scatter(region_sales.index, region_sales.values)           # one point per region
plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 6) SUBPLOTS: bar + line side-by-side for quick comparison ---
fig, axes = plt.subplots(1, 2, figsize=(12,4))  # 1 row, 2 columns

# left: bar chart on axes[0]
axes[0].bar(region_sales.index, region_sales.values)
axes[0].set_title("Bar: Total Sales")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Sales ($)")
axes[0].grid(axis='y', linestyle='--', alpha=0.4)

# right: line chart on axes[1]
axes[1].plot(region_sales.index, region_sales.values, marker='o')
axes[1].set_title("Line: Sales (same data)")
axes[1].set_xlabel("Region")
axes[1].set_ylabel("Sales ($)")
axes[1].grid(True)

plt.suptitle("Comparison: Bar vs Line")  # overall title for the subplot group
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # leave room for suptitle
plt.show()

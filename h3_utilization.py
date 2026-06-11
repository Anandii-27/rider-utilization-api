import pandas as pd
import h3

# Read rider data
df = pd.read_csv("riders.csv")

# Read cluster names
mapping_df = pd.read_csv("cluster_name.csv")

# Merge cluster names into rider data
df = df.merge(
    mapping_df,
    left_on="pickup_cluster",
    right_on="parent_geozone_id",
    how="left"
)

# Create H3 hex from pickup latitude and longitude
df["pickup_h3"] = df.apply(
    lambda row: h3.latlng_to_cell(
        row["pickup_latitude"],
        row["pickup_longitude"],
        6
    ),
    axis=1
)

# Calculate utilization by H3 and cluster
result = (
    df.groupby(["pickup_h3", "geozone_name"])
      .agg(
          busy_riders=("occupied_flag", lambda x: (x == 1).sum()),
          free_riders=("occupied_flag", lambda x: (x == 0).sum())
      )
      .reset_index()
)

# Total riders
result["total_riders"] = (
    result["busy_riders"] + result["free_riders"]
)

# Utilization percentage
result["utilization_percentage"] = (
    result["busy_riders"] / result["total_riders"] * 100
).round(2)

# Sort by utilization
result = result.sort_values(
    by="utilization_percentage",
    ascending=False
)

# Display full table
print(result.to_string(index=False))

# Summary
print("\nTotal rows in CSV:", len(df))
print("Unique H3 cells:", df["pickup_h3"].nunique())
print("Rows in result table:", len(result))
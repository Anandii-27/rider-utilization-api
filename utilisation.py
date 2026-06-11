import pandas as pd

# Read CSV file
df = pd.read_csv("riders.csv")

# Count busy and free riders
busy = (df["occupied_flag"] == 1).sum()
free = (df["occupied_flag"] == 0).sum()

# Total riders
total = busy + free

# Utilization percentage
utilization = (busy / total) * 100 if total > 0 else 0

# Print results
print(f"Busy Riders: {busy}")
print(f"Free Riders: {free}")
print(f"Total Riders: {total}")
print(f"Utilization: {utilization:.2f}%")
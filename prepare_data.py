import pandas as pd

# Load dataset
df = pd.read_csv("intern_data.csv")

# Create KPIs
df["Task_Completion_Rate"] = (df["completed_tasks"] / df["total_tasks"]) * 100
df["Attendance_Percentage"] = (df["days_present"] / df["total_days"]) * 100

# Save new dataset
df.to_csv("final_dataset.csv", index=False)

print("Final dataset created successfully!")
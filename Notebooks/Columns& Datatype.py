columns = ["Intern_ID", "Name", "Department", "Tasks_Assigned", "Tasks_Completed",
           "Attendance", "Feedback", "Submission_Timeliness", "Week"]
data_types = ["int", "string", "string", "int", "int", "float", "float", "float", "string"]

for col, dtype in zip(columns, data_types):
    print(f"{col} -> {dtype}")
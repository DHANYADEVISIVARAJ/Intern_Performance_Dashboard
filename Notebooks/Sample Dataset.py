sample_data = {
    "Intern_ID": [101, 102, 103, 104, 105],
    "Name": ["Asha", "Ravi", "Arun", "Meena", "Kiran"],
    "Department": ["UI/UX", "Data Science", "Development", "UI/UX", "Data Science"],
    "Tasks_Assigned": [20, 21, 22, 23, 24],
    "Tasks_Completed": [20, 20, 20, 20, 20],
    "Attendance": [75, 76, 77, 78, 79],
    "Feedback": [3.5, 3.6, 3.7, 3.8, 3.9],
    "Submission_Timeliness": [65, 66, 67, 68, 69],
    "Week": ["Week1", "Week2", "Week3", "Week4", "Week5"]
}

df_sample = pd.DataFrame(sample_data)
df_sample
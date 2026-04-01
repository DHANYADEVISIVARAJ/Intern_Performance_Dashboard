                                         Intern Performance Analytics Dashboard
--Project Objective

The objective of this project is to analyze intern performance data and generate actionable insights through analytics and visualization.
The dashboard will help managers evaluate intern productivity, attendance, submission timeliness, and overall performance.

         Sprint 1 – Day 1: Dataset Planning
 #### Tasks Planned (SOD)
1.  Understand project requirements for the Intern Performance Analytics Dashboard
2. Identify required data fields:
     Intern details (ID, Name, Department)
     Task information (Tasks Assigned, Tasks Completed)
     Attendance
     Feedback / Ratings
     Submission Timeliness
     Week tracking
3. Design dataset structure (columns & data types)
4. Research similar datasets

  #### Tasks Completed (EOD)
1. Finalized dataset structure with following columns:
      Intern_ID
      Name
      Department
      Tasks_Assigned
      Tasks_Completed
      Attendance
      Feedback
      Submission_Timeliness
      Week
2. Designed dataset schema and column definitions
3. Prepared project folder structure
4. Documented dataset details in document.md

 #### Notes
    =>The dataset structure was designed based on typical intern performance metrics
    =>Columns were selected to support future analysis like productivity, attendance, and performance evaluation
    =>No real data was used; only planning and structure design were completed in this phase
    =>The defined structure will be used to generate synthetic data in the next step

       Sprint 1 – Day 2: Dataset Creation
   #### Tasks Planned (SOD)
1. Create synthetic dataset using Python
2. Generate realistic intern performance data
3. Calculate derived metrics (Completion Rate)
4. Save dataset in CSV format
5. Update notebook and README

    #### Tasks Completed (EOD)
1. Generated dataset with 100 records using Python
2. Created dataset with columns:
      Intern_ID
      Department
      Tasks_Assigned
      Tasks_Completed
      Hours_Worked
      Attendance
      Performance_Score
      Completion_Rate
3. Calculated Completion Rate using formula:
   Tasks_Completed / Tasks_Assigned × 100
4. Saved dataset as:
   dataset/intern_data.csv
5. Implemented dataset creation in:
   notebooks/data_preprocessing.ipynb
  #### Updated README with Day 2 progress
 UPDATED Folder Structure
Intern-Performance-Dashboard
│
├── README.md
├── dataset
│   └── intern_data.csv
├── notebooks
│   └── data_preprocessing.ipynb
├── document.md


# Notes

    =>The dataset is synthetically generated using Python for simulation purposes
    =>Completion Rate is a derived performance metric
    =>Data is structured for further analysis in upcoming sprints
    =>This dataset will be used for Data Cleaning and EDA in next steps



Day	Status
Day 1	----- Planning Done
Day 2	----- Dataset Created
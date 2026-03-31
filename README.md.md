&#x20;         **Intern Performance Analytics Dashboard**



**Project Objective**



&#x20;   The objective of this project is to analyze intern performance data and generate actionable insights through analytics and visualization.  

The dashboard will help managers evaluate intern productivity, attendance, submission timeliness, and overall performance.





**Sprint 1 – Day 1: Dataset Planning**



&#x20;**Tasks Planned (SOD)**

\- Understand project requirements for the Intern Performance Analytics Dashboard

\- Identify the required data fields:

&#x20; - Intern details (ID, Name, Department)

&#x20; - Task information (Tasks Assigned, Tasks Completed)

&#x20; - Attendance

&#x20; - Feedback / Ratings

&#x20; - Submission Timeliness

&#x20; - Week tracking

\- Design dataset structure (columns \& data types)

\- Research similar datasets for reference



&#x20;**Tasks Completed (EOD)**

\- Finalized dataset structure with 9 columns:

&#x20; - Intern\_ID

&#x20; - Name

&#x20; - Department

&#x20; - Tasks\_Assigned

&#x20; - Tasks\_Completed

&#x20; - Attendance

&#x20; - Feedback

&#x20; - Submission\_Timeliness

&#x20; - Week

\- Created sample dataset with 300+ records: \[sample\_dataset.csv]

\- Documented the purpose of each column: \[dataset\_documentation.md]







&#x20;**Folder Structure**



Intern-Performance-Dashboard

│

├── README.md

├── Dataset

│ └── sample\_dataset.csv

├── Notebooks

│ └── 01\_dataset\_planning.ipynb

└── Docs

└── dataset\_documentation.md



&#x20;**Notes**

\- The dataset contains sample intern data to simulate real-world performance tracking.

\- Feedback column currently stores numeric ratings (can be updated to text feedback later).

\- Attendance and Submission\_Timeliness are numeric values representing percentages or scores.

\- The dataset and documentation will be used as the foundation for future sprints.


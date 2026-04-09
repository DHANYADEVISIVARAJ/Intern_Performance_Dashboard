# Intern Performance Analytics Dashboard

---

##  Sprint 1 – Day 1: Dataset Planning

### **Tasks Planned (SOD)**

* Understand project requirements for the Intern Performance Analytics Dashboard
* Identify required data fields:

  * Intern details (ID, Name, Department)
  * Task information (Tasks Assigned, Tasks Completed)
  * Attendance
  * Feedback / Ratings
  * Submission Timeliness
  * Week tracking
* Design dataset structure (columns & data types)
* Research similar datasets

---

### **Tasks Completed (EOD)**

* Finalized dataset structure with columns:

  * Intern_ID
  * Name
  * Department
  * Tasks_Assigned
  * Tasks_Completed
  * Attendance
  * Feedback
  * Submission_Timeliness
  * Week

* Designed dataset schema and column definitions

* Prepared project folder structure

* Documented dataset details

---

### **Notes**

* Dataset structure is designed based on real-world intern performance metrics
* Focus is on tracking productivity, attendance, and performance
* This structure will be used to generate synthetic data in upcoming steps

---

### **Blockers**

* None

---

## 📅 Sprint 1 – Day 2: Dataset Creation

### **Tasks Planned (SOD)**

* Create synthetic dataset using Python
* Generate intern performance data
* Calculate derived metrics (Completion Rate)
* Save dataset in CSV format
* Update notebook and README

---

### **Tasks Completed (EOD)**

* Generated synthetic dataset using Python

* Created dataset with columns:

  * Intern_ID
  * Name
  * Department
  * Tasks_Assigned
  * Tasks_Completed
  * Hours_Worked
  * Attendance
  * Performance_Score
  * Completion_Rate

* Calculated Completion Rate as a performance metric

* Saved dataset as `intern_data.csv`

* Implemented dataset creation in notebook

* Updated README with Day 2 progress

* Successfully pushed project to GitHub

---

### **Notes**

* Dataset is synthetically generated using Python
* Random values simulate real-world intern performance
* Completion Rate is used as a key performance indicator

---

### **Blockers**

* None

---

## 📅 Sprint 1 – Day 3: Data Cleaning

### **Tasks Planned (SOD)**

* Load dataset into notebook
* Check for missing values
* Verify data types
* Remove duplicate records
* Validate data ranges
* Perform data cleaning
* Save cleaned dataset
* Update documentation

---

### **Tasks Completed (EOD)**

* Loaded dataset into notebook
* Checked for missing values
* Handled missing values in Name column
* Verified data types of all columns
* Removed duplicate records
* Validated Completion Rate values
* Saved cleaned dataset as `intern_data_cleaned.csv`
* Updated notebook and documentation
* Pushed updates to GitHub

---

### **Notes**

* Data cleaning ensures dataset quality and consistency
* Cleaned dataset will be used for analysis and visualization
* Prepared data for next stage (EDA and dashboard development)

---

### **Blockers**

* None

---

## 📅 Sprint 1 – Day 4: Exploratory Data Analysis (EDA)

### **Tasks Planned (SOD)**

* Load cleaned dataset (`intern_data_cleaned.csv`) into notebook
* Perform exploratory data analysis using visualizations
* Analyze relationships between key variables
* Identify trends and patterns in intern performance
* Generate charts such as scatter plots, bar charts, histograms, and heatmaps
* Derive meaningful insights from the dataset
* Update notebook and documentation
* Push changes to GitHub

---

### **Tasks Completed (EOD)**

* Loaded cleaned dataset into notebook
* Performed data visualization using matplotlib and seaborn
* Created scatter plot for Tasks Assigned vs Tasks Completed
* Analyzed department-wise performance using bar chart
* Visualized attendance distribution using histogram
* Examined completion rate distribution
* Generated correlation heatmap to understand relationships between variables
* Derived basic insights from visual analysis
* Updated notebook with EDA steps
* Updated documentation and pushed changes to GitHub

---

### **Notes**

* EDA helps in understanding data patterns and relationships
* Visualizations make it easier to interpret performance trends
* Correlation analysis helps identify key factors affecting performance
* Insights generated here will be used for KPI definition and dashboard creation

---

### **Blockers**

* None

---



## 📅 Sprint 1 – Day 5: KPI Identification & Dashboard Planning

### **Tasks Planned (SOD)**

* Load cleaned dataset (`intern_data_cleaned.csv`) into notebook
* Identify key performance indicators (KPIs) for intern evaluation
* Calculate overall performance metrics using dataset
* Analyze department-wise KPIs
* Plan structure and components of the dashboard
* Identify key insights to be displayed
* Update notebook and documentation
* Push updates to GitHub

---

### **Tasks Completed (EOD)**

* Loaded cleaned dataset into notebook

* Defined key performance indicators (KPIs):

  * Total Tasks Assigned
  * Total Tasks Completed
  * Average Completion Rate
  * Average Performance Score
  * Average Attendance

* Calculated overall KPI metrics using Python

* Performed department-wise KPI analysis

* Planned dashboard structure including KPI cards, charts, and insights

* Identified key insights for performance tracking

* Updated notebook with KPI calculations and planning

* Updated documentation and pushed changes to GitHub

---

### **Notes**

* KPIs help measure intern performance effectively
* Completion Rate and Performance Score are key indicators
* Dashboard planning ensures clear visualization of insights
* These KPIs will be used in dashboard development (next sprint)

---

### **Blockers**

* None

---


## 📅 Sprint 2 – Day 1: Exploratory Data Analysis (EDA)
🔹 Start of Day (SOD)

### Tasks Planned:

Load cleaned dataset (intern_data_cleaned.csv)
Perform basic statistical analysis
Create visualizations (scatter, bar, histogram, heatmap)
Identify trends and patterns
Document insights in notebook
Update documentation and push to GitHub
🔹 End of Day (EOD)

### Tasks Completed:

Loaded cleaned dataset into notebook
Performed statistical analysis using describe()
Created visualizations:
Scatter plot (Tasks Assigned vs Completed)
Bar chart (Department-wise Performance)
Histogram (Attendance Distribution)
Heatmap (Correlation analysis)
Identified patterns and relationships in data
Documented insights in notebook
Updated EDA notebook
Pushed changes to GitHub
🔹 Notes
EDA helped in understanding data distribution and relationships
Attendance and task completion impact performance
Visualization makes data easy to interpret
Heatmap showed correlation between key variables
🔹 Any Blockers
None

## 📅 Sprint 2 – Day 2: Advanced Data Analysis
🔹 Start of Day (SOD)

### Tasks Planned:

Perform advanced analysis using groupby()
Analyze performance based on:
Department
Attendance
Completion Rate
Identify top and low performing interns
Create additional visualizations (bar chart, boxplot)
Derive insights from grouped data
Document findings in notebook
Update document.md and push to GitHub
🔹 End of Day (EOD)

### Tasks Completed:

Loaded cleaned dataset into notebook
Performed department-wise performance analysis
Analyzed relationship between attendance and performance
Created attendance categories (Low, Medium, High)
Calculated Completion Rate for all interns
Performed department-wise completion rate analysis
Identified top 10 and low performing interns
Created visualizations:
Bar chart (Department Performance)
Boxplot (Performance Distribution)
Documented insights in notebook
Saved analysis results
Updated notebook and pushed changes to GitHub
🔹 Notes
Advanced analysis provided deeper insights into intern performance
High attendance is strongly related to better performance
Completion Rate is a key factor influencing performance
Department-wise comparison helped identify performance differences
Visualization helped in better understanding of data distribution
🔹 Any Blockers
None

## 📅 Sprint 2 – Day 3: KPI Finalization
🔹 Start of Day (SOD)

### Tasks Planned:

Identify and finalize key performance indicators (KPIs)
Calculate overall performance metrics:
Completion Rate
Average Performance Score
Average Attendance
Perform department-wise KPI comparison
Analyze relationships between KPIs
Summarize insights for dashboard preparation
Document findings in notebook
Update document.md and push to GitHub
🔹 End of Day (EOD)

### Tasks Completed:

Loaded cleaned dataset into notebook
Calculated Completion Rate for all interns
Computed overall KPIs:
Total Tasks Assigned
Total Tasks Completed
Average Completion Rate
Average Performance Score
Average Attendance
Performed department-wise KPI analysis using groupby()
Identified best performing department
Visualized KPI comparison using bar chart
Derived insights from KPI analysis
Documented results in notebook
Updated document.md and pushed changes to GitHub
🔹 Notes
KPIs help measure intern performance effectively
Completion Rate is a strong indicator of productivity
Attendance has a direct impact on performance
Department-wise analysis helps identify performance differences
KPI insights will be used in dashboard development
🔹 Any Blockers
None

## Sprint 2 – Day 4: Dashboard Planning
🔹 Start of Day (SOD)

### Tasks Planned:

Identify key KPIs for dashboard display (Completion Rate, Performance Score, Attendance)
Select visualizations to include in dashboard
Design dashboard layout (KPI cards, charts, insights)
Choose tool for dashboard development (Streamlit)
Create a basic dashboard structure/wireframe
Document dashboard planning details
Update document.md and push to GitHub
🔹 End of Day (EOD)

### Tasks Completed:

Finalized KPIs for dashboard:
Completion Rate
Performance Score
Attendance
Selected visualizations:
Bar chart (Department Performance)
Scatter plot (Tasks Assigned vs Completed)
Histogram (Attendance Distribution)
Heatmap (Correlation Analysis)
Designed dashboard layout:
Top section – KPI cards
Middle section – charts
Bottom section – insights
Chose Streamlit as the dashboard development tool
Documented dashboard structure and planning in notebook
Updated document.md with Day 4 details
Pushed all updates to GitHub
🔹 Notes
Dashboard planning helps organize how insights will be presented
KPIs provide a quick summary of performance
Visualizations make analysis easy to understand
A well-structured layout improves user experience
🔹 Any Blockers
None
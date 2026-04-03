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

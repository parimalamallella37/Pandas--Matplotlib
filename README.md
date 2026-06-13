# 📊 Student Marks Analysis using Python

## 📌 Project Overview

This project analyzes student academic performance using **Python**, **Pandas**, and **Matplotlib**. It processes student marks, handles missing values, calculates the best two mid-exam scores for each subject, generates grades, identifies top and bottom performers, and visualizes performance using charts.

## 🚀 Features

* Load and analyze student marks dataset.
* Handle missing values in the dataset.
* Calculate the **Best 2 Mid Exam Marks** for each subject.
* Compute total marks for every subject.
* Assign grades based on total marks.
* Calculate overall student performance.
* Display Top 10 and Bottom 10 students.
* Generate pie chart for subject-wise average marks.
* Generate bar charts for grade distributions.
* Export the processed dataset to a new CSV file.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

## 📂 Dataset Structure

The dataset should contain:

* Student Name
* Mid1 Marks
* Mid2 Marks
* Mid3 Marks
* Semester Marks

For the following subjects:

* Maths
* Physics
* Chemistry
* English
* Telugu
* IT

Example:

| Name | Maths_Mid1 | Maths_Mid2 | Maths_Mid3 | Maths_Sem |
| ---- | ---------- | ---------- | ---------- | --------- |
| John | 24         | 22         | 25         | 45        |

## 📈 Analysis Performed

### 1. Data Cleaning

* Detects missing values.
* Replaces missing values with `0`.

### 2. Best Two Mid Calculation

* Selects the highest two mid-exam scores.
* Calculates their sum.

### 3. Subject Total Marks

* Adds Best Two Mid Marks and Semester Marks.

### 4. Grade Assignment

| Marks Range | Grade |
| ----------- | ----- |
| 90+         | Ex    |
| 80-89       | A     |
| 70-79       | B     |
| 60-69       | C     |
| 50-59       | D     |
| 40-49       | E     |
| Below 40    | Fail  |

### 5. Student Ranking

* Identifies Top 10 students.
* Identifies Bottom 10 students.

### 6. Visualization

* Pie Chart for average subject marks.
* Bar Charts for grade distribution in each subject.

## ▶️ How to Run

1. Install required libraries:

```bash
pip install pandas matplotlib
```

2. Place the dataset file:

```text
student_marks.csv
```

in the project folder.

3. Run the script:

```bash
python student_marks_analysis.py
```

## 📁 Output

The project generates:

* Top 10 Students Report
* Bottom 10 Students Report
* Subject Average Pie Chart
* Grade Distribution Bar Charts
* Processed Dataset:

```text
student_marks_final_analysis.csv
```

## 🎯 Learning Outcomes

Through this project, you can learn:

* Data Cleaning with Pandas
* Data Manipulation and Analysis
* Handling Missing Values
* Data Visualization with Matplotlib
* Grade Calculation Logic
* Student Performance Analytics

## 👩‍💻 Author

**Parimala Mallela**

AI & ML Student passionate about Data Analysis, Machine Learning, and Artificial Intelligence.

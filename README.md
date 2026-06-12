# Garment Job Risk Dataset Cleaning & EDA with Pandas

## Project Overview

This project demonstrates a complete **Data Cleaning** and **Exploratory Data Analysis (EDA)** workflow using **Python** and **Pandas** on a Garment Job Risk dataset.

The dataset contains **2,500 rows and 14 columns**. The objective was to transform messy data into a clean, readable, and analysis-ready dataset by handling missing values, removing duplicates, validating data, detecting outliers, and performing basic statistical analysis.

---

## Dataset Features

* Name
* Garment_Name
* Experience_Years
* Job_Role
* Working_Hours_Per_Week
* Exposure_To_Chemicals
* Machine_Use
* Workstation_Ergonomics
* Injury_History
* Health_Condition
* Safety_Training
* Shift_Type
* Task_Rotation_Frequency
* Job_Risk

---

## Pandas Concepts Practiced

### Dataset Overview

* `head()`
* `tail()`
* `sample()`
* `shape`
* `columns`
* `dtypes`
* `info()`
* `describe()`

### Missing Value Analysis

* `isnull()`
* `isna()`
* `fillna()`
* `mean()`
* `median()`
* `mode()`

### Duplicate Handling

* `duplicated()`
* `drop_duplicates()`

### Date Handling

* `to_datetime()`

### Sorting

* `sort_values()`

### Filtering

* Single-condition filtering
* Multi-condition filtering
* Boolean operators (`&`, `|`)

### Statistical Analysis

* `mean()`
* `median()`
* `mode()`
* `max()`
* `min()`
* `std()`
* `count()`

### Grouping & Aggregation

* `groupby()`
* `agg()`

### Feature Engineering

* Creating new columns from existing columns

### Outlier Detection

* Conditional filtering
* Data validation

### Missing Value Imputation

* Forward Fill (`ffill`)
* Backward Fill (`bfill`)

---

## Data Cleaning Workflow

### 1. Missing Value Handling

* Filled numerical missing values using column means.
* Filled categorical missing values using column modes.

### 2. Duplicate Removal

* Identified duplicate records.
* Removed duplicate rows from the dataset.

### 3. Data Validation

* Checked data types and dataset structure.
* Verified dataset consistency.

### 4. Outlier Handling

* Inspected unusual values.
* Applied value capping for excessive working hours.

### 5. Feature Engineering

Created additional features such as:

* Hours_Per_Experience
* Experience_Workload
* Injury_Risk_Score

---

## Project Structure

```text
.
├── 1.py
├── making_clean.py
├── Garment_Job_Risk.csv
├── Garment_Job_Risk_Cleaned.csv
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* PyCharm
* Git & GitHub

---

## Learning Resources

This project was completed while learning through:

* AI/ML Engineering Bootcamp (Batch 1) by Shohoj Coding Platform
* W3Schools Documentation
* ChatGPT

---

## How to Run

Install dependencies:

```bash
pip install pandas
```

Run the Pandas practice file:

```bash
python 1.py
```

Run the cleaning pipeline:

```bash
python making_clean.py
```

The cleaned dataset will be generated as:

```text
Garment_Job_Risk_Cleaned.csv
```

---

## Learning Outcome

Through this project, I gained hands-on experience with:

* Real-world data cleaning
* Exploratory Data Analysis (EDA)
* Missing value treatment
* Duplicate handling
* Data transformation
* Feature engineering
* Outlier detection
* Pandas-based data preprocessing

This project helped me better understand how raw datasets are prepared before data analysis, visualization, and machine learning workflows.

---

## Author

**Mohammad Hasibur Rahman**

Department of Computer Science & Engineering (CSE)

Shahjalal University of Science and Technology (SUST)

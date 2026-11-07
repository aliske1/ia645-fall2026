# Lab 2 — Data Ingestion and Cleaning

**Course:** IA 645 — Data Analytics for Cybersecurity  
**Instructor:** Aaron Liske | aliske1@emich.edu  
**Week:** 2  
**Points:** 45  
**Due:** Check Canvas for exact due date

---

## Objective

Identify and correct data quality issues in a real-format security log dataset using Python and pandas.

## Background

Security data in the real world is almost never clean. Logs come from different systems with different formats, timestamps in different timezones, inconsistent field naming, missing values, and duplicate records. An analyst who cannot clean data cannot analyze it. This lab gives you a deliberately messy version of the authentication log from Lab 1 and asks you to document and fix its problems.

## Dataset

`week2/datasets/auth_log_messy/auth_log_messy.csv`

## Requirements


### Part 1 — Load and Audit the Dataset

- Load auth_log_messy.csv into a pandas DataFrame
- Use .info(), .isnull().sum(), and .value_counts() to audit the dataset
- Identify and document every data quality issue you find — be specific
- Expected issues include but may not be limited to: missing values, inconsistent timestamp formats, malformed IP addresses, inconsistent event_type casing, duplicate records
- Write a data quality report section in your write-up listing every issue found with row counts

### Part 2 — Clean the Dataset

- Fix timestamp inconsistencies — standardize all timestamps to YYYY-MM-DD HH:MM:SS format using pd.to_datetime()
- Handle missing data — document your decision: drop, fill, or flag? Justify your choice
- Standardize event_type — all values should be either SUCCESS or FAILED, uppercase
- Remove or flag malformed IP addresses — define what constitutes a malformed IP
- Remove duplicate records using .drop_duplicates()
- After cleaning, re-run .info() and .isnull().sum() to verify

### Part 3 — Validate and Compare

- Compare record counts before and after cleaning
- Compare event_type distribution before and after cleaning
- Export your cleaned dataset to a new CSV file: auth_log_clean.csv
- Load auth_log_clean.csv back in and verify it loads correctly

### Part 4 — Reflection

- What was the most common data quality issue in this dataset?
- What decisions did you make that could affect downstream analysis? For example, if you dropped rows with missing data, what events might you now be missing?
- How would these data quality issues affect a machine learning model trained on the dirty data?

---

## Submission

- Written lab report (Word or PDF) containing:
-   - Data quality audit report — every issue found with counts
-   - Justification for each cleaning decision made
-   - Before/after comparison of record counts and distributions
-   - Answers to all reflection questions
- Your completed Jupyter notebook (.ipynb) with all cells executed
- Your exported auth_log_clean.csv file

Submit via Canvas as a single zip or upload each file separately. All files must be submitted before the due date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Data quality audit — all issues identified and documented | 15 |
| Cleaning steps — all issues addressed with justified decisions | 15 |
| Validation — before/after comparison completed and exported | 10 |
| Written reflection — quality and depth of analysis | 5 |
| **Total** | **45** |

---

## AI Use Policy

AI tools may be used to help with pandas syntax. Your data quality audit and reflection answers must reflect your own analysis of this specific dataset — AI cannot tell you what is wrong with this particular file.

---

*All materials are for enrolled IA 645 students only.*
# Lab 5 — ML-Based Intrusion Detection

**Course:** IA 645 — Data Analytics for Cybersecurity  
**Instructor:** Aaron Liske | aliske1@emich.edu  
**Week:** 4  
**Points:** 45  
**Due:** Check Canvas for exact due date

---

## Objective

Build, train, and evaluate a machine learning classifier for intrusion detection using scikit-learn, and interpret your model's performance in a security context.

## Background

Machine learning intrusion detection systems (ML-IDS) attempt to classify network traffic or log events as malicious or benign based on learned patterns rather than fixed rules. This lab has two parts: first you build features from the course dataset and train a classifier, then you apply the same approach to the NSL-KDD benchmark dataset which has pre-labeled attack traffic.

## Dataset

`week4/datasets/course_data/auth_log.csv + security_events.db — plus NSL-KDD dataset (download instructions below)`

## Requirements


### Part 0 — Download NSL-KDD Dataset

- Download the NSL-KDD dataset from: https://www.unb.ca/cic/datasets/nsl.html
- Download KDDTrain+.txt and KDDTest+.txt
- Place both files in week4/datasets/nsl_kdd/
- The column names file is available at the same URL — download it too

### Part 1 — Feature Engineering on Course Dataset

- Load auth_log.csv from week4/datasets/course_data/
- Engineer the following features from the raw log data:
-   - failed_login_count: count of failed logins per username in a rolling window
-   - unique_ips_per_user: count of unique source IPs per username
-   - is_off_hours: binary flag, 1 if login outside 07:00-19:00
-   - port_is_ssh: binary flag, 1 if port == 22
- Create a binary label column: is_suspicious — flag any username that appears in the known attacker patterns from Lab 4
- Document your feature engineering decisions in your write-up

### Part 2 — Train a Classifier on Course Data

- Split your engineered dataset into 80% train / 20% test using train_test_split()
- Train a Random Forest classifier using RandomForestClassifier(n_estimators=100)
- Generate predictions on the test set
- Evaluate using: accuracy_score, confusion_matrix, classification_report
- Plot the confusion matrix as a heatmap using seaborn
- Plot feature importances as a bar chart

### Part 3 — NSL-KDD Benchmark

- Load KDDTrain+.txt and KDDTest+.txt with correct column names
- Encode categorical columns using LabelEncoder or pd.get_dummies()
- Create a binary label: 0 = normal, 1 = attack (original has multi-class labels)
- Train a second Random Forest classifier on the KDD training set
- Evaluate on the KDD test set using the same metrics as Part 2
- Compare performance between your course dataset model and the NSL-KDD model

### Part 4 — Reflection

- Why does precision matter more than accuracy in a security IDS context?
- What does a false positive mean operationally for a SOC analyst?
- What does a false negative mean for the organization being defended?
- Looking at your feature importances, which features drove detection most? Does that make intuitive sense given what you know about the planted attacks?

---

## Submission

- Written lab report (Word or PDF) containing:
-   - Feature engineering documentation — what you built and why
-   - Model performance metrics for both classifiers — confusion matrices, precision, recall, F1
-   - Feature importance plots with interpretation
-   - Comparison between course dataset and NSL-KDD results
-   - Reflection answers
- Your completed Jupyter notebook (.ipynb) with all cells executed

Submit via Canvas as a single zip or upload each file separately. All files must be submitted before the due date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Feature engineering — appropriate features built and documented | 10 |
| Course dataset classifier — correctly trained and evaluated | 10 |
| NSL-KDD classifier — correctly trained and evaluated | 10 |
| Visualizations — confusion matrix heatmaps and feature importance plots | 5 |
| Reflection — quality of answers, application to security context | 10 |
| **Total** | **45** |

---

## AI Use Policy

AI tools may be used to help with scikit-learn syntax. Your reflection answers and model interpretation must be your own analysis.

---

*All materials are for enrolled IA 645 students only.*
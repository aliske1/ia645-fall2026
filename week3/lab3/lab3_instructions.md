# Lab 3 — Statistical Anomaly Detection

**Course:** IA 645 — Data Analytics for Cybersecurity  
**Instructor:** Aaron Liske | aliske1@emich.edu  
**Week:** 3  
**Points:** 45  
**Due:** Check Canvas for exact due date

---

## Objective

Apply statistical methods to detect anomalous behavior in network traffic data, and visualize your findings.

## Background

Statistical anomaly detection is one of the foundational techniques in security analytics. Rather than looking for known attack signatures, you establish what normal looks like and flag deviations. This lab uses a network traffic dataset containing simulated enterprise traffic — with real attack behavior hidden in the noise. Your job is to find it using statistics, not intuition.

## Dataset

`week3/datasets/network_traffic/network_traffic.csv`

## Requirements


### Part 1 — Load and Explore

- Load network_traffic.csv into a pandas DataFrame
- Inspect the dataset — how many records, what columns, what time range?
- Plot a histogram of bytes_out — describe the distribution
- Plot a histogram of duration_sec — describe the distribution
- Plot a time series of event counts by hour of day

### Part 2 — Establish Baselines

- Calculate mean, median, and standard deviation for bytes_out
- Calculate mean, median, and standard deviation for duration_sec
- Calculate the average number of connections per username
- Document your baselines in your write-up — these are your definition of normal

### Part 3 — Z-Score Anomaly Detection

- Calculate z-scores for bytes_out: z = (value - mean) / std
- Flag any record with |z| > 3 as anomalous
- How many records are flagged? What usernames and destination IPs appear most in flagged records?
- Repeat z-score analysis for duration_sec
- Create a scatter plot of bytes_out vs duration_sec, coloring anomalous points red and normal points blue

### Part 4 — Off-Hours Detection

- Parse the timestamp column to extract hour of day
- Define business hours as 08:00–18:00
- Flag all events outside business hours
- How many off-hours events are there? Which usernames are most active off-hours?

### Part 5 — Findings

- Write a findings section summarizing what you found
- For each anomaly cluster you identified: what is it, when did it happen, who is involved, why is it suspicious?
- What would your next investigative step be as an analyst?

---

## Submission

- Written lab report (Word or PDF) containing:
-   - Baseline statistics documented
-   - All visualizations with captions explaining what each shows
-   - Anomaly detection results — counts, usernames, IPs involved
-   - Findings section — written narrative of what you found and why it matters
- Your completed Jupyter notebook (.ipynb) with all cells executed and all plots visible

Submit via Canvas as a single zip or upload each file separately. All files must be submitted before the due date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Exploration and baseline documentation | 10 |
| Z-score anomaly detection implemented correctly | 15 |
| Off-hours detection implemented correctly | 10 |
| Visualizations — appropriate chart types, labeled, captioned | 5 |
| Findings narrative — quality, specificity, analytical thinking | 5 |
| **Total** | **45** |

---

## AI Use Policy

AI tools may be used to help with matplotlib syntax or pandas operations. Your findings narrative must reflect your own analysis of this specific dataset and the specific anomalies you found.

---

*All materials are for enrolled IA 645 students only.*
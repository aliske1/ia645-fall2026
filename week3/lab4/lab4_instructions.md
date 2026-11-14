# Lab 4 — SQL-Based Threat Hunting

**Course:** IA 645 — Data Analytics for Cybersecurity  
**Instructor:** Aaron Liske | aliske1@emich.edu  
**Week:** 3  
**Points:** 45  
**Due:** Check Canvas for exact due date

---

## Objective

Write SQL queries to hunt for specific threat patterns across a multi-table security database, and document your findings in a professional threat hunting report.

## Background

Threat hunting is the proactive practice of searching through data to detect and isolate advanced threats that evade automated security tools. Unlike alert-based detection, hypothesis-driven hunting starts with a theory about attacker behavior and uses queries to confirm or deny it. This lab gives you a multi-table database representing a simulated enterprise environment with real attack patterns planted in the data. Your job is to find them.

## Dataset

`week3/datasets/security_events/security_events.db (4 tables: auth_log, network_log, role_changes, threat_intel)`

## Requirements


### Part 1 — Database Familiarization

- Connect to security_events.db using sqlite3
- List all tables using: SELECT name FROM sqlite_master WHERE type='table'
- For each table, describe its schema using PRAGMA table_info(tablename)
- Count records in each table
- Document the schema in your write-up — what does each table represent?

### Part 2 — Hunting Queries

- Hunt 1 — Brute Force: Find source IPs with more than 10 failed login attempts. List IP, count, and targeted usernames.
- Hunt 2 — Credential Stuffing: Find source IPs that attempted more than 5 unique usernames. List IP and unique username count.
- Hunt 3 — Off-Hours Access: Find successful logins that occurred before 07:00 or after 19:00. List timestamp, username, source IP, and hostname.
- Hunt 4 — Successful Login After Brute Force: Find usernames that had more than 5 failed logins followed by a successful login from the same IP.
- Hunt 5 — Data Exfiltration: Find sessions where bytes_out is more than 3 standard deviations above the mean. List username, dst_ip, bytes_out.
- Hunt 6 — Privilege Escalation: Find users whose role changed to admin. List username, timestamp, changed_by, and change_type.
- Hunt 7 — Threat Intel Correlation: JOIN auth_log with threat_intel on source_ip = ip_address. List any auth events from IPs classified as malicious.

### Part 3 — Attack Chain Documentation

- Based on your query results, identify the most significant attack chain you can reconstruct
- Document the chain chronologically: initial access → lateral movement or escalation → impact
- Name the specific timestamps, usernames, and IPs involved
- Map your findings to at least 2 MITRE ATT&CK techniques using the reference sheet in /course/resources/

### Part 4 — Recommended Detections

- For each hunt query that returned results, propose a detection rule that could alert on this behavior in real time
- Format: IF [condition] THEN alert [severity] — [description]

---

## Submission

- Written threat hunting report (Word or PDF) containing:
-   - Database schema documentation
-   - All 7 hunt queries with results (copy query and result table)
-   - Attack chain narrative — chronological reconstruction of what happened
-   - MITRE ATT&CK technique mapping
-   - Recommended detection rules
- Your completed Jupyter notebook (.ipynb) with all queries executed

Submit via Canvas as a single zip or upload each file separately. All files must be submitted before the due date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Database familiarization — schema documented correctly | 5 |
| Hunt queries 1-4 — correct SQL, results documented | 15 |
| Hunt queries 5-7 — correct SQL, results documented | 15 |
| Attack chain narrative — specificity, accuracy, chronological flow | 5 |
| Detection recommendations — actionable and specific | 5 |
| **Total** | **45** |

---

## AI Use Policy

AI tools may be used to help debug SQL syntax. Your attack chain narrative and detection recommendations must be your own analysis of what you actually found in this dataset.

---

*All materials are for enrolled IA 645 students only.*
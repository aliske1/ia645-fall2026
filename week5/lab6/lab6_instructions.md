# Lab 6 — ELK Stack Security Dashboard

**Course:** IA 645 — Data Analytics for Cybersecurity  
**Instructor:** Aaron Liske | aliske1@emich.edu  
**Week:** 5  
**Points:** 45  
**Due:** Check Canvas for exact due date

---

## Objective

Ingest security event data into Elasticsearch and build a professional security operations dashboard in Kibana.

## Background

The ELK stack — Elasticsearch, Logstash, Kibana — is one of the most widely deployed log management and SIEM platforms in enterprise security. Kibana dashboards are how SOC analysts monitor their environment in real time. This lab gives you hands-on experience ingesting data into ELK and building the kind of dashboard an analyst would actually use.

## Dataset

`week5/datasets/security_events/security_events.db (converted to JSON for ELK ingestion)`

## Requirements


### Part 0 — Start the ELK Environment

- The ELK environment uses a separate Docker Compose file from the base course container
- Navigate to the week5/lab6/elk/ folder of your repository in your terminal (see ELK_SETUP_GUIDE.md in that folder)
- Run: docker-compose up -d
- Wait approximately 60-90 seconds for Elasticsearch and Kibana to initialize
- Verify Elasticsearch is running: open http://localhost:9200 in your browser — you should see a JSON response
- Open Kibana at: http://localhost:5601
- Take a screenshot of both URLs responding correctly

### Part 1 — Prepare and Ingest Data

- Open lab6_notebook.ipynb in JupyterLab (base container)
- Load security_events.db and export auth_log and network_log tables to JSON
- Use the Python elasticsearch client to index the auth_log records into an index called ia645-auth
- Index the network_log records into an index called ia645-network
- Verify record counts in Elasticsearch match your database record counts

### Part 2 — Build Kibana Dashboard

- In Kibana, create an Index Pattern for ia645-auth and ia645-network
- Set the time field to timestamp
- Build the following visualizations:
-   - Visualization 1: Time series line chart — login events over time, split by event_type (SUCCESS vs FAILED)
-   - Visualization 2: Bar chart — top 10 source IPs by failed login count
-   - Visualization 3: Pie chart — event_type distribution
-   - Visualization 4: Data table — top 10 usernames by total login attempts
-   - Visualization 5: Time series — network bytes_out over time
-   - Visualization 6 (your choice) — any visualization that highlights something interesting in the data
- Assemble all 6 visualizations into a single dashboard titled: IA645 Security Operations Dashboard

### Part 3 — Dashboard Analysis

- Take a full screenshot of your completed dashboard
- For each visualization, write 2-3 sentences explaining: what it shows, why it is useful to a SOC analyst, and what you observe in this specific dataset
- Identify the most suspicious pattern visible in your dashboard and explain it

---

## Submission

- Written lab report (Word or PDF) containing:
-   - Screenshots of Elasticsearch and Kibana running
-   - Screenshot of your completed dashboard
-   - Individual screenshots of each visualization
-   - Written analysis of each visualization (2-3 sentences each)
-   - Identification and explanation of the most suspicious pattern
- Your completed Jupyter notebook (.ipynb) showing data ingestion

Submit via Canvas as a single zip or upload each file separately. All files must be submitted before the due date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| ELK environment running — both URLs verified with screenshots | 5 |
| Data ingested correctly — record counts verified | 10 |
| All 6 visualizations built and assembled into dashboard | 20 |
| Written analysis — quality, specificity, security relevance | 10 |
| **Total** | **45** |

---

## AI Use Policy

AI tools may be used to help with Elasticsearch client syntax. Your dashboard analysis must reflect what you actually see in your specific dashboard.

---

*All materials are for enrolled IA 645 students only.*
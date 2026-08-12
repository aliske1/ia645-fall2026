# IA 645 — Data Analytics for Cybersecurity
## Fall 2026 | Eastern Michigan University | Aaron Liske

---

## Course Overview

This repository contains all lab environments, datasets, and resources for IA 645. Everything you need to complete the labs is here. Read this document carefully before Week 2.

---

## Getting Started — Required Setup

Complete these steps **before Week 2**. If you run into issues, post in the Week 2 QCC board on Canvas.

### Step 1 — Install Docker Desktop

1. Go to https://www.docker.com/products/docker-desktop
2. Download the Windows installer (AMD64 for most machines)
3. Run the installer — say **yes** to WSL2 if prompted
4. Restart your computer after installation
5. Launch Docker Desktop from the Start menu
6. Wait until you see **"Engine running"** in Docker Desktop before continuing

**System requirements:** Windows 10/11, minimum 8GB RAM (16GB recommended), 30GB free storage

---

### Step 2 — Create a GitHub Account

If you do not already have one, create a free account at https://github.com

---

### Step 3 — Clone This Repository

Open PowerShell and run:

```
git clone https://github.com/[INSTRUCTOR_GITHUB]/ia645-fall2026.git
```

This downloads the entire course repository to your machine. Navigate into it:

```
cd ia645-fall2026
```

If you do not have Git installed, download it at https://git-scm.com/download/win

---

### Step 4 — Build the Course Docker Image

Make sure Docker Desktop is running, then in PowerShell run:

```
docker build -t ia645-base .
```

This will take a few minutes the first time. You only need to do this once.

---

### Step 5 — Start the Course Environment

Double-click **start_ia645.bat** in the repository folder, or run in PowerShell:

```
docker run -p 8888:8888 -v "${PWD}:/course" ia645-base
```

Then open your browser and go to:

```
http://localhost:8888
```

You should see JupyterLab open. You are ready to work.

---

## Verifying Your Setup

In JupyterLab, open a new notebook and run the following to confirm everything is installed:

```python
import pandas as pd
import sqlite3
import sklearn
import matplotlib
import seaborn as sns

print("pandas:", pd.__version__)
print("scikit-learn:", sklearn.__version__)
print("matplotlib:", matplotlib.__version__)
print("seaborn:", sns.__version__)
print("sqlite3:", sqlite3.sqlite_version)
print("All good!")
```

If you see version numbers and "All good!" your environment is working correctly.

---

## Repository Structure

```
ia645-fall2026/
├── README.md                  ← You are here
├── Dockerfile                 ← Course container definition
├── start_ia645.bat            ← Windows quick-start script
├── setup/                     ← Additional setup guides
├── datasets/                  ← Datasets organized by week
├── labs/                      ← Lab instructions and starter notebooks
└── resources/                 ← Reference materials and cheat sheets
```

---

## Lab Submission

Each lab folder contains:
- **Instructions** — what the lab asks you to do
- **Starter notebook** — a scaffold to work from

Your submission is a single Canvas upload containing:
- Your completed Jupyter notebook (.ipynb)
- A written lab report documenting your methodology and findings (Word or PDF)
- Screenshots of key outputs where specified

See individual lab instructions for specific requirements.

---

## Getting Help

- **QCC Board** — Post questions about lab content on the weekly Canvas discussion board
- **Office Hours** — Zoom by appointment, request via email at aliske1@emich.edu
- **Common Issues** — Check the setup guide in the `/setup` folder before posting

---

*All materials in this repository are for enrolled IA 645 students only. Do not distribute outside the course.*

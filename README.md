# github-repository-analytics
The GitHub Repository Analytics Pipeline demonstrates how raw data from a REST API can be transformed into meaningful insights through a structured Data Engineering workflow. The project combines Python programming, ETL concepts, database analytics, SQL, and interactive visualization to create an end-to-end data pipeline.
# GitHub Repository Analytics Pipeline

## 📌 Project Overview

The GitHub Repository Analytics Pipeline is a Data Engineering project that collects public repository data from the GitHub REST API, processes and transforms the data, stores it in an analytical database, and presents insights through an interactive dashboard.

The project follows an end-to-end data engineering workflow:

**Extract → Transform → Store → Analyze → Visualize**

---

## 🎯 Project Objectives

- Extract public repository data from the GitHub REST API.
- Clean and transform raw JSON data using Python and Pandas.
- Handle missing values and duplicate records.
- Store processed data in Parquet format.
- Load structured data into DuckDB.
- Perform analytical queries using SQL.
- Visualize repository insights using Streamlit.
- Build a modular and reusable data pipeline.

---

## 🏗️ Project Architecture

```text
GitHub REST API
       │
       ▼
Python + Requests
       │
       ▼
Raw JSON Data
       │
       ▼
Pandas Data Transformation
       │
       ▼
Processed Parquet Data
       │
       ▼
DuckDB Database
       │
       ▼
SQL Analytics
       │
       ▼
Streamlit Dashboard

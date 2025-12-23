# Databricks Bronze Ingestion Framework

This repository demonstrates an **enterprise-grade Bronze ingestion framework**
built using **Azure Databricks, PySpark, and Delta Lake**.

The framework is designed for **regulated enterprise environments**
and follows production-ready ingestion patterns.

---

## 🔧 Key Capabilities

- Config-driven source ingestion
- Column standardisation & naming enforcement
- Column exclusion for sensitive / non-required fields
- Idempotent Delta Lake writes
- Scalable Bronze layer design (Medallion Architecture)

---

## 🧱 Architecture (Bronze Layer)

Source Files (CSV / Extracts)
↓
Read & Standardise Columns
↓
Apply Column Exclusions
↓
Bronze Delta Table

---

## 🛠️ Tech Stack

- Azure Databricks
- PySpark
- Delta Lake
- Azure Data Lake Gen2 (simulated)

└── table_config.json
notebooks/
├── 01_read_source.py
├── 02_standardize_columns.py
├── 03_apply_exclusions.py
└── 04_write_bronze_delta.py
DISCLAIMER.md
README.md

---


---

## ⚠️ Disclaimer

All data paths, table names, and configurations are **generic placeholders**.
No enterprise data, credentials, or proprietary information is included.


## 📁 Repository Structure


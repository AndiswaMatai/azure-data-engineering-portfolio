# 🔄 Azure Incremental & Streaming Data Pipeline

Enterprise-grade incremental ingestion and near-real-time analytics solution
built on Azure cloud services.

---

## 📌 Business Scenario
Operational systems generate **high-volume transactional data** that cannot
be fully reloaded daily due to cost, latency, and performance constraints.

The business requires:
- Near-real-time visibility into operations
- Incremental updates instead of full refreshes
- Scalable and fault-tolerant pipelines
- Secure, governed data access

---

## 🎯 Solution Overview
This project demonstrates an **incremental + streaming data pipeline** using Azure.

### Key Capabilities
- Incremental ingestion using watermark columns
- Streaming ingestion for real-time events
- Bronze → Silver → Gold data architecture
- Late-arriving data handling
- Data quality and governance controls

---

## 🛠️ Technology Stack
- **Azure Data Factory** – incremental batch ingestion
- **Azure Event Hubs** – streaming ingestion
- **Azure Databricks (PySpark)** – transformations
- **Azure Delta Lake** – ACID-compliant storage
- **Azure Synapse Analytics** – analytics layer
- **Power BI** – near-real-time dashboards
- **AAD & Key Vault** – security and secrets

---

## 🔄 Architecture Flow

1. Source systems emit transactional data
2. ADF ingests **only new or changed records**
3. Event Hubs streams real-time events
4. Databricks applies transformations
5. Delta Lake maintains Bronze / Silver / Gold tables
6. Synapse exposes curated analytics
7. Power BI consumes live datasets

---

## 🧱 Incremental Load Logic

```text
WHERE LastUpdated > @Watermark
Watermark stored in control table

Late-arriving data handled via reprocessing window

Idempotent writes using Delta Lake MERGE

---
📊 Reporting Use Cases

Live operational dashboards

SLA breach monitoring

Volume and latency tracking

Trend analysis by time windows

---
🎯 Business Outcomes

Reduced processing costs

Near-real-time visibility

Scalable ingestion architecture

Audit-ready, governed datasets

---


---

## ✅ STEP 2.2.3 — Commit the changes

1. Scroll down
2. Commit message:

---
3. Click **Commit changes**

## 🌐 VERIFY IT’S LIVE

Open this link in a new tab:

---

https://andiswamatai.github.io/azure-data-engineering-portfolio/azure-incremental-pipeline/


You should see the page rendered 🎉

---

## 🥉 NEXT STEP (Very important)

Next we will:
### 🥉 STEP 2.3 — Add Images + Mock Streaming Scripts
- Architecture diagram
- Databricks streaming notebook
- ADF watermark example
- Power BI real-time dashboard mock

This is what **pushes you into senior / lead level**.

👉 Say **“Step 2.2 done”** and we continue.

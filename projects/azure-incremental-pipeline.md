# ⚡ Azure Incremental Data Pipeline (Streaming-style)

## 📌 Business Scenario
Mobility platforms generate trip data continuously.
Reprocessing full datasets is expensive and slow.

This project demonstrates a **watermark-based incremental ingestion**
strategy to process only **new or updated trip records**.

---

## 🏗️ Architecture
- Azure Data Factory – watermark-based ingestion
- Azure Data Lake – bronze & silver zones
- Azure Databricks – incremental MERGE logic
- Azure Synapse Analytics – serving layer
- Power BI – near real-time dashboards

---

## 🔄 Incremental Logic
- Track `LastUpdatedTimestamp`
- Store last watermark in control table
- Fetch only new/changed records
- Merge into clean datasets

---

## 🎯 Business Outcomes
- Reduced processing costs
- Faster dashboard refresh
- Production-ready scalability
- Audit-friendly data lineage


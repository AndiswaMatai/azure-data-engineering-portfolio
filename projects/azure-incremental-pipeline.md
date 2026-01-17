# 🔄 Azure Incremental Data Pipeline (Streaming-Style)

## Business Context
Mobility platforms generate **high-volume trip and event data continuously**.
Reprocessing full datasets daily is computationally expensive and delays insight delivery.

This project demonstrates a **watermark-based incremental ingestion strategy**
that processes only new or updated records.

---

## Problem Statement
The existing batch processing approach had several limitations:

- Full dataset reloads consumed excessive compute resources
- Long processing times delayed analytics
- Duplicate data risks during reprocessing
- Limited support for near real-time reporting

---

## Solution Overview
An incremental Azure data pipeline was designed to ingest and process data efficiently
using **watermarking and idempotent logic**.

### Architecture Components
- **Azure Data Factory (ADF)**  
  Implemented watermark-based incremental ingestion

- **Azure Data Lake Storage (ADLS)**  
  Stored raw incremental data and curated datasets

- **Azure Databricks**  
  Applied deduplication, transformation, and enrichment logic

- **Azure Synapse Analytics**  
  Served as the analytics layer for incremental data

- **Power BI**  
  Delivered near real-time operational dashboards

---

## Incremental Pipeline Flow
Source System
↓
ADF (Watermark Logic)
↓
ADLS (Incremental Loads)
↓
Databricks (Deduplication & Transforms)
↓
Synapse Analytics
↓
Power BI

---


---

## Automation & Governance
- Watermark tracking to identify new and updated records
- Idempotent pipeline design to prevent duplicates
- Automated scheduling and monitoring
- Optimized compute usage through incremental processing

---

## Business Impact
- ⚡ Reduced processing time by over 70%
- 💰 Lowered compute and storage costs
- 📈 Enabled near real-time insights
- 🔄 Improved pipeline reliability and scalability

---

## Technology Stack
- Azure Data Factory  
- Azure Databricks  
- Azure Data Lake Storage  
- Azure Synapse Analytics  
- Python  
- SQL  
- Power BI  

---

## STAR Interview Narrative

### Situation
High-volume trip data was being reprocessed in full,
leading to inefficient pipelines and delayed insights.

### Task
Design an efficient incremental ingestion strategy
to improve performance and reduce costs.

### Action
- Implemented watermark logic in ADF
- Built incremental transformation pipelines in Databricks
- Ensured idempotency and data quality checks
- Modeled incremental datasets in Synapse

### Result
- Faster pipeline execution
- Reduced infrastructure costs
- Improved data freshness for business users

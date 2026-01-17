# 🏎️ GUUD Mobility — Azure Data Engineering Case Study

## Business Context
**GUUD Mobility** provides urban mobility services, managing fleet operations, routes, and revenue.
Core operational and financial data was hosted **on-premise in SQL Server**, creating challenges
for scalability, reporting speed, and executive visibility.

---

## Problem Statement
The business faced several data challenges:

- Fragmented operational and financial datasets
- Manual reporting cycles taking multiple days
- Limited visibility into real-time fleet performance
- Delayed decision-making for route and utilization optimization
- Lack of executive-level KPIs across fleet, routes, and revenue

---

## Solution Overview
An **end-to-end Azure data engineering platform** was designed and implemented to modernize
data ingestion, transformation, storage, and analytics.

### Architecture Components
- **Azure Data Factory (ADF)**  
  Ingested raw on-prem SQL Server data into Azure Data Lake Storage (ADLS)

- **Azure Databricks**  
  Cleaned, standardized, and transformed raw datasets into analytics-ready structures

- **Azure Synapse Analytics**  
  Stored curated datasets and provided optimized analytical models

- **Power BI**  
  Delivered interactive dashboards for operational and executive stakeholders

- **Azure AD & Key Vault**  
  Enabled enterprise-grade security, access control, and secrets management

---

## Data Pipeline Flow

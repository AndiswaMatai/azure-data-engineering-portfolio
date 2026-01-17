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

SQL Server (On-Prem)
↓
Azure Data Factory
↓
ADLS (Raw → Clean)
↓
Azure Databricks
↓
Synapse Analytics
↓
Power BI Dashboards

---

## Automation & Governance
- Fully automated ETL pipelines with scheduled refreshes
- Elimination of manual reporting processes
- Secure credential management via Azure Key Vault
- Role-based access control through Azure AD
- Monitoring and failure handling built into pipelines

---

## Business Impact
The solution delivered measurable business outcomes:

- ⏱ **Reporting time reduced** from **2–3 days → under 2 hours**
- 🚗 **Fleet utilization improved by 12%** through better route optimization
- 📊 Near real-time executive dashboards for faster decision-making
- 📈 Improved data accuracy and consistency across departments

---

## Technology Stack
- Azure Data Factory  
- Azure Databricks  
- Azure Synapse Analytics  
- Azure Data Lake Storage (ADLS)  
- Python  
- SQL  
- Power BI  

---

## Key Takeaways
This project demonstrates:
- Enterprise-scale Azure data engineering design
- Modern cloud migration from on-premise systems
- Automated, analytics-ready data pipelines
- Business-driven data architecture aligned to executive KPIs

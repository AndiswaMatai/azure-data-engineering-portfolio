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

## Architecture Diagram

![GUUD Mobility Azure Architecture](../images/guud_mobility/architecture.png)

---

## Data Ingestion & Transformation

![ADF Pipeline](../images/guud_mobility/adf_pipeline.png)

---

## Analytics & Reporting

![Power BI Dashboard](../images/guud_mobility/powerbi_dashboard.png)

---

## Architecture Diagram

![GUUD Mobility Azure Architecture](../images/guud_mobility/architecture.png)

**Description:**  
- **Source Systems:** On-prem SQL Server databases for fleet and financial data  
- **ADF Pipelines:** Orchestrates extraction and landing into ADLS  
- **ADLS (Raw → Clean):** Raw data is stored and then cleaned/transformed  
- **Databricks:** Applies transformation, standardization, and business logic  
- **Synapse Analytics:** Analytics-ready datasets for reporting  
- **Power BI:** Interactive dashboards for operational and executive users

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

---

## Role Alignment

### Senior Data Engineer
- Designed and implemented cloud-native Azure data pipelines
- Optimized ETL performance and data models
- Delivered analytics-ready datasets for BI consumption

### Lead Data Engineer
- Defined end-to-end data architecture and standards
- Established governance, security, and automation practices
- Collaborated with business stakeholders on KPI definition

### Analytics / Data Engineering Manager
- Translated business problems into scalable data solutions
- Enabled executive decision-making through trusted dashboards
- Drove measurable business outcomes through data initiatives


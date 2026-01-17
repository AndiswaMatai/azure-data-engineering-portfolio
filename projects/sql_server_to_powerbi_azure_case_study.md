# 🌐 Azure Data Engineering — SQL Server to Power BI

## Business Context
Many organizations rely on **on-premise SQL Server** systems for operational reporting.
However, legacy reporting architectures often struggle with scalability, automation,
and modern analytics requirements.

This project demonstrates an **end-to-end Azure data engineering solution**
for ingesting, transforming, and visualizing SQL Server data using cloud-native services.

---

## Problem Statement
The existing reporting approach presented several challenges:

- Manual or semi-automated data extracts from SQL Server
- Slow reporting refresh cycles
- Limited scalability for growing data volumes
- Lack of centralized data governance
- Business users dependent on technical teams for insights

---

## Solution Overview
A modern Azure data platform was designed to automate ingestion, transformation,
and analytics delivery from SQL Server to Power BI.

### Architecture Components
- **Azure Data Factory (ADF)**  
  Extracted SQL Server data and landed it in Azure Data Lake Storage

- **Azure Data Lake Storage (ADLS)**  
  Served as the raw and clean data zones

- **Azure Databricks**  
  Applied data cleansing, standardization, and transformation logic

- **Azure Synapse Analytics**  
  Modeled curated datasets optimized for analytics

- **Power BI**  
  Delivered self-service and executive dashboards

---

## Data Pipeline Flow
SQL Server
↓
Azure Data Factory
↓
ADLS (Raw → Clean)
↓
Azure Databricks
↓
Synapse Analytics
↓
Power BI

---


---

## Automation & Governance
- Fully automated ETL pipelines
- Scheduled refreshes eliminating manual intervention
- Centralized data storage and versioning
- Secure access control using Azure AD
- Consistent data models across reports

---

## Business Impact
- ⏱ Reduced reporting latency from hours to minutes
- 📊 Improved data consistency across business units
- 🔄 Enabled scalable, repeatable reporting pipelines
- 👥 Empowered business users with self-service analytics

---

## Technology Stack
- Azure Data Factory  
- Azure Data Lake Storage  
- Azure Databricks  
- Azure Synapse Analytics  
- SQL Server  
- Power BI  

---

## STAR Interview Narrative

### Situation
Reporting relied heavily on direct SQL Server queries and manual extracts,
creating performance and scalability issues.

### Task
Design and implement a scalable Azure-based data platform
to modernize ingestion and reporting.

### Action
- Built automated ADF pipelines from SQL Server
- Implemented transformation logic in Databricks
- Modeled analytics-ready datasets in Synapse
- Delivered Power BI dashboards for business users

### Result
- Faster reporting cycles
- Reduced dependency on technical teams
- Improved trust in reporting data

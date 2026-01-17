# 🏎️ GUUD Mobility — Azure Data Engineering Case Study

**Context:**  
GUUD Mobility provides urban mobility services with fleet and operational data stored in SQL Server on-premise.  

**Problem Statement:**  
- Fragmented operational and financial data delayed decision-making.  
- Manual reporting cycles were slow, limiting actionable insights.  
- Leadership lacked real-time KPIs on fleet, routes, and revenue.  

**Solution Implemented:**  
- Built end-to-end **Azure data platform**:  
  - **ADF** – ingest raw SQL Server data into ADLS  
  - **Databricks** – clean and transform data  
  - **Synapse Analytics** – store and model clean datasets  
  - **Power BI** – interactive dashboards  
  - **AAD & Key Vault** – governance, security, and monitoring  
- Automated ETL pipelines and scheduled refreshes to eliminate manual reporting  

**Business Impact:**  
- Reduced reporting time from 2–3 days → under 2 hours  
- Improved fleet utilization by 12% through route optimization  
- Provided near real-time dashboards for executive decision-making  

**Tech Stack:** Azure Data Factory, Databricks, Synapse Analytics, ADLS, Python, SQL, Power BI

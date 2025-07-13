Week 6 Azure Data Factory Assignment
Dheeraj Joshi

Objective
This assignment demonstrates how I built and automated data pipelines in Azure Data Factory (ADF) to simulate hybrid and external integrations, automate incremental loads, and handle failure scenarios.

Directory Structure
ADFWeek6_Assignment/
├── 1_SHIR_to_AzureSQL/
│   ├── 01.png ... 12.png
├── 2_FTP_to_Blob/
│   ├── 01.png ... 02.png
├── 3_Incremental_Loads_Triggers/
│   ├── 01.png ... 02.png
├── 4_Retry_and_Settings/
│   ├── 01.png
├── README.txt

1. SHIR to Azure SQL – Data Extraction & Loading
Note: Since Self-hosted Integration Runtime (SHIR) is not supported on Mac, I simulated the hybrid scenario by creating two Azure SQL Databases: one representing the "local" source, and one as the Azure target. This allowed me to demonstrate the end-to-end data pipeline process entirely within Azure.

- Configured linked services for both source (LocalSQLSource) and target (AzureSQLTarget) Azure SQL databases.
- Adjusted firewall/IP access on SQL server for connectivity.
- Populated source database with test data via SQL scripts.
- Created datasets for both source and target tables.
- Built the CopyOrdersPipeline for data movement.
- Implemented retry logic (3 retries, 10s interval) on the copy activity.
- Ran debug tests to ensure the pipeline worked as expected.

2. FTP to Azure Blob Pipeline
- Created an FTP linked service to connect to test.rebex.net.
- Configured FTP dataset (Binary1) and Azure Blob Storage dataset (Binary2).
- Built a pipeline to copy the file from FTP to Azure Blob Storage.
- Verified the output to ensure successful transfer.

3. Incremental Loads and Triggers
- Added a pipeline parameter (lastWatermark) for incremental loading.
- Dynamic SQL query: Only pull records newer than the last watermark.
- Created a daily trigger for incremental loads.
- Configured a monthly trigger to run every last Saturday.

4. Failure Handling & Retry Logic
- Configured retry settings (3 retries, 10s interval) for the copy activity to handle transient failures like network or DB issues.

Screenshot Legend
All screenshots are renamed and grouped according to each step. Please refer to the folders above for a clear mapping to each assignment component.

Submission
All images and this README are packaged in a single zip file, with a clean folder structure.

Prepared by:
Dheeraj Joshi
Week 6 Azure Data Factory Assignment

--  ETL Load Script for Azure Synapse
-- Load clean dataset from CSV in Data Lake to Synapse staging table

CREATE TABLE IF NOT EXISTS StagingTrips (
    DriverID VARCHAR(10),
    RouteID VARCHAR(10),
    TripDate DATE,
    TripDurationMinutes FLOAT,
    FareCollected FLOAT,
    RevenuePerHour FLOAT
);

BULK INSERT StagingTrips
FROM 'adl://datalake/clean/sample_clean_table.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- Verify load
SELECT TOP 10 * FROM StagingTrips;

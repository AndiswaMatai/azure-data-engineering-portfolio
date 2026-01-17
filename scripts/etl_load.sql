ETL: Load clean data into Synapse staging table
CREATE TABLE StagingTrips (
    DriverID VARCHAR(10),
    RouteID VARCHAR(10),
    TripDate DATE,
    TripDurationMinutes INT,
    FareCollected DECIMAL(10,2),
    RevenuePerHour DECIMAL(10,2)
);

BULK INSERT StagingTrips
FROM '../data/clean/sample_clean_table.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',

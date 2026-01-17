CREATE TABLE WatermarkControl (
    PipelineName VARCHAR(100),
    LastProcessedTimestamp DATETIME
);

INSERT INTO WatermarkControl
VALUES ('TripsIncrementalPipeline', '2024-01-01 00:00:00');


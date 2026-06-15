CREATE DATABASE system_monitoring;
USE system_monitoring;

CREATE TABLE system_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    cpu_usage FLOAT,
    memory_usage FLOAT,
    disk_usage FLOAT,
    bytes_received BIGINT,
    bytes_sent BIGINT
);

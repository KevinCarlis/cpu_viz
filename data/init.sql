DROP DATABASE IF EXISTS cpudata;
CREATE DATABASE IF NOT EXISTS cpudata;
USE cpudata;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS registers;

/*!50503 set default_storage_engine = InnoDB */;
/*!50503 select CONCAT('storage engine: ', @@default_storage_engine) as INFO */;

CREATE TABLE registers (
    name varchar(10) NOT NULL,
    value varchar(8) DEFAULT '00000000'
);

INSERT INTO registers (name) VALUES ('Register 0'), ('Register 1'), 
    ('Register 2'), ('Register 3'), ('Register 4'), ('Register 5'), 
    ('CPSR'), ('PC');

flush /*!50503 binary */ logs;

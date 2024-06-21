-- This script creates the table id_not_null on MySQL server.
-- id default value is 1.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

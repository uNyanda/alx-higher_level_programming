-- This script  creates a table called first_table in the current database in MySQL server.
-- If the table first_table already exists, your script doesn't fail
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);

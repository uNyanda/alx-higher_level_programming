-- This script creates a database 'hbtn_0d_usa' and the table 'cities' (in the database 'hbtn_0d_usa') on MySQL server.

/* first: create the database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* second: use the created database */
USE hbtn_0d_usa;

/* third: create the table in the database */
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);

-- This script creates a database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server.
-- id must be a primary key & can't be null.

/* first: create the database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* second: use the created database */
USE hbtn_0d_usa;

/* third: create the table in the created database */
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);

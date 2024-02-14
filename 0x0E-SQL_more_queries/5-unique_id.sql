-- A script that creates the table unique_id on your MySQL server.
-- Create the table unique_id if it doesn't exist

CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

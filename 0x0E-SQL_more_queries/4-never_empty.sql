-- Create the table id_not_null
-- if already exists, should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);

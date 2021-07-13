-- Create the MySQL server user_0d_1
-- Set the password of the user if it doesn't exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges for this user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';

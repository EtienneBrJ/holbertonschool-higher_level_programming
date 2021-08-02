-- Create the databse htbn_0d_2 and the user_0d_2
-- user only have the SELECT privilege
-- script should not fail if it already exists (databse or user)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant only SELECT privilege to user below
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';

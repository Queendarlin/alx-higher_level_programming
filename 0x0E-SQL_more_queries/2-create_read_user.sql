-- A script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Create the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- If user_0d_2 doesn't exist, create it with SELECT privilege only on hbtn_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

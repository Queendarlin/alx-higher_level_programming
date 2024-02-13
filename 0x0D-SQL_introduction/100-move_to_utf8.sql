-- Convert the database, table and fields to UTF-8
-- This script will switch to the hbtn_0c_0 database and then alter the first_table
-- within that database to use the UTF-8 character set (utf8mb4) and the utf8mb4_unicode_ci collation
USE `hbtn_0c_0`;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

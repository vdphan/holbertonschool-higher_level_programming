-- Choose database
USE hbtn_0c_0;
-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts table data to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts field name
ALTER TABLE first_table MODIFY name varchar(256) CHARACTER SET utf8mb4;

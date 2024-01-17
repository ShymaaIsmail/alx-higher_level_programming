-- change db collation(db rules for how data is stored and compared)
ALTER DATABASE CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;

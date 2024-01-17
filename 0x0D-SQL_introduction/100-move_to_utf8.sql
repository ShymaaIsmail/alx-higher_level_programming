-- change db collation(db rules for how data is stored and compared)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci

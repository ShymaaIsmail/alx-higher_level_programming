-- 3-list_tables.sql
SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema='$1'

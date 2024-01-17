-- 3-list_tables.sql
SCHEMA_NAME='$1' # Replace with your actual schema name
SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE' AND table_schema='$SCHEMA_NAME'

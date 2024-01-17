-- 15-groups.sql
SELECT score, COUNT(id) as number
FROM second_table
group by score

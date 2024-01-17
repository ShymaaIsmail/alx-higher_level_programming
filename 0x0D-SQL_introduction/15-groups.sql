-- 15-groups.sql
SELECT score, COUNT(id) as number
FROM second_table
ORDER BY score DESC
group by score

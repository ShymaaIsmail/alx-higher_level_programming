-- 102-top_city.sql
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3

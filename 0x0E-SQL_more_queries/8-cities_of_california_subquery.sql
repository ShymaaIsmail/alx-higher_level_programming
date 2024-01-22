-- 8-cities_of_california_subquery.sql
SELECT c.id, c.name
FROM cities AS c
WHERE c.state_id in (SELECT s.id
                        FROM states AS s
                        WHERE s.NAME = "California")

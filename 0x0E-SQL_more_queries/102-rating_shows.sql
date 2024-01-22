-- 102-rating_shows.sql
SELECT tv_shows.title, SUM(rate) as rating
FROM tv_shows JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC

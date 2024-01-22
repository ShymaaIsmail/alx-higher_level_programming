-- 13-count_shows_by_genre.sql
SELECT tv_genres.name AS 'genre', COUNT(DISTINCT(tv_shows.id)) AS 'number_of_shows'
FROM tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON  tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY  COUNT(DISTINCT(tv_shows.id)) DESC

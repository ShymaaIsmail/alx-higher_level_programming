-- 100-not_my_genres.sql
SELECT DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name not in (SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC
)
ORDER BY tv_genres.name ASC

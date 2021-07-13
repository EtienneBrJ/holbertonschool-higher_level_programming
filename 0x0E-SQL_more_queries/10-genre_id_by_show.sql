-- Lists all shows contained in hbtn_0d_tvshows
-- each record should display in ascending order tv_shows.title and tv_show_genres.genre_id
-- only one SELECT
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

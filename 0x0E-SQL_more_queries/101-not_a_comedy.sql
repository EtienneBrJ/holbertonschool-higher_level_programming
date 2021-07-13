-- Lists all shows without the genre Comedy
SELECT title FROM tv_shows
WHERE id NOT IN (
    SELECT tv_shows.id FROM tv_shows
    JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE name = 'Comedy')
ORDER BY title ASC;

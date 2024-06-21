-- This script lists all shows contained tin the database 'hbtn_0d_tvshows'

-- The data to display.
SELECT tv_shows.title, tv_show_genres.genre_id

-- The main table to work from.
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC ;

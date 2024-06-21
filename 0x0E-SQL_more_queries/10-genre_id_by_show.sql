-- This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- The data to display.
SELECT tv_shows.title, tv_show_genres.genre_id

-- The main table to use.
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

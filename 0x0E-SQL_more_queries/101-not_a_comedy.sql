-- This script lists all shows without the genre 'Comedy' in the database 'hbtn_0d_tvshows'.

SELECT tv_shows.title
FROM tv_shows
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres
    INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy' AND tv_show_genres.show_id = tv_shows.id
)
ORDER BY tv_shows.title ASC;

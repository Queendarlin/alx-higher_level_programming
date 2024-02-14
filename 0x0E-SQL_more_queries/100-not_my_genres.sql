-- Import the database dump from hbtn_0d_tvshows to your MySQL server

-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- Select genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter' AND tv_show_genres.genre_id = tv_genres.id
)
ORDER BY tv_genres.name ASC;

-- Import the database dump of hbtn_0d_tvshows to your MySQL server

-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.

-- Select shows and their linked genre IDs using LEFT JOIN
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

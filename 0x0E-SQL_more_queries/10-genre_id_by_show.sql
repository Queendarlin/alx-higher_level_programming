-- Import the database dump from hbtn_0d_tvshows to your MySQL server

-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- Select shows and their linked genre IDs using JOIN and GROUP BY
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

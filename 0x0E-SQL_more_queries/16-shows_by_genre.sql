-- Import the database dump from hbtn_0d_tvshows to your MySQL server

-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-- Select all shows and their linked genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

-- Import the database hbtn_0d_tvshows_rate dump to your MySQL server

-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;

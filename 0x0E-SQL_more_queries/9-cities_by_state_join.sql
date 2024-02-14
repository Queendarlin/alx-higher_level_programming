-- A script that lists all cities contained in the database hbtn_0d_usa

-- Select cities and corresponding state names using JOIN
SELECT id, name, name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY id ASC;

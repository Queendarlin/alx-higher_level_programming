-- To display the average temperature (in Fahrenheit) by city ordered by temperature (descending)
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

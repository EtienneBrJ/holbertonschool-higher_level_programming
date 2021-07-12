-- display the tops 3 cities temperature 
-- display the top 3 values of a column in a table
SELECT city, AVG(`value`) avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;

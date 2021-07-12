-- Lists all records of the table second_table
-- displays the score and the name (in this order)
-- dont list rows without a name value
-- listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

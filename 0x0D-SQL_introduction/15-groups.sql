-- Lists the number of records with the same score in the table second_table
-- result should display: the score, the number of records for this score with the label number
-- sorted by the number of records (descending)
SELECT score, COUNT(`score`) 'number' FROM second_table GROUP BY `score` ORDER BY `number` DESC;

-- this lists all records of second_table, don't list rows without name value
-- results shoudl display the score and name (in this order)
-- records should be listed by desending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
	ORDER BY score DESC;

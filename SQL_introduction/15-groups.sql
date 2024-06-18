-- Script lists numbers of records with the same score in the table second_table
-- 15-groups.sql
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
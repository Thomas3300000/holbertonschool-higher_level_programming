-- Script lists all records with a score >= 10 in the table second_table
-- 11-best_score.sql
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
-- Script lists all records of the table second_table
-- 16-no_link.sql
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
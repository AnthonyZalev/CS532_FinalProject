-- use regex to split words into table, then count words
-- \s+ matches one or more whitespace characters

SELECT COUNT(word) AS word_count
FROM (
  SELECT regexp_split_to_table(text_col, '\s+') AS word
  FROM shakespeare_processed sp 
) AS word_table;
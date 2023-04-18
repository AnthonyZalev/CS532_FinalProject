CREATE TABLE text_file (id INT, line VARCHAR(1000));

-- load text file into table (line by line)
LOAD DATA INFILE '/data/shakespeare_processed.txt' INTO TABLE text_file (line);

-- split text into words with regular expression
SELECT REGEXP_REPLACE(line, '[^a-zA-Z0-9 ]', '') AS words
FROM text_file;

-- get frequency of words
SELECT words, COUNT(*) AS frequency
FROM (
  SELECT REGEXP_REPLACE(line, '[^a-zA-Z0-9 ]', '') AS words
  FROM text_file
) t
GROUP BY words;

-- words by frequency
SELECT words, COUNT(*) AS frequency
FROM (
  SELECT REGEXP_REPLACE(line, '[^a-zA-Z0-9 ]', '') AS words
  FROM text_file
) t
WHERE words != ''
GROUP BY words
ORDER BY frequency DESC;

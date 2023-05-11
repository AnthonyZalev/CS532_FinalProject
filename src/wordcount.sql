-- use regex to split words into table, then count words
-- \s+ matches one or more whitespace characters

-- SELECT COUNT(word) AS word_count
-- FROM (
--   SELECT regexp_split_to_table(text_col, '\s+') AS word
--   FROM shakespeare_processed sp 
-- ) AS word_table;


-- updated sql scripts 
-- had to manually remove empty entries?
-- error when compared to native python is 229677 (14% more)

create table words as 
select regexp_split_to_table(column1, '\s+') as word
  from shakespeare_processed sp;
  
delete from words where trim(word) = '';

select count(*) from words;
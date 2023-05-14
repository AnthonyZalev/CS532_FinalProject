#!/bin/bash

# Create Single Node
cockroach start \
--insecure \
--store=node1 \
--listen-addr=localhost:26257 \
--http-addr=localhost:8080 \
--join=localhost:26257,localhost:26263,localhost:26264 \
--background

# Initialize
cockroach init --insecure --host=localhost:26257

# Nodelocal Upload
cockroach nodelocal upload ./new_shakespeare_processed_1.csv new_shakespeare_processed_1.csv --host=localhost:26257 --insecure
cockroach nodelocal upload ./new_shakespeare_processed_16.csv new_shakespeare_processed_16.csv --host=localhost:26257 --insecure
cockroach nodelocal upload ./new_shakespeare_processed_64.csv new_shakespeare_processed_64.csv --host=localhost:26257 --insecure


# Start built-in SQL Client
cockroach sql --insecure --host=localhost:26257 

# Run the following SQL commands for each repetition
create table table64(lines STRING);
# For tables 1, 16, 64 import directly from CSV file
import into table64 (lines) CSV DATA('nodelocal://1/new_shakespeare_processed_64.csv');
# For tables 256, 1024, 2048 insert n times from previous iteration. Ex:
insert into table256(lines) select * FROM table64; #4 times 


# Word Count
SELECT COUNT(word) AS word_count FROM (SELECT regexp_split_to_table(lines, '\s+') AS word FROM table1024) AS word_table;

# Word Count for distributed node diagrams run with 'Explain'
EXPLAIN ANALYZE(DISTSQL) SELECT COUNT(word) AS word_count FROM (SELECT regexp_split_to_table(lines, '\s+') AS word FROM table256) AS word_table;


# Kill Nodes 
ps -ef | grep cockroach | grep -v grep
kill -9 <PID>


# For Distributed Nodes, create more nodes and repeat SQL process
cockroach start \
--insecure \
--store=node2 \
--listen-addr=localhost:26258 \
--http-addr=localhost:8081 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background

cockroach start \
--insecure \
--store=node3 \
--listen-addr=localhost:26259 \
--http-addr=localhost:8082 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background

cockroach start \
--insecure \
--store=node4 \
--listen-addr=localhost:26260 \
--http-addr=localhost:8083 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background

cockroach start \
--insecure \
--store=node5 \
--listen-addr=localhost:26261 \
--http-addr=localhost:8084 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background

cockroach start \
--insecure \
--store=node6 \
--listen-addr=localhost:26262 \
--http-addr=localhost:8085 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background
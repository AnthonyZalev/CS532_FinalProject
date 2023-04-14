# Implement in pyspark dataframes, RDD, and sql all the stuff.


from pyspark.sql import SparkSession
from  pyspark.sql.functions import *

def start_spark():
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    return spark

def pyspark_dataframe(file, spark):
    logFile = file  
    logData = spark.read.text(logFile).cache()

    # Split by the " " delimiter, get the size of each lines "word" column, and sum them up.

    logData.select(size(split(logData.value, ' ')).alias('words')).agg(sum('words')).show()
    pass

def pyspark_rdd(file, spark):
    logFile = file  

    text_file = spark.sparkContext.textFile(logFile)

    counts = text_file.flatMap(lambda line: line.split(" ")) \
                           .map(lambda word: 1 ) \
                           .reduce(lambda a,b: a + b)
    print(counts)

    pass

def pyspark_sql(file):
    pass


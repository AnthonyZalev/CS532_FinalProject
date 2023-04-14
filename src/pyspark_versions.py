# Implement in pyspark dataframes, RDD, and sql all the stuff.


from pyspark.sql import SparkSession
from  pyspark.sql.functions import *


def pyspark_dataframe(file):
    logFile = file  
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    logData = spark.read.text(logFile).cache()

    # Split by the " " delimiter, get the size of each lines "word" column, and sum them up.

    logData.select(size(split(logData.value, ' ')).alias('words')).agg(sum('words')).show()
    pass

def pyspark_rdd(file):
    pass

def pyspark_sql(file):
    pass


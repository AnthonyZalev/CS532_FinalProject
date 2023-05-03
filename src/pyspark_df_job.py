from pyspark.sql import SparkSession
from  pyspark.sql.functions import *
import os
import time


if __name__ == "__main__":

    I = [1, 16, 64,256,1024,2048]
    #logFile = "src/data/shakespeare_processed_"
    logFile = "s3://anthonybucketcs532/532_data_files/shakespeare_processed_"
    spark = SparkSession.builder.appName("RDD_WordCount").getOrCreate()

    print("Pyspark_Dataframe Output:")

    for i in I:
        for j in range(5):
            output = logFile + str(i) + ".txt"
            #logData = spark.read.text(output).cache()
            print(output)
            start_time = time.time()
            logData = spark.read.text(output).cache()
            logData.select(size(split(logData.value, ' ')).alias('words')).agg(sum('words')).show()
            end_time = time.time() - start_time
            print('. Done in ' + str(end_time) + ' seconds.')

    spark.stop()
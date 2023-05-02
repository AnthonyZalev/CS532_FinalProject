from pyspark.sql import SparkSession
#from  pyspark.sql.functions import
import os
import time 

if __name__ == "__main__":
    
    I = [1, 16, 64, 256, 1024, 2048]

    logFile = "s3://anthonybucketcs532/532_data_files/shakespeare_processed"
    #write_file = "s3://anthonybucketcs532/532_project/data/rdd_output.txt"
    spark = SparkSession.builder.appName("RDD_WordCount").getOrCreate()

    for i in I:
        logfile = logFile + str(i) + ".txt"
        text_file = spark.sparkContext.textFile(logFile)
        start_time = time.time()
        counts = text_file.flatMap(lambda line: line.split(" ")) \
                            .map(lambda word: 1 ) \
                            .reduce(lambda a,b: a + b)
        end_time = time.time() - start_time
        print(f'Pyspark_RDD Output: {counts}. Done in {end_time} seconds.')

        output = f'Pyspark_RDD Output: {counts}. Done in {end_time} seconds.'
        #with open(write_file, 'w') as file:
        #    file.write(f'Pyspark_RDD Output: {counts}. Done in {end_time} seconds.')

        #spark.write.text(output).save(write_file)

    spark.stop()
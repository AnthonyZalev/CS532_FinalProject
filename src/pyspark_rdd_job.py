from pyspark.sql import SparkSession
#from  pyspark.sql.functions import
import os

if __name__ == "__main__":
    logFile = "src/data/new_shakespeare.txt"

    spark = SparkSession.builder.appName("RDD_WordCount").getOrCreate()

    text_file = spark.sparkContext.textFile(logFile)

    counts = text_file.flatMap(lambda line: line.split(" ")) \
                           .map(lambda word: 1 ) \
                           .reduce(lambda a,b: a + b)
    
    with open("src/data/rdd_output.txt", "w") as file:
        file.write(f'Pyspark_RDD Output: {counts}, for New Shakespeare File Sized {round((os.stat(logFile).st_size / (1024 * 1024)),2)} MB')
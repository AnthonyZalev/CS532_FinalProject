from enlarge_dataset import create_large_dataset
from pyspark_versions import pyspark_dataframe, pyspark_rdd, pyspark_sql, start_spark
from native_python import native_python_count
import time

def main():
    
    # Increase locally
    #create_large_dataset(2)
    #dataset = "src/data/new_shakespeare.txt"
    #spark = start_spark()

    # Run Pyspark with RDD
    #start_time= time.time()
    #pyspark_rdd(dataset, spark)
    #print(time.time() - start_time)

    # Run Pyspark with Dataframe
    #start_time= time.time()
    #pyspark_dataframe(dataset, spark)
    #print(time.time() - start_time)

    I = [1, 16, 64,256,1024,2048]
    #logFile = "src/data/shakespeare_processed_"
    logFile = "s3://anthonybucketcs532/532_data_files/shakespeare_processed_"
    #Run Native Python Word Count
    for i in I:
        output = logFile + str(i) + ".txt"
        start_time= time.time()
        native_python_count(output)
        print(f' FileSize: {i} and time: {time.time() - start_time}')
    

   

if __name__ == "__main__":
    main()

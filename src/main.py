from enlarge_dataset import create_large_dataset
from pyspark_versions import pyspark_dataframe, pyspark_rdd, pyspark_sql, start_spark
from native_python import native_python_count
import time

def main():
    # Increase locally
    #create_large_dataset(2)
    dataset = "src/data/new_shakespeare.txt"
    spark = start_spark()

    # Run Pyspark with RDD
    start_time= time.time()
    pyspark_rdd(dataset, spark)
    print(time.time() - start_time)

    # Run Pyspark with Dataframe
    start_time= time.time()
    pyspark_dataframe(dataset, spark)
    print(time.time() - start_time)

    # Run Native Python Word Count
    start_time= time.time()
    native_python_count(dataset)
    print(time.time() - start_time)
    

   

if __name__ == "__main__":
    main()

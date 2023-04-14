from enlarge_dataset import create_large_dataset
from pyspark_versions import pyspark_dataframe

def main():
    # Increase locally
    #create_large_dataset(2)
    dataset = "src/data/new_shakespeare.txt"
    pyspark_dataframe(dataset)

if __name__ == "__main__":
    main()

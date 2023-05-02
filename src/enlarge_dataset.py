import string

# The goal of this file is to make our dataset 1000 times bigger by appending it to itself 1000 times.
# This gives us a decent computational intensity that forces us to use memory managment techniques without being overwhelming.
# This file also contains the function that processes the dataset by removing punctuation and casting all letters to lowercase.

def append_file(file1, file2):
    #Append second file to the first.
    append_file = open(file1, "a")
    read_file = open(file2, "r")

    append_file.write(read_file.read())
    append_file.close()
    read_file.close()

def create_large_dataset(iterations, processed_file, final):
    # original = "src/data/shakespeare.txt"
    #final = "src/data/new_shakespeare.txt"

    # clear final folder:
    with open(final, 'w') as file:
        pass

    for _ in range(iterations):
        append_file(final, processed_file)

def process_dataset(write_file: str, read_file: str):
    r = open(read_file, 'r')
    w = open(write_file, 'w')

    for line in r:
        # removing punctuations and cast all letters to lowercase
        line = line.translate(str.maketrans("", "", string.punctuation)).lower()

        # only write to output if the line is not empty
        if line != "" and line != '\n':
            w.write(line)

    r.close()
    w.close()

def main():
    I = [1, 16, 64, 256, 1024, 2048]

    shakespear_file = "src/data/shakespeare.txt"
    processed_file = "src/data/shakespeare_processed.txt"

    process_dataset(processed_file, shakespear_file)

    for i in I:
        print(f"Creating shakespeare dataset {i} times larger")
        file = f"src/data/shakespeare_processed_{i}.txt"
        create_large_dataset(i, processed_file, file)

if __name__ == "__main__":
    main()

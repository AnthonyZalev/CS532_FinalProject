# The goal of this file is to make our dataset 1000 times bigger by appending it to itself 1000 times.
# This gives us a decent computational intensity that forces us to use memory managment techniques without being overwhelming.


def append_file(file1, file2):
    #Append second file to the first.
    append_file = open(file1, "a")
    read_file = open(file2, "r")

    append_file.write(read_file.read())
    append_file.close()
    read_file.close()

def create_large_dataset(iterations):
    original = "src/data/shakespeare.txt"
    final = "src/data/new_shakespeare.txt"

    # clear final folder:
    with open(final, 'w') as file:
        pass

    for _ in range(iterations):
        append_file(final, original)


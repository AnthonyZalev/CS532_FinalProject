# import 
from smart_open import smart_open
def native_python_count(filename):
    # Split by the " " delimiter and then calculated length of the resulting array.

    count = 0
    with smart_open(filename, 'rb') as s3_source:
        for line in s3_source:
            count += len(line.split(" "))
    print(count)
import re
def native_python_count(filename):
    # Split by the " " delimiter and then calculated length of the resulting array.

    def read_in_chunks(file_object, chunk_size=1000):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data
    count = 0
    with open(filename) as f:
        for piece in read_in_chunks(f):
            count += len(piece.split(" "))
            pass
    print(count)
def native_python_count(filename):
    # Split by the " " delimiter, get the size of each lines "word" column, and sum them up.
    with open(filename) as f:
        lines = f.read()
    word_count = len(lines.split())
    print("Word Count: ", word_count)
    pass
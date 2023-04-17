def native_python_count(filename):
    # Split by the " " delimiter and then calculated length of the resulting array.
    with open(filename) as f:
        lines = f.read()
    word_count = len(lines.split(" "))
    print("Word Count: ", word_count)
    pass
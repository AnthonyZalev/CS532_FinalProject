import string

r = open(r"new_shakespeare.txt", 'r')
w = open(r"shakespeare_processed.txt", 'w')

for line in r:
    # removing punctuations and cast all letters to lowercase
    line = line.translate(str.maketrans("", "", string.punctuation)).lower()

    # only write to output if the line is not empty
    if line != "" and line != '\n':
        w.write(line)

r.close()
w.close()
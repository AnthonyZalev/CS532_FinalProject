reps = [1, 16, 64, 256, 1024, 2048]
logFile = "shakespeare_processed_" 
with open("shakespeare_processed.txt") as f:
    lines = f.read()

for I in reps:
    output = logFile + str(I) + ".txt"
    for i in range(0,I):
        f = open(output, "a")
        f.write(lines)
f.close()

import numpy as np

filename = "data/marks.csv" 
infile =  open(filename, "r")

emptylist = []
for line in infile:

    # remove whitespaces and endlines chars
    line = line.strip()
    # print(line)
    v = line.split()

    for i in range(len(v)):
        print(v[i].strip())
        # print(v[i])


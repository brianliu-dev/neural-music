import sys
import os

f = open("input.txt", "a")
w = open(sys.argv[1], 'rt')
for line in w:
    f.write(line)
f.write("\n\n")
w.close()
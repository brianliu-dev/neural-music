import numpy as np
import string
import csv
import sys
import os

file_path = "../music-data/texts/"
PRINT_KEY = True

# Puts ascii characters into ascii_list
ascii_printable = string.printable
ascii_list = []
for char in ascii_printable:
	ascii_list.append(char)

# TODO
def inverse_conversion():
	# Need to convert back to midi format!
	position = ascii_list.index("ascii")    #to get pitch back from ascii character

# Writes from dictionary to file
def write_to_file(dictionary):
	f = open(file_path, 'w')
	k = list(dictionary.keys())
	k.sort()
	try:
		for key in k:
			line_to_write = ''
			if (PRINT_KEY):
				line_to_write = str(key) + dictionary[key] + " "
			else:
				line_to_write = dictionary[key] + " "
			f.write(line_to_write)		# python will convert \n to os.linesep
	finally:
		f.close() 


time_dict = {}

# Read file using CSV reader
f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
    	if row[2] == " Note_on_c" or row[2] == " Note_off_c":
	    	# Convert from [2, 265, Note_off_c, 0, 60, 127] to [265, ascii_list[pitch]] 
	    	r = [int(row[1][1:]), ascii_list[int(row[4][1:])]]
	    	if r[0] in time_dict:
	    		time_dict[r[0]] += r[1]
    		else:
    			time_dict[r[0]] = r[1]
finally:
    f.close()

# Write to file
string = sys.argv[1]
s = string.split("/")[-1]
file_path += s.split(".csv")[0] + ".txt"
write_to_file(time_dict)

import numpy as np
import string
import csv
import sys
import os

file_path = "../music-data/rnn-csv/"
test_csv = "../music-data/test.csv"
PRINT_KEY = True
note = [' Note_on_c', ' Note_off_c']

# Puts ascii characters into ascii_list
ascii_printable = string.printable
ascii_list = []
for char in ascii_printable:
	ascii_list.append(char)

def inverse_conversion(ascii):
	position = ascii_list.index(ascii)    #to get pitch back from ascii character
	return position

def create_rows(text):
	body = []
	previous_time = 0
	current_time = 0
	current_notes = []
	is_time = True
	for x in text:
		if is_time:
			is_time = False
			current_time = int(x)
			if (current_time < previous_time):
				current_time = previous_time
		else:
			is_time = True
			note_on = 0
			for a in x:
				if a in current_notes:
					note_on = 1
					current_notes.remove(a)
				else:
					note_on = 0
					current_notes.append(a)
				body.append(create_line(current_time, note_on, a))
		previous_time = current_time
	return body

def create_line(time, on_off, ascii):
	return ['2', time, note[on_off], '0', inverse_conversion(ascii), '127']

# Read epoch_.txt file 
f = open(sys.argv[1], 'rt')
print("Converting " + sys.argv[1] + " to csv...")

a = []
a = f.readline().split(" ")

# Getting csv wrappers for midi format
intro = []
ending = []

f = open(test_csv, 'rt')
try:
    reader = csv.reader(f)
    x = 0
    for row in reader:
    	if x < 32 or len(row) == 3 or row[0] == '3':
    		intro.append(row)
finally:
    f.close()

ending = intro[-5:]
intro = intro[:32]

body = create_rows(a)
ending[0][1] = body[-1][1]

# Write intro to file
string = sys.argv[1]
s = string.split("/")[-1]
file_path += s.split(".txt")[0] + ".csv"

with open(file_path, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(intro)
    writer.writerows(body)
    writer.writerows(ending)


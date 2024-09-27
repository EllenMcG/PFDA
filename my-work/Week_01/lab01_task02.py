# lab01_task02.py
# Week 01 - Lab 1 - Task 2
# Write python program to read in the data.csv created in lab01_task01.py 
# and output each line as a list

# Author Ellen McGrory

import csv

FILENAME= "data.csv" 
DATADIR = "../Week_01/"
with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    for line in reader: 
        print(line)

print(type(line))
# line is of the type list
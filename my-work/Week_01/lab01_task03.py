# lab01_task03.py
# Week 01 - Lab 1 - Task 3
# Modify the program to deal with the header line separately in lab01_task02.py

# Author Ellen McGrory

import csv

FILENAME= "data.csv" 
DATADIR = "../Week_01/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    linecount = 0 
    for line in reader: 
        if linecount == 0: # header 
            print(f"{line}\n-------------------") 
        else: # all subsequent rows 
            print(line) 
        linecount += 1
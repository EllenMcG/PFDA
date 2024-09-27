# lab01_task04.py
# Week 01 - Lab 1 - Task 4
# Modify the program lab01_task03.py to calculate the average age,

# Author Ellen McGrory

import csv

FILENAME= "data.csv" 
DATADIR = "../Week_01/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    linecount = 0 
    total = 0 
    for line in reader: 
        if linecount == 0: # header 
            pass 
        else: 
            total += int(line[1]) # line[1] for age column
        linecount += 1 
    print(f"average is {total/(linecount-1):.1f}") # -1 to take away 
    # header row from average calculation 
# lab01_task05.py
# Week 01 - Lab 1 - Task 5
# Modify the program lab01_task04.py to calculate the average age
# by reading in data.csv as a dictionary object using DictReader().

# Author Ellen McGrory

import csv

FILENAME= "data.csv" 
DATADIR = "../Week_01/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter=",") 
    total = 0 
    count = 0
    for line in reader: 
        total += int(line['age'])
        count +=1
    print(f"average is {total/(count):.1f}")
# lab01_task01.py
# Week 01 - Lab 1 - Task 1 
# Create a CSV file called data with the below data
# "id","age","name"
# 1,20,"Joe"
# 2,21,"Mary"
# 3,32,"Fred"

# Author Ellen McGrory

# Data populated to a CSV can be done manually with Excel, but python 
# can be used to do this by using a context manager with the 
# csv module

# resource used 
# https://www.freecodecamp.org/news/how-to-create-a-csv-file-in-python/

import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["id", "age", "name"] # column headers

    writer.writerow(field)
    writer.writerow(["1", "20", "Joe"])
    writer.writerow(["2", "21", "Mary"])
    writer.writerow(["3", "32", "Fred"])
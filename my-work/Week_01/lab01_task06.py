# lab01_task06.py
# Week 01 - Lab 1 - Task 6
# Write a program that prints JSON object from the below URL
# URL https://api.coindesk.com/v1/bpi/currentprice.json

# Author Ellen McGrory

import requests 

url ="https://api.coindesk.com/v1/bpi/currentprice.json" 
response = requests.get(url) 
data = response.json() 
print(data)

print(type(data))
# data is of type dictionary 

# Modify program to print the current price in Euros
print(data['bpi']['EUR']['rate_float'])
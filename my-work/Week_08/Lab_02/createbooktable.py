# Week 08 Lab 02 

import sqlite3

# create a database called pfda.db
con = sqlite3.connect('pfda.db')
cur = con.cursor() 

cur.execute("CREATE TABLE book(title, author, ISBN)") 
con.close()
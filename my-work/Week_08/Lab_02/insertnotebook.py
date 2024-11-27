# Week 08 Lab 02

import sqlite3

con = sqlite3.connect("pfda.db") 
cur = con.cursor()

# check that no data exists in book
result = cur.execute('select * from book') 
print(result.fetchone())

# insert data 
sql = '''INSERT INTO book VALUES 
            ('Harry Pothead', 'Just Kidding Really', "112344"), 
            ('Harry Potter does something profound', 'JK Rowling', "123444")'''

# The below will lead to SQL injection 
cur.execute(sql)
con.commit() # commit updates

result = cur.execute("select * from book") 
print(result.fetchone()) 
con.close()

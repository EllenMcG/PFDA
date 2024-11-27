# Week 08 Lab 03
# Delete data

import mysql.connector 


db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='', 
    database='wsaa'
) 


cursor = db.cursor() 

sql='delete from student where id = %s' 
values = (1,) 

cursor.execute(sql, values) 

db.commit() 
print('delete done')
cursor.close() 
db.close()

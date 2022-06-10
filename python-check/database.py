#!/usr/bin/python

import sqlite3

# connect to database

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table
# c.execute("""CREATE TABLE customers(
#           firstname text,
#           lastname text,
#           email text

# )""")

# my_customers = [('riyan','nandana','riyan@email.com'),
#                 ('neelu','pasupu','neelu@email.com'),
#                 ('kishore','hari','hari@email.com'), 
#                ]

# c.executemany("INSERT INTO customers VALUES(?,?,?)", my_customers)

# query the database
c.execute("SELECT * FROM customers")
# c.fetchone()
#c.fetchmany()
item = c.fetchall()

print("Name" + "\t\temail")
print("......." + "\t\t.......")

for items in item:
    print(items[0] + "\t\t" + items[2])




print("command excuted successfully")


#DATATYPES
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#commit our command

conn.commit()

# close to connection

conn.close()

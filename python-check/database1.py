#!/usr/bin/python

import sqlite3


# connect to database

#conn = sqlite3.connect('employee.db')

#create a cursor

#c = conn.cursor()

# create a table

# c.execute("""CREATE TABLE employees(
#          first_name text,
#          last_name text,
#          salary int       
#    ) 
# """)

# add a new record to the table

def add_one(first,last,salary):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees VALUES(?,?,?)",(first,last,salary))
    conn.commit()
    conn.close()


# query the db and return all records

def show_all():
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM employees")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()


# delete record from table

def delete_one(id):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE rowid = (?)",id)
    conn.commit()
    conn.close()

# add many records to table

def add_many(list):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.executemany("INSERT INTO employees VALUES (?,?,?)",(list))
    conn.commit()
    conn.close()


def sal_lookup(salary):
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from employees WHERE salary = (?)",(salary,))
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()



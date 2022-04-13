#!/usr/bin/python

import sys
print(sys.version)
print(sys.executable)

num = 3.4
print(type(num))

x = "Hello World"
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = True
print(type(x))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    #int
y = 3.45 #float
z = 2j   #complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


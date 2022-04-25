#!/usr/bin/python

# x = lambda a : a + 10
# print(x(5))

# x = lambda a ,b : a * b
# print(x(5,6)) 

# x = lambda a ,b ,c : a + b + c
# print(x(5,6,7))

def myfunction(n):
    return lambda a : a * n
x = myfunction(2)
y = myfunction(3)
print(x(11))
print(y(11))    

#!/usr/bin/python

print("initially :",dir())

num =20

def f1():
    n =10
    print("inside the function:",dir())
f1()

print("outside the function:",dir())
#!/usr/bin/pytthon

########## here having four scope variables.
######### theya are local,global,enclosed,built-in

##### y is global variable

y =10

def outer():
    z =11 ##### z is non-local variable(enclosed scope)

    def inner():

        x = 4 ##### x is local variable

        global y

        y = y+1

        nonlocal z

        z = z-1
        
        print("x is local variable :",x)

        print("inside the function :",z)

        print("inside the global:",y)

    inner()

    print("global value:",y)

    print("non local value:",z)

outer()    


    

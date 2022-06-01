#!/usr/bin/python

######## class decorators ########

# def check_name(method):
#     def inner(name_ref):
#         if name_ref.name == "riyan":
#             print("we both are same name also")
#         else:
#             method(name_ref)
#     return inner

# class printing:
#     def __init__(self,name):
#         self.name = name
#     @check_name 
#     def print_name(self):
#         print("entered the username:",self.name)

# a = printing("riyan")
# a.print_name()           



# class printing:
#     def __init__(self,name):
#         self.name = name
#     def printname(self):
#         print("entered the username:",self.name)

# p = printing("riyan")
# p()

# class printing:
#     def __init__(self,name):
#         self.name = name
#     def __call__(self):
#         print("entered the username:",self.name)
# p = printing("riyan")
# p()



# class Decorator:
#     def __init__(self,func):
#         self.func = func
#     def __call__(self):
#         str1 = self.func()
#         return str1.upper()

# @Decorator
# def greet():
#     return "good morning"

# print(greet())           



class checkdiv:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
    
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i == 0 :
                return "you can not divide any number"
            else:
                return self.func(*args,**kwargs)    

@checkdiv
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0    

    
    
@checkdiv
def div1(a,b,c):
    try:
        return a/b/c
    except ZeroDivisionError:
        return 0 

    
print(div(10,5))
print(div1(10,5,0))



                                
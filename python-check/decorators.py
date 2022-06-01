#!/usr/bin/python

# def outer():
#     x = 3
#     def inner():
#         y = 5
#         result = x+y
#         return result
#     return inner

# a = outer()
# #print(a.__name__)
# print(a())

# def function1():
#     print("hi to call the function1")
# def function2(func):
#     print("hi i am function2 now i will call on function1")
#     func()
# function2(function1)            

###### decorate function #########

# def str_upper(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner

# @str_upper

# def print_str():
#     return "good morning"
# print(print_str())    


# def div_dec(func):
#     def inner(x,y):
#         if y == 0:
#             return "give proper input"
#         return func(x,y)
#     return inner

# @div_dec
# def div(a,b):
#     return a/b
# print(div(4,0))                



###### multiple decorator using single function #####

# def upper_d(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner

# def split_d(func):
#     def wrapper():
#         str2 = func()
#         return str2.split()
#     return wrapper

# @split_d
# @upper_d
# def ordinary():
#     return "good morning"
# print(ordinary())    
                    

###### decorator contains parameter ########

# def outter(exper):
#     def upper_d(func):
#         def inner():
#            str1 = func() + exper
#            return str1.upper()
#         return inner
#     return upper_d

# @outter(" riyan ")
# def ordinary():
#     return "good morning"
# print(ordinary())    



####### single decorator using multiple functions ########

def div_dec(func):
    def inner(*args):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i == 0 :
                return "give proper input"
        return func(*args)
    return inner

@div_dec
def div1(a,b):
    return a/b
@div_dec    
def div2(a,b,c):
    return a/b/c    
print(div1(10,5))
print(div2(0,10,5))








def hello_fun():
    return "hello function"

print(hello_fun())

def hello_1(greetings):
    return '{} ! everyone'.format(greetings)

print(hello_1('Hi'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['a','b','c','d']
info = {'name':'e','age':22}
student_info(*courses,**info)


def avg(n1,n2,n3):
    return (n1+n2+n3)/3.0

print("welcome average values :\n")
result1 = avg(1,2,3)
result2 = avg(10,20,30)
result3 = avg(3.1,2,4.5)    

print(result1)
print(result2)
print(result3)



def sum(a,b):
    return a+b

x = int(input("\n enter the value of x ="))
y = int(input("enter the value of y="))
z = sum(x,y)
print("sum of", x ,"and" ,y ,"is :" ,z )    
    
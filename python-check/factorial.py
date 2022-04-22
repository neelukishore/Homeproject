#¡/usr/bin/python

####### factorial using loop #########


num = int(input("enter a number: "))

fact = 1 

for i in range(1, num + 1):
    fact = fact*i
print("the factorial of ",num,"is",fact)    



######factorial using recursive########

def fact(x):
    if x == 0:
        return 1
    else:
        return (x * fact(x - 1))

n = int(input("enter a number: "))
result = fact(n)
print("the factorial of",n,"is",result)             
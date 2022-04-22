#¡/usr/bin/python

def fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibbo(n-1) + fibbo(n-2))

nterms = int(input("\n\nenter the terms:  "))
if nterms <= 0:
    print("enter the positive integer")
else:
    print("fibbonacci sequence: ")
    for i in range(nterms):
        print(fibbo(i))


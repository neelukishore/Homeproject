

def sum(*args):
	s=0
	for i in args:
		s+=i
	print("sum is:",s)	
sum(10,20,30)

def my_val(a,b,c,d):
	print(a,b,c,d)

args = [1,2,3,4]
my_val(*args)

def value(a,b,c):
	print(a,b,c)

a = {'a':"one",'b':"two",'c':"three"}
value(**a)	


def func(**kargs):
	for i,j in kargs.items():
	    print(i,j)
func(name='one',game='football',role=10)






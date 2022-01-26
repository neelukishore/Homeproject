
#/usr/bin/python

li=[9,7,6,8,4,5,3,2,1]
s_li=sorted(li)
print("sorted variable:\t",s_li)
print("original variable:\t",li)
############
s_li=sorted(li,reverse=True)
print("sorted variable:\t",s_li)
li.sort()
print("original variablr:\t",li)
######

di={'name':'riyan','age':None,'job':'progamming','os':'Mac'}
s_dic=sorted(di)
print("sorted variable:\t",s_dic)


###############
class Employee():
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
	def __repr__(self):
		return '({},{},${})'.format(self.name,self.age,self.salary)


def main():	
	emp1 = Employee('riyan',30,1000)
	emp2 = Employee('neelu',32,2000)
	emp3 = Employee('kishore',34,3000)
	employees = [emp1,emp2,emp3]
	print(employees)
	s_employees = sorted(employees, key=e_sort)
	print(s_employees)


def e_sort(emp):
    return emp.name	


if __name__ == '__main__':
   main()


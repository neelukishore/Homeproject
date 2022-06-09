#!/usr/bin/python


######## object oriented techniques #########

# class Student:
#     clg = 'xyz'

#     def __init__(self,rollno,name):
#         self.rollno = rollno
#         self.name = name
#     def display(self):
#         print("rollno:",self.rollno)
#         print("name:",self.name)
#         print("collage name:",Student.clg)
#         print("....................")

# s1 = Student("x123","riyan")
# s1.display()

# s2 = Student("y123","neelu")
# s2.display()


######### multi level inheritance ##########

# class Person:
#     def display(self):
#         print("this is base class")

# class Employee(Person):
#     def printing(self):
#         print(" this is dervied employee class")

# class Programmer(Employee):
#     def show(self):
#         print(" this is dervied programmer class")

# p1 = Programmer()
# p1.display()
# p1.printing()
# p1.show()                        


######## multiple inheritance ##########

# class Father:
#     def printing(self):
#         print(" this is base class1")

# class Mother:
#     def show(self):
#         print("this is base class2")

# class child(Father,Mother):
#     def display(self):
#         print("this is dervied class")

# c1 = child()
# c1.printing()
# c1.show()
# c1.display()



class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)      

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay) 
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay,employees = None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("......>",emp.fullname())


dev1 = Developer('nadana','riyan',50000,'python')
dev2 =Developer('pasupu','neelu',40000,'java')
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

mag1 = Manager('hari','kishpore',60000,[dev1])
print(mag1.email)
mag1.add_emp(dev2)
mag1.remove_emp(dev2)
mag1.print_emp()






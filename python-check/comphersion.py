#!/usr/bin/python

# num = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for i in num:
#     my_list.append(i)
# print(my_list)


# name1 = ['kishore','neelu','riyan']
# name2 = ['father','mother','son']
# my_dict= {}
# for i,j in zip(name1,name2):
#     my_dict[i] = j
# print(my_dict)


# nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

# my_set = set()
# for i in nums:
#     my_set.add(i)
# print(my_set)


######### sorting ##########

# num = [6,5,7,8,9,3,4,2,1,10]

# s_li = sorted(num,reverse=True)

# num.sort(reverse=True)
# print('original list :\t',num)
# print('sorted list:\t',s_li)




class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary =salary
    def __repr__(self):
        return'({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('neelu',32,4000)
e2 = Employee('kishore',34,5000)
e3 = Employee('riyan',5,60000)
#print(e1)
employees = [e1,e2,e3]
# def e_sorted(emp):
#     return emp.salary
s_employees = sorted(employees,key = lambda e : e.age)
print(s_employees)
        
         



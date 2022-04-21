#!/usr/bin/python

courses = ['maths','physics','chemistry','english']

print(courses[3])
print(courses[-2])
print(courses[:2])

courses.append('art')

courses.insert(0,'social')

print(courses)

print(len(courses))

print(type(courses))

##### using extend ##########

value1 = [1,2,3,4,5]
value2 = [6,7,8,9,10]

#####using insert#####

#value1.insert(0,value2)
#print(value1)

#######using extend#######

value1.extend(value2)

#######using remove ,pop #######
value1.remove(3)
popped = value1.pop()
print(popped)
print(value1)

######## using sort #########
num = ['a','b','d','c','f','e']
num.sort(reverse=True)
num_sort = sorted(num)
print(num_sort)
print(num)

####### using loop ##########
items = ['apple','ball','cat','dog']
for item in items:
    print(item)

########using enumerate #######
items = ['apple','ball','cat','dog']
for index,item in enumerate(items,start=1):
    print(index,item)  

#####using join #######
items = ['apple','ball','cat','dog']

str1 = '-'.join(items)
new_list = str1.split('-')
print(str1)
print(new_list)



######mutable#######

list_1 = ['telugu','english','hindi','maths']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'art'
print(list_1)
print(list_2)

###### immutable ########
tuple_1 = ('telugu','english','hindi','maths')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'art'
# print(tuple_1)
# print(tuple_2)

###### using set ########

set_course1 = {'maths','telugu','english','hindi'}
set_course2 = {'maths','telugu','art','design'}
print(set_course1.intersection(set_course2))


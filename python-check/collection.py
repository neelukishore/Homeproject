
courses=['a','b','c','d']
courses.append('e')
print(courses)

print(courses[3])
print(courses[0:2])

print(len(courses))

courses.insert(4,'f')
print(courses)

courses1=['0','1']
courses.extend(courses1)
print(courses)

courses.pop()
print(courses)

popped=courses.pop()
print(popped)

num=[1,2,3,4]
num.sort(reverse=True)
print(num)

print(courses.index('f'))

for course in courses:
    print(course) 

for index,course in enumerate(courses, start=0):
     print(index,course)

 #muttable    

list1=['maths','physics','chemistry']
list2=list1
print(list1)
print(list2)
list1[0]='social'
print(list1)
print(list2)

#immuttable

tuple1=('maths','chemistry','physics')
tuple2=tuple1
print(tuple1)
print(tuple2)
#tuple1[0]='science'
print(tuple1)
print(tuple2)

#sets
set1={'a','b','c','d','e'}
set2={'a','b','f','g','e'}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))









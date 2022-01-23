
#Dictionaries
student={'name':'riyan','age':3,'games':['vallyball','football']}
student['phone']=5555
student.update({'name':'kishore','age':34})
print(student)

age=student.pop('age')
print(student)
print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for item in student.items():
	print(item)

for key,value in student.items():
    print(key,value)     	 





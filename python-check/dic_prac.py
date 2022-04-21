#¡/usr/bin/python

student = {
    "name" : "neelu",
    "branch":"cse",
    "courses": ['maths','social']   
    }
student['name'] = 'kishore'
student['phone'] = '555555555'   
########delete
del student['phone']

branch = student.pop('branch')
print(student)    
print(branch)

for key,value in student.items():
    print(key,value)
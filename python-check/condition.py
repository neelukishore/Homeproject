#¡/usr/bin/python

language = 'java'

if language == 'python':
    print('python language')
elif language == 'java':
    print('java language')
else:
    print('not match')    

user = 'admin'
logged_in = True
if user == 'admin' and logged_in:
    print('admin page')

else:
    print('bad cred')


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
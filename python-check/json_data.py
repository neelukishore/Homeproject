import json

with open('employee.json') as f:
	data = json.load(f)
	#print(data)
	#print(type(data))

for k,v in data.items():
	#print(data)
	for each_value in v:
		#print(each_value)
		if each_value['department'] == 'HR':
			print(each_value['id'],"->",each_value['name'])


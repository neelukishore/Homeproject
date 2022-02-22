

import yaml

#with open('data.yaml') as f:
    
 #   docs = yaml.load_all(f, Loader=yaml.FullLoader)

  #  for doc in docs:
        
   #     for k, v in doc.items():
    #        print(k, "->", v)


users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

#print(yaml.dump(users))

with open('employee.yaml','r') as _emp:
    data_emp = yaml.safe_load(_emp)
'''
print(data_emp)
print(type(data_emp))
for k,v in data_emp.items():
    print(k, " -> ", v)

for each_emp in data_emp.values():
    #print(each_emp)
    for emp_info in each_emp:
        print(emp_info)
        for emp_info_tech in emp_info['Technologies']:

            if emp_info_tech == 'JAVA':
                print(emp_info['current_company'])
                print(emp_info['firstname'])

for k,v in data_emp.items():
    for each_val in v:
        print(each_val['firstname'])
        if each_val['firstname'] == 'Neelu':
            print(each_val['Technologies'])
            if "MYSQL" not in each_val['Technologies']:
            #if "MYSQL" not in ['AWS', 'BIGDATA', 'POSTGRES']:
                print("MYSQL TECH not found")
            else:
                print("MYSQL FOUND for Neelu")
'''

for k,v in data_emp.items():
    #print(k,"_",v)
    for data_value in v:
        #print(data_value)
        if data_value['firstname'] == 'hari':
            data_value['current_company'] = 'ABCD'


with open('new _emp.yaml' , 'w') as f:
    doc = yaml.dump(data_emp,f)
    
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompsSci']}
print(student) # {'name': 'John', 'age': 25, 'courses': ['Math', 'CompsSci']}
print(student['name']) # John
print(student['courses']) # ['Math', 'CompsSci']
print(student.get('name')) # John
print(student.get('gender', 'Not Found')) # If gender is not there, it returns Not Found

student['phone']='555-555-555'
print(student) # {'name': 'John', 'age': 25, 'courses': ['Math', 'CompsSci'], 'phone': '555-555-555'}

# Pop method
age = student.pop('age')
print(student) # {'name': 'John', 'courses': ['Math', 'CompsSci'], 'phone': '555-555-555'}
print(age) # 25

# functions
print(len(student)) # 3
print(student.keys()) # dict_keys(['name', 'courses', 'phone'])
print(student.values()) # dict_values(['John', ['Math', 'CompsSci'], '555-555-555'])
print(student.items()) # dict_items([('name', 'John'), ('courses', ['Math', 'CompsSci']), ('phone', '555-555-555')])

for key,value in student.items():
    print(key,value)
# name John
# courses ['Math', 'CompsSci']
# phone 555-555-555

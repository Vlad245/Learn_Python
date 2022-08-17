students = {
    'alex' : 258,
    'max' : 227,
    'anna' : 278
}

print(students)
print(students['anna'])

#dict.get(x) - Getting an element from the dictionary
print(students.get('alex'))

students['andrey'] = 268
print(students)
students['andrey'] = 177
print(students)

#dict.setdafeult(x) - Adding a new element with None key
students.setdefault('oleg')
print(students)

#dict.pop(x) - Removing an element with key from the dictionary
students.pop('oleg')
print(students)

#dict.keys() - Getting all keys from the dictionary
print(students.keys())
print(type(students.keys()))
key_list = list(students.keys())
print(key_list)

#dict.values() - Getting all values from the dictionary
print(students.values())
print(type(students.values()))

#check and values in the dictionary
print('anna' in students)
print('peter' not in students)

print(students['max'])
print(students.get('anna'))

capitals = dict()

capitals['Ukraine'] = 'Kyiv'
capitals['Spain'] = 'Madrid'
capitals['Germany'] = 'Berlin'
capitals['England'] = 'London'

countries = ['Ukraine', 'Spain', 'USA', 'Germany', 'Italy', 'England', 'Ukraine']

for country in countries:
    if country in capitals:
        print('Capital of the ' + country + ': ' + capitals[country])
    else:
        print('There is no such country in the database ' + country)

A = dict(zip('abcdef', list(range(6))))
for key in A:
    print(key, A[key])

A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)

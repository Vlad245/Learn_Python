import random

#List comprehension 
list = [random.randint(0, 10) for i in range(5)]

print(list)
print(min(list))
print(max(list))
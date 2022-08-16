import random

#Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов
# (почти как массив, но типы элементов могут отличаться).

#Creating a new list

list = [124113, 'Klopp', 46363, 34, True, [1, 2, 3, 4]]
print(list)

# list.append(x) - Adding a new element to the end of the list
list.append([list[-1]])
list.append(False)
list.append('Sindy')
print(list)

#list.extend(list_2) - Extend list, adding all elements from the list_2 to the end of the list
list_2 = ['Andrew Robertson', 'Virgil van Dijk', 'Mohhamad Salah', 'Boby Firmino', 'Tiago']

list.extend(list_2)
print(list)

#list.insert(i, x) - Insert an value 'x' to the element 'i'
list_2.insert(1, 26)
list.insert(0, [4, 3, 2, 1])
list.insert(1, False)
list_2.insert(3, 4)
list_2.insert(5, 11)
list_2.insert(7, 9)
list_2.insert(9, 6)
print(list)
print(list_2)

#list.remove(x) - Removing first element in the list with value 'x'. ValueError when ther is no such value
list.remove('Sindy')
list.remove(34)
list.remove(True)
list.remove([1, 2, 3, 4])
print(list)

#list.count(x) - Returns number of elements with valaue 'x'
count = list_2.count(6)
count = list.count(False)
print(count)

#list.reverse - Reverse a list
list.reverse()
list_2.reverse()
print(list)
print(list_2)

#list.clear() - Crear the list
list.clear()
list_2.clear()
#print(list)
#print(list_2)


#Create a new list with random numbers
new_list = []

for elem in range(int(input())):
    number = random.randint(0, 10000)
    new_list.append(number)

print(new_list)

# дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]

string = 'ab12c59p7dq'

digits = []

for symbol in string:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)







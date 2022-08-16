print("Hello! \n Input desire number 1: ")
number1 = float(input())
print("Input desire number 2:")
number2 = float(input())
print("Please select an action typing an appropriate sign: 1 - addition, 2 - deletion, 3 - division, 4 - multiplication")
action = int(input())

result = None

if action == 1:
    result = number1 + number2
    print(result)
elif action == 2:
    result = number1 - number2
    print(result)
elif action == 3:
    result = number1 / number2
    print(result)
elif action == 4:
    result = number1 * number2
    print(result)
elif action == 0 or action > 4:
    print("Error! You entered incorrect sign. Please, try again.")


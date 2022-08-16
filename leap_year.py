def is_year_leap(number):
    if number % 4 == 0 and number % 100 != 0:
        return 'True'
    elif number % 400 == 0:
        return 'True'
    else:
        return 'False'

year = int(input())

print(is_year_leap(year))

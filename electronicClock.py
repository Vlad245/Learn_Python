n = int(input())

hours = (n // 60) % 24
minutes = n % 60
days = n // (60 * 24)

print(hours, ':', minutes)
print(days)

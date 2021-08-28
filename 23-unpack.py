numbers = (1, 2, 3)
print(numbers)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

x, y, z = numbers
print(y)

x, _, _ = numbers
print(x)

x, *b = numbers
print(x)
print(b)
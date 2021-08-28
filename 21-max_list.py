numbers = [5, 8, 9, 2]

# cara 1
max_number = max(numbers)
print(max_number)

# cara 2
numbers.sort()
max_number = numbers[-1]
print(max_number)

# cara 3
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

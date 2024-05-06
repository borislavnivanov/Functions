text = input().split()

numbers = []
for char in text:
    numbers.append(abs(float(char)))

print(numbers)

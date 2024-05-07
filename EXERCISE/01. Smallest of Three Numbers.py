def smallest_number(n: list):
    return min(n)


numbers: list = []
for i in range(3):
    numbers.append(int(input()))

result = smallest_number(numbers)
print(result)

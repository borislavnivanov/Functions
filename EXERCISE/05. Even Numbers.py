def get_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


text = str.split(input())
number = []
for char in text:
    number.append(int(char))

even: list = list(filter(get_even, number))

print(even)

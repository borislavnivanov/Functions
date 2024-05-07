def is_even(l: list) -> tuple:
    even_list = []
    odd_list = []

    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    _sum_even = sum(even_list)
    _sum_odd = sum(odd_list)
    return _sum_even, _sum_odd


text = input()
numbers = []
for char in text:
    numbers. append(int(char))

sum_even, sum_odd = is_even(numbers)

print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

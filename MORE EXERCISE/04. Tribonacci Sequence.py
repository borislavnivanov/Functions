n = int(input())


def counter(_n):
    numbers = [1, 0, 0]
    for _ in range(_n):
        new_number = sum(numbers)
        print(new_number, end=' ')
        numbers.append(new_number)
        numbers.pop(0)

counter(n)

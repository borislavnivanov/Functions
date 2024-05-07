def add_and_subtract(n1: int, n2: int, n3: int):
    def sum_numbers():
        return n1 + n2

    def subtract(n_sum):
        return n_sum - n3

    return subtract((sum_numbers()))


num1, num2, num3 = int(input()), int(input()), int(input())

print(add_and_subtract(num1, num2, num3))

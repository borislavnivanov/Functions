def calculate_factorial(num: int) -> int:
    factorial = 1
    for i in range(1, num):
        factorial += factorial * i
    return factorial


fact_num_1 = calculate_factorial(int(input()))
fact_num_2 = calculate_factorial(int(input()))

print(f'{fact_num_1 / fact_num_2:.2f}')

def get_dividers(num: int):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


get_dividers(int(input()))

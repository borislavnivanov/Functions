text = str.split(input())
number = []
for i in text:
    number.append(int(i))

sorted_list = sorted(number)

print(f'The minimum number is {sorted_list[0]}\nThe maximum number is {sorted_list[-1]}\n'
      f'The sum number is: {sum(sorted_list)}')

text = input().split(' ')

result = []


def rounder(num: str) -> int:
    n = float(num)
    return round(n)


for i in range(len(text)):
    result.append(rounder(text[i]))

print(result)

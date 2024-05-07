def printer(start: int, end: int):
    for i in range(start + 1, end):
        result.append(chr(i))


char1, char2 = ord(input()), ord(input())
result = []
printer(char1, char2)

for char in result:
    print(char, end=' ')

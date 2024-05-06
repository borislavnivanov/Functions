text = input()
n = int(input())

repeat = lambda _text, _n: _text * _n
result = repeat(text, n)

print(result)

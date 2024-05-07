def is_palindrome(n):
    mirror = n[:: -1]
    if mirror == n:
        print('True')
    else:
        print('False')


text = str.split(input(), ', ')
for n in text:
    is_palindrome(n)

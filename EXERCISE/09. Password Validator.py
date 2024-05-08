import re


def password_length(_password: str) -> int:
    return len(_password)


def password_contains(_password: str) -> bool:
    for char in _password:
        if re.fullmatch(r'[\w\d]+', _password) is None:
            return False
        else:
            return True


def digits_checker(_password: str) -> bool:
    digit_count = 0
    for char in _password:
        if str.isdigit(char):
            digit_count += 1

    if digit_count >= 2:
        return True
    else:
        return False


def password_checker(password_check: str) -> None:
    length = True
    contains = True
    digits = True

    if not 6 <= password_length(password_check) <= 10:
        print('Password must be between 6 and 10 characters')
        length = False
    if not password_contains(password_check):
        print('Password must consist only of letters and digits')
        contains = False
    if not digits_checker(password_check):
        print('Password must have at least 2 digits')
        digits = False
    if length and contains and digits:
        print('Password is valid')


text = input()
password_checker(text)
